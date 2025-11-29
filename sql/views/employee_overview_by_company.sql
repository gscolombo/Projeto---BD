CREATE OR REPLACE VIEW employee_overview_by_company AS
SELECT
    e.cnpj,
    e.razao_social,
    e.nome_fantasia,
    f.nome,
    f.sexo,
    f.cargo,
    EXTRACT(years from AGE(f.data_nascimento)) AS idade_funcionario
FROM empresa AS e
JOIN funcionario AS f ON f.cnpj_empresa = e.cnpj
