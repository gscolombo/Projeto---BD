CREATE OR REPLACE PROCEDURE delete_company (p_cnpj VARCHAR(14))
LANGUAGE plpgsql
AS $$
DECLARE
    employee RECORD;
BEGIN
    -- Remove os telefones de cada funcionário da empresa
    FOR employee IN 
        SELECT codigo FROM funcionario WHERE cnpj_empresa = p_cnpj
    LOOP
        DELETE FROM telefone_funcionario WHERE codigo_func = employee.codigo;
    END LOOP;
    
    DELETE FROM funcionario WHERE cnpj_empresa = p_cnpj; -- Remove os funcionários
    DELETE FROM veiculo WHERE cnpj_empresa = p_cnpj; -- Remove os veículos
    DELETE FROM empresa WHERE cnpj = p_cnpj; -- Remove a empresa
END;
$$