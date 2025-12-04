CREATE OR REPLACE VIEW local_overview AS
SELECT 
    l.nome,
    l.lat,
    l.lng,
    a.nome_arquivo,
    a.tipo,
    a.tamanho,
    a.conteudo  -- BYTEA
FROM local l
LEFT JOIN local_arquivo a
       ON (l.lat, l.lng) = (a.local_lat, a.local_lng);
