CREATE OR REPLACE VIEW vehicle_overview_by_company AS
SELECT
    e.cnpj,
    e.razao_social,
    e.nome_fantasia,
    v.placa,
    v.km,
    v.ano_fabricacao,
    v.modelo,
    v.categoria
FROM empresa AS e
JOIN (
    SELECT
        v.cnpj_empresa,
        v.placa,
        v.km,
        v.ano_fabricacao,
        mo.nome AS modelo,
        c.nome AS categoria
    FROM veiculo AS v
    JOIN modelo AS mo ON mo.codigo = v.codigo_modelo
    JOIN categoria AS c ON c.codigo = mo.codigo_categoria
) AS v ON v.cnpj_empresa = e.cnpj
