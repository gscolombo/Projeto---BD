-- Inserindo locais no Distrito Federal
INSERT INTO Local (lat, lng, nome, descricao)
VALUES (
        -15.7941,
        -47.8825,
        'Rodoviaria do Plano Piloto',
        'Principal terminal de onibus de Brasilia'
    ),
    (
        -15.8336,
        -47.8346,
        'Estacao do Metro Asa Sul',
        'Estacao de metro na Asa Sul'
    ),
    (
        -15.7797,
        -47.9297,
        'Praca do Relogio - Taguatinga',
        'Praca central de Taguatinga'
    ),
    (
        -15.8404,
        -47.9462,
        'Terminal de Onibus de Ceilandia',
        'Maior terminal de onibus do DF'
    ),
    (
        -15.7565,
        -47.8695,
        'Setor Comercial Sul',
        'Area comercial da Asa Sul'
    );
-- Inserindo empresas
INSERT INTO Empresa (
        cnpj,
        razao_social,
        nome_fantasia,
        lat_local,
        lng_local
    )
VALUES (
        '00111222000101',
        'Viacao Expresso Brasilia Ltda',
        'Expresso Brasilia',
        -15.7941,
        -47.8825
    ),
    (
        '00111222000102',
        'Transporte Coletivo Taguatinga SA',
        'Taguatrans',
        -15.7797,
        -47.9297
    ),
    (
        '00111222000103',
        'Consorcio de Transporte Ceilandia',
        'TransCeilandia',
        -15.8404,
        -47.9462
    );
-- Inserindo funcionarios
INSERT INTO Funcionario (
        cnpj_empresa,
        nome,
        sexo,
        cargo,
        data_nascimento,
        data_contratacao
    )
VALUES (
        '00111222000101',
        'Joao Silva Santos',
        'M',
        'Motorista',
        '1985-03-15',
        '2020-01-10'
    ),
    (
        '00111222000101',
        'Maria Oliveira Costa',
        'F',
        'Cobrador',
        '1990-07-22',
        '2021-03-15'
    ),
    (
        '00111222000101',
        'Carlos Eduardo Pereira',
        'M',
        'Fiscal',
        '1982-11-30',
        '2019-05-20'
    ),
    (
        '00111222000102',
        'Ana Paula Rodrigues',
        'F',
        'Motorista',
        '1988-05-10',
        '2022-02-01'
    ),
    (
        '00111222000102',
        'Pedro Henrique Alves',
        'M',
        'Cobrador',
        '1995-09-18',
        '2023-01-15'
    ),
    (
        '00111222000103',
        'Fernanda Lima Souza',
        'F',
        'Motorista',
        '1980-12-05',
        '2018-08-12'
    ),
    (
        '00111222000103',
        'Ricardo Martins Ferreira',
        'M',
        'Cobrador',
        '1992-04-25',
        '2022-11-30'
    );
-- Telefones
INSERT INTO Telefone_Funcionario (codigo_func, telefone)
VALUES (1, '61999991111'),
    (1, '6133334444'),
    (2, '61988882222'),
    (3, '61977773333'),
    (4, '61966664444'),
    (5, '61955552222'),
    (6, '61944441111'),
    (7, '61933330000');
-- Motoristas
INSERT INTO Motorista (
        cnh,
        codigo_funcionario,
        status_cnh,
        data_validade_cnh
    )
VALUES ('123456789', 1, 'Válida', '2025-08-31'),
    ('987654321', 4, 'Válida', '2024-12-31'),
    ('456789123', 6, 'Válida', '2026-03-31');
-- Categorias
INSERT INTO Categoria (codigo, nome, descricao)
VALUES (
        1,
        'Onibus Urbano',
        'Onibus para transporte urbano'
    ),
    (
        2,
        'Onibus Articulado',
        'Onibus articulado para corredores'
    ),
    (
        3,
        'Micro-onibus',
        'Veiculos menores para areas especificas'
    );
-- Modelos
INSERT INTO Modelo (codigo, codigo_categoria, nome)
VALUES (1, 1, 'Marcopolo Torino'),
    (2, 1, 'Mercedes-Benz O-500'),
    (3, 2, 'Marcopolo Allegro'),
    (4, 3, 'Volkswagen 15-210'),
    (5, 1, 'Comil Svelto');
-- Veiculos
INSERT INTO Veiculo (
        placa,
        cnpj_empresa,
        codigo_modelo,
        km,
        ano_fabricacao
    )
VALUES ('DF1A234', '00111222000101', 1, 125000, 2020),
    ('DF2B345', '00111222000101', 2, 89000, 2021),
    ('DF3C456', '00111222000102', 3, 156000, 2019),
    ('DF4D567', '00111222000102', 4, 45000, 2022),
    ('DF5E678', '00111222000103', 5, 178000, 2018);
-- Manutencoes
INSERT INTO Manutencao (placa_veiculo, data_hora)
VALUES ('DF1A234', '2024-01-15 08:30:00'),
    ('DF2B345', '2024-01-20 14:15:00'),
    ('DF3C456', '2024-02-01 10:00:00'),
    ('DF4D567', '2024-02-10 16:45:00'),
    ('DF5E678', '2024-02-15 09:20:00');
-- Servicos
INSERT INTO Servico (descricao, valor)
VALUES ('Troca de oleo e filtro', 350.00),
    ('Alinhamento e balanceamento', 280.00),
    ('Troca de pastilhas de freio', 420.00),
    ('Revisao geral preventiva', 850.00),
    ('Reparo no sistema eletrico', 600.00);
-- Manutencao_Servico
INSERT INTO Manutencao_Servico (id_manutencao, codigo_servico)
VALUES (1, 1),
    (1, 4),
    (2, 2),
    (3, 3),
    (4, 1),
    (5, 5);
-- Ocorrencias
INSERT INTO Ocorrencia (placa_veiculo, data_hora, lat_local, lng_local)
VALUES (
        'DF1A234',
        '2024-01-10 07:30:00',
        -15.7941,
        -47.8825
    ),
    (
        'DF3C456',
        '2024-01-25 16:45:00',
        -15.7797,
        -47.9297
    ),
    (
        'DF5E678',
        '2024-02-05 12:15:00',
        -15.8404,
        -47.9462
    );
-- Acidentes
INSERT INTO Acidente (
        id_ocorrencia,
        descricao,
        gravidade,
        numero_feridos,
        numero_mortos
    )
VALUES (
        1,
        'Colisao traseira em congestionamento',
        'Leve',
        0,
        0
    ),
    (2, 'Atropelamento de pedestre', 'Grave', 1, 0);
-- Avarias
INSERT INTO Avaria (id_ocorrencia, descricao, nivel_dano, total)
VALUES (
        3,
        'Pane eletrica no sistema de ignicao',
        'Moderado',
        FALSE
    );
-- Linhas
INSERT INTO Linha (cnpj_empresa, codigo)
VALUES ('00111222000101', '001'),
    ('00111222000101', '002'),
    ('00111222000102', '101'),
    ('00111222000103', '201'),
    ('00111222000103', '202');
-- Itinerarios
INSERT INTO Itinerario (codigo_linha, lat_local, lng_local, numero)
VALUES ('001', -15.7941, -47.8825, 1),
    ('001', -15.8336, -47.8346, 2),
    ('001', -15.7565, -47.8695, 3),
    ('002', -15.7941, -47.8825, 1),
    ('002', -15.7797, -47.9297, 2),
    ('101', -15.7797, -47.9297, 1),
    ('101', -15.8404, -47.9462, 2),
    ('201', -15.8404, -47.9462, 1),
    ('201', -15.7941, -47.8825, 2);
-- Viagens
INSERT INTO Viagem (
        codigo_linha,
        codigo_cobrador,
        codigo_motorista,
        placa_veiculo,
        data,
        hora_partida,
        hora_chegada
    )
VALUES (
        '001',
        2,
        1,
        'DF1A234',
        '2024-03-01',
        '2024-03-01 06:00:00',
        '2024-03-01 07:30:00'
    ),
    (
        '002',
        2,
        1,
        'DF2B345',
        '2024-03-01',
        '2024-03-01 08:00:00',
        '2024-03-01 09:45:00'
    ),
    (
        '101',
        5,
        4,
        'DF3C456',
        '2024-03-01',
        '2024-03-01 07:15:00',
        '2024-03-01 08:30:00'
    ),
    (
        '201',
        7,
        6,
        'DF5E678',
        '2024-03-01',
        '2024-03-01 05:45:00',
        '2024-03-01 07:15:00'
    );