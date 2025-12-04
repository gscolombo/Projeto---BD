CREATE OR REPLACE FUNCTION log_empresa_changes_func()
RETURNS TRIGGER AS $$
BEGIN
    -- Caso seja atualizacao
    IF TG_OP = 'UPDATE' THEN
        INSERT INTO empresa_log(id_empresa, operation, old_data, new_data)
        VALUES (
            OLD.cnpj,
            'UPDATE',
            to_jsonb(OLD),
            to_jsonb(NEW)
        );
        RETURN NEW;
    -- Caso seja insercao
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO empresa_log(id_empresa, operation, new_data)
        VALUES (
            NEW.cnpj,
            'INSERT',
            to_jsonb(NEW)
        );
        RETURN NEW;
    -- Caso seja exclusao
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO empresa_log(id_empresa, operation, old_data)
        VALUES (
            OLD.cnpj,
            'DELETE',
            to_jsonb(OLD)
        );
        RETURN OLD;
    END IF;

END;
$$ LANGUAGE plpgsql;

-- Trigger que chama a funcao apos qualquer operacao em "empresa"
DROP TRIGGER IF EXISTS empresa_changes_trigger ON empresa;

CREATE TRIGGER empresa_changes_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON empresa
FOR EACH ROW
EXECUTE PROCEDURE log_empresa_changes_func();