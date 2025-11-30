CREATE OR REPLACE VIEW local_overview AS
SELECT 
    l.id_local,
    l.nome,
    l.lat,
    l.long,
    a.nome_arquivo,
    a.tipo,
    a.tamanho,
    a.conteudo  -- BYTEA
FROM local l
LEFT JOIN local_arquivo a
       ON l.id_local = a.id_local;
