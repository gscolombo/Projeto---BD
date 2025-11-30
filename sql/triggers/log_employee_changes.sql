CREATE TABLE IF NOT EXISTS employee_log (
    id_log SERIAL PRIMARY KEY,
    id_employee INT,
    changed_at TIMESTAMP DEFAULT NOW(),
    operation TEXT,
    old_data JSONB,
    new_data JSONB
);

-- Funcao que registra mudanças na tabela "employee"
CREATE OR REPLACE FUNCTION log_employee_changes_func()
RETURNS TRIGGER AS $$
BEGIN
    -- Caso seja atualizacao
    IF TG_OP = 'UPDATE' THEN
        INSERT INTO employee_log(id_employee, operation, old_data, new_data)
        VALUES (
            OLD.id_employee,
            'UPDATE',
            to_jsonb(OLD),
            to_jsonb(NEW)
        );
    -- Caso seja insercao
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO employee_log(id_employee, operation, new_data)
        VALUES (
            NEW.id_employee,
            'INSERT',
            to_jsonb(NEW)
        );
    -- Caso seja exclusao
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO employee_log(id_employee, operation, old_data)
        VALUES (
            OLD.id_employee,
            'DELETE',
            to_jsonb(OLD)
        );
    END IF;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Trigger que chama a funcao apos qualquer operacao em "employee"
DROP TRIGGER IF EXISTS employee_changes_trigger ON employee;

CREATE TRIGGER employee_changes_trigger
AFTER INSERT OR UPDATE OR DELETE
ON employee
FOR EACH ROW
EXECUTE PROCEDURE log_employee_changes_func();
