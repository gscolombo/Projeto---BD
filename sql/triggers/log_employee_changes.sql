CREATE OR REPLACE FUNCTION log_funcionario_changes_func()
RETURNS TRIGGER AS $$
BEGIN
    -- Caso seja atualizacao
    IF TG_OP = 'UPDATE' THEN
        INSERT INTO funcionario_log(id_employee, operation, old_data, new_data)
        VALUES (
            OLD.codigo,
            'UPDATE',
            to_jsonb(OLD),
            to_jsonb(NEW)
        );
        RETURN NEW;
    -- Caso seja insercao
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO funcionario_log(id_employee, operation, new_data)
        VALUES (
            NEW.codigo,
            'INSERT',
            to_jsonb(NEW)
        );
        RETURN NEW;
    -- Caso seja exclusao
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO funcionario_log(id_employee, operation, old_data)
        VALUES (
            OLD.codigo,
            'DELETE',
            to_jsonb(OLD)
        );
        RETURN OLD;
    END IF;

END;
$$ LANGUAGE plpgsql;

-- Trigger que chama a funcao apos qualquer operacao em "funcionario"
DROP TRIGGER IF EXISTS funcionario_changes_trigger ON funcionario;

CREATE TRIGGER employee_changes_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON funcionario
FOR EACH ROW
EXECUTE PROCEDURE log_funcionario_changes_func();
