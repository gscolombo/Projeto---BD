CREATE TABLE IF NOT EXISTS company_log (
    id_log SERIAL PRIMARY KEY,
    id_company INT,
    changed_at TIMESTAMP DEFAULT NOW(),
    operation TEXT,
    old_data JSONB,
    new_data JSONB
);

-- Funcao que registra mudanças na tabela "company"
CREATE OR REPLACE FUNCTION log_company_changes_func()
RETURNS TRIGGER AS $$
BEGIN
    -- Caso seja atualizacao
    IF TG_OP = 'UPDATE' THEN
        INSERT INTO company_log(id_company, operation, old_data, new_data)
        VALUES (
            OLD.id_company,
            'UPDATE',
            to_jsonb(OLD),
            to_jsonb(NEW)
        );

    -- Caso seja insercao
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO company_log(id_company, operation, new_data)
        VALUES (
            NEW.id_company,
            'INSERT',
            to_jsonb(NEW)
        );

    -- Caso seja exclusao
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO company_log(id_company, operation, old_data)
        VALUES (
            OLD.id_company,
            'DELETE',
            to_jsonb(OLD)
        );
    END IF;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;


-- Trigger que chama a funcao apos qualquer operacao em "company"
DROP TRIGGER IF EXISTS company_changes_trigger ON company;

CREATE TRIGGER company_changes_trigger
AFTER INSERT OR UPDATE OR DELETE
ON company
FOR EACH ROW
EXECUTE PROCEDURE log_company_changes_func();
