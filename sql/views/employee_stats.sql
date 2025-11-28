CREATE OR REPLACE VIEW employee_stats AS
SELECT
    eobc.cnpj,
    eobc.nome_fantasia,
    COUNT(eobc.nome) AS quant_funcionarios,
    SUM(CASE WHEN eobc.sexo = 'M' THEN 1. ELSE 0. END) / COUNT(eobc) AS proporcao_homens,
    SUM(CASE WHEN eobc.cargo = 'Motorista' THEN 1. ELSE 0. END) / COUNT(eobc) AS proporcao_motorista,
    SUM(CASE WHEN eobc.cargo = 'Cobrador' THEN 1. ELSE 0. END) / COUNT(eobc) AS proporcao_cobrador,
    SUM(CASE WHEN eobc.cargo = 'Fiscal' THEN 1. ELSE 0. END) / COUNT(eobc) AS proporcao_fiscal,
    AVG(idade_funcionario) AS idade_media
FROM employee_overview_by_company AS eobc
GROUP BY eobc.cnpj, eobc.nome_fantasia