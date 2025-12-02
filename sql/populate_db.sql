-- Inserindo locais no Distrito Federal
<<<<<<< HEAD
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
=======
INSERT INTO Local (lat, lng, nome, descricao) VALUES
(-15.7941, -47.8825, 'Rodoviária do Plano Piloto', 'Principal terminal de ônibus de Brasília'),
(-15.8336, -47.8346, 'Estação do Metrô Asa Sul', 'Estação de metrô na Asa Sul'),
(-15.7797, -47.9297, 'Praça do Relógio - Taguatinga', 'Praça central de Taguatinga'),
(-15.8404, -47.9462, 'Terminal de Ônibus de Ceilândia', 'Maior terminal de ônibus do DF'),
(-15.7565, -47.8695, 'Setor Comercial Sul', 'Área comercial da Asa Sul'),
(-15.7996, -47.8643, 'Setor Hoteleiro Norte', 'Área de hotéis na Asa Norte'),
(-15.7677, -47.8823, 'Conjunto Nacional', 'Shopping center na Asa Sul'),
(-15.8234, -47.9215, 'Feira dos Importados', 'Centro de compras em Taguatinga'),
(-15.8556, -47.9601, 'Centro Metropolitano - Ceilândia', 'Área central de Ceilândia'),
(-15.8787, -47.8376, 'Park Shopping', 'Shopping center em Águas Claras'),
(-15.7289, -47.9012, 'Estádio Mané Garrincha', 'Estádio nacional de Brasília'),
(-15.7839, -47.8992, 'Parque da Cidade', 'Maior parque urbano da América Latina'),
(-15.8012, -47.8943, 'Shopping Brasília', 'Shopping center no Plano Piloto'),
(-15.8456, -47.9123, 'Terminal de Samambaia', 'Terminal de ônibus de Samambaia'),
(-15.8923, -47.9789, 'Terminal de Sol Nascente', 'Terminal de ônibus em Ceilândia'),
(-15.7589, -47.9234, 'Terminal de Águas Claras', 'Terminal de ônibus e metrô'),
(-15.8123, -47.8765, 'Hospital Regional da Asa Norte', 'Hospital público de referência'),
(-16.0197, -48.0673, 'Terminal de Ônibus do Gama', 'Terminal rodoviário do Gama'),
(-15.6144, -47.6667, 'Terminal de Planaltina', 'Terminal de ônibus de Planaltina'),
(-16.0056, -47.9856, 'Terminal de Santa Maria', 'Terminal rodoviário de Santa Maria'),
(-15.6494, -47.7917, 'Terminal de Sobradinho', 'Terminal de ônibus de Sobradinho');

-- Inserindo empresas de transporte do DF
INSERT INTO Empresa (cnpj, razao_social, nome_fantasia, lat_local, lng_local) VALUES
('00111222000101', 'Viação Expresso Brasília Ltda', 'Expresso Brasília', -15.7941, -47.8825),
('00111222000102', 'Transporte Coletivo Taguatinga S/A', 'Taguatrans', -15.7797, -47.9297),
('00111222000103', 'Consórcio de Transporte Ceilândia', 'TransCeilândia', -15.8404, -47.9462),
('00111222000104', 'Transporte Coletivo Gama Ltda', 'TransGama', -16.0197, -48.0673),
('00111222000105', 'Viação Planaltina S/A', 'Planaltina Transportes', -15.6144, -47.6667),
('00111222000106', 'Consórcio Santa Maria', 'TransSanta', -16.0056, -47.9856),
('00111222000107', 'Auto Viação Sobradinho', 'Sobradinho Ônibus', -15.6494, -47.7917);

-- Inserindo funcionários
INSERT INTO Funcionario (cnpj_empresa, nome, sexo, cargo, data_nascimento, data_contratacao, data_demissao) VALUES
('00111222000101', 'João Silva Santos', 'M', 'Motorista', '1985-03-15', '2020-01-10', NULL),
('00111222000101', 'Maria Oliveira Costa', 'F', 'Cobrador', '1990-07-22', '2021-03-15', NULL),
('00111222000101', 'Carlos Eduardo Pereira', 'M', 'Fiscal', '1982-11-30', '2019-05-20', NULL),
('00111222000102', 'Ana Paula Rodrigues', 'F', 'Motorista', '1988-05-10', '2022-02-01', NULL),
('00111222000102', 'Pedro Henrique Alves', 'M', 'Cobrador', '1995-09-18', '2023-01-15', NULL),
('00111222000103', 'Fernanda Lima Souza', 'F', 'Motorista', '1980-12-05', '2018-08-12', NULL),
('00111222000103', 'Ricardo Martins Ferreira', 'M', 'Cobrador', '1992-04-25', '2022-11-30', NULL),
('00111222000101', 'Roberto Almeida Santos', 'M', 'Motorista', '1978-09-12', '2015-03-20', NULL),
('00111222000101', 'Juliana Mendes Costa', 'F', 'Cobrador', '1993-04-18', '2022-06-10', NULL),
('00111222000101', 'Felipe Rocha Lima', 'M', 'Motorista', '1987-11-25', '2019-08-15', '2024-01-15'),
('00111222000102', 'Camila Torres Silva', 'F', 'Motorista', '1991-02-28', '2021-09-05', NULL),
('00111222000102', 'Rafael Costa Oliveira', 'M', 'Motorista', '1983-07-14', '2017-11-30', NULL),
('00111222000103', 'Patrícia Nunes Alves', 'F', 'Cobrador', '1975-12-08', '2010-05-22', NULL),
('00111222000103', 'Bruno Carvalho Souza', 'M', 'Motorista', '1994-08-03', '2023-02-14', NULL),
('00111222000104', 'Luciana Ferreira Rodrigues', 'F', 'Motorista', '1986-06-19', '2018-04-18', NULL),
('00111222000104', 'Daniel Martins Costa', 'M', 'Motorista', '1989-03-22', '2020-07-25', NULL),
('00111222000105', 'Sandra Oliveira Lima', 'F', 'Cobrador', '1981-01-30', '2016-12-10', NULL),
('00111222000105', 'Marcos Antonio Santos', 'M', 'Motorista', '1990-09-15', '2021-10-20', NULL),
('00111222000106', 'Gabriela Silva Pereira', 'F', 'Fiscal', '1979-04-05', '2014-08-30', NULL),
('00111222000106', 'Thiago Rocha Almeida', 'M', 'Motorista', '1992-07-12', '2022-03-08', NULL),
('00111222000107', 'Amanda Costa Nunes', 'F', 'Cobrador', '1984-11-28', '2019-01-15', NULL),
('00111222000107', 'Leonardo Souza Mendes', 'M', 'Motorista', '1988-05-17', '2020-09-22', NULL),
('00111222000101', 'Paulo Henrique Dias', 'M', 'Fiscal', '1980-03-14', '2015-07-18', NULL),
('00111222000102', 'Cristina Alves Monteiro', 'F', 'Fiscal', '1977-08-21', '2013-11-05', NULL),
('00111222000103', 'Rodrigo Pereira Castro', 'M', 'Cobrador', '1982-12-03', '2018-02-28', NULL),
('00111222000104', 'Vanessa Santos Rocha', 'F', 'Fiscal', '1985-06-09', '2019-04-12', NULL),
('00111222000105', 'André Luiz Fernandes', 'M', 'Cobrador', '1976-10-27', '2012-09-15', NULL);


-- Inserindo telefones dos funcionários
INSERT INTO Telefone_Funcionario (codigo_func, telefone) VALUES
(1, '61999991111'),
(1, '6133334444'),
(2, '61988882222'),
(3, '61977773333'),
(4, '61966664444'),
(5, '61955552222'),
(6, '61944441243'),
(7, '61933330000'),
(8, '61922221111'),
(9, '61922223333'),
(10, '61922224444'),
(11, '61922225555'),
(12, '61922226666'),
(13, '61922227777'),
(14, '61922228888'),
(15, '61922229999'),
(16, '61922220000'),
(17, '61933331111'),
(18, '61933332222'),
(19, '61933333333'),
(20, '61933334444'),
(21, '61933335555'),
(22, '61933336666'),
(23, '61933337777'),
(24, '61933338888'),
(25, '61933339999'),
(26, '61933330010'),
(27, '61944441111');

-- Inserindo motoristas (apenas funcionários com cargo 'Motorista')
INSERT INTO Motorista (cnh, codigo_funcionario, status_cnh, data_validade_cnh) VALUES
('123456789', 1, 'Válida', '2025-08-31'),
('987654321', 4, 'Válida', '2024-12-31'),
('456789123', 6, 'Válida', '2026-03-31'),
('111222333', 8, 'Válida', '2025-11-30'),
('222333444', 11, 'Válida', '2024-09-30'),
('333444555', 12, 'Suspensa', '2025-06-30'),
('444555666', 14, 'Válida', '2026-01-31'),
('555666777', 16, 'Válida', '2024-12-31'),
('666777888', 18, 'Vencida', '2023-10-31'),
('777888999', 20, 'Válida', '2025-07-31'),
('888999000', 22, 'Válida', '2026-03-31');

-- Inserindo categorias de veículos
INSERT INTO Categoria (codigo, nome, descricao) VALUES
(1, 'Ônibus Urbano', 'Ônibus para transporte urbano'),
(2, 'Ônibus Articulado', 'Ônibus articulado para corredores'),
(3, 'Micro-ônibus', 'Veículos menores para áreas específicas'),
(4, 'Ônibus Biarticulado', 'Ônibus com dois articulados para alta capacidade'),
(5, 'Ônibus Elétrico', 'Veículo elétrico para transporte sustentável'),
(6, 'Van Executiva', 'Vans para transporte executivo');

-- Inserindo modelos de veículos
INSERT INTO Modelo (codigo, codigo_categoria, nome) VALUES
(1, 1, 'Marcopolo Torino'),
(2, 1, 'Mercedes-Benz O-500'),
(3, 2, 'Marcopolo Allegro'),
(4, 3, 'Volkswagen 15-210'),
(5, 1, 'Comil Svelto'),
(6, 4, 'Marcopolo Torino G7 Biarticulado'),
(7, 2, 'Volvo B340M Articulado'),
(8, 5, 'BYD D9W Elétrico'),
(9, 6, 'Mercedes-Benz Sprinter'),
(10, 1, 'Comil Campione 2023');

-- Inserindo veículos
INSERT INTO Veiculo (placa, cnpj_empresa, codigo_modelo, km, ano_fabricacao) VALUES
('DF1A234', '00111222000101', 1, 125000, 2020),
('DF2B345', '00111222000101', 2, 89000, 2021),
('DF3C456', '00111222000102', 3, 156000, 2019),
('DF4D567', '00111222000102', 4, 45000, 2022),
('DF5E678', '00111222000103', 5, 178000, 2018),
('DF6F789', '00111222000101', 6, 234000, 2017),
('DF7G890', '00111222000102', 7, 187000, 2019),
('DF8H901', '00111222000103', 8, 45000, 2023),
('DF9I012', '00111222000104', 9, 89000, 2021),
('DF0J123', '00111222000105', 10, 123000, 2020),
('DF1K234', '00111222000106', 1, 167000, 2018),
('DF2L345', '00111222000107', 2, 203000, 2016),
('DF3M456', '00111222000101', 3, 145000, 2019),
('DF4N567', '00111222000102', 4, 78000, 2022),
('DF5O678', '00111222000103', 5, 198000, 2017),
('DF6P789', '00111222000104', 6, 112000, 2020),
('DF7Q890', '00111222000105', 7, 156000, 2018),
('DF8R901', '00111222000106', 8, 34000, 2023),
('DF9S012', '00111222000107', 9, 67000, 2021),
('DF0T123', '00111222000101', 10, 134000, 2019);

-- Inserindo manutenções
INSERT INTO Manutencao (placa_veiculo, data_hora) VALUES
('DF1A234', '2024-01-15 08:30:00'),
('DF2B345', '2024-01-20 14:15:00'),
('DF3C456', '2024-02-01 10:00:00'),
('DF4D567', '2024-02-10 16:45:00'),
('DF5E678', '2024-02-15 09:20:00'),
('DF6F789', '2024-01-05 09:00:00'),
('DF7G890', '2024-01-08 14:30:00'),
('DF8H901', '2024-01-12 11:15:00'),
('DF9I012', '2024-01-18 16:45:00'),
('DF0J123', '2024-01-22 08:20:00'),
('DF1K234', '2024-01-25 13:10:00'),
('DF2L345', '2024-01-30 10:30:00'),
('DF3M456', '2024-02-02 15:20:00'),
('DF4N567', '2024-02-08 12:00:00'),
('DF5O678', '2024-02-12 09:45:00'),
('DF6P789', '2024-02-15 14:15:00'),
('DF7Q890', '2024-02-20 11:30:00'),
('DF8R901', '2024-02-25 16:00:00'),
('DF9S012', '2024-03-01 08:45:00'),
('DF0T123', '2024-03-05 13:50:00'),
('DF1A234', '2024-03-10 10:10:00'),
('DF2B345', '2024-03-12 15:30:00'),
('DF3C456', '2024-03-15 12:20:00'),
('DF4D567', '2024-03-18 09:15:00'),
('DF5E678', '2024-03-20 14:40:00');

-- Inserindo serviços de manutenção
INSERT INTO Servico (descricao, valor) VALUES
('Troca de óleo e filtro', 350.00),
('Alinhamento e balanceamento', 280.00),
('Troca de pastilhas de freio', 420.00),
('Revisão geral preventiva', 850.00),
('Reparo no sistema elétrico', 600.00),
('Troca de pneus', 1200.00),
('Reparo na transmissão', 2500.00),
('Substituição de para-brisa', 800.00),
('Reparo no sistema de ar condicionado', 950.00),
('Troca de bateria', 450.00),
('Revisão do sistema de freios', 680.00),
('Alinhamento 3D', 320.00),
('Balanceamento completo', 180.00),
('Troca de correia dentada', 520.00),
('Limpeza de bicos injetores', 380.00);

-- Inserindo serviços realizados nas manutenções
INSERT INTO Manutencao_Servico (id_manutencao, codigo_servico) VALUES
(1, 1), (1, 4), (2, 2), (3, 3), (4, 1), (5, 5),
(6, 6), (6, 2), (6, 13), (7, 7), (7, 4),(8, 8), 
(8, 1), (9, 9), (9, 5), (10, 10), (10, 4), (11, 11), 
(11, 3), (12, 12), (12, 13), (13, 14), (13, 1), (14, 15), 
(14, 4), (15, 6), (15, 2), (16, 7), (16, 11), (17, 8), 
(17, 1), (18, 9), (18, 5), (19, 10), (19, 4), (20, 11), 
(20, 3), (21, 12), (21, 13), (22, 14), (22, 1), (23, 15),
(23, 4), (24, 6), (24, 2), (25, 7), (25, 11);

-- Inserindo ocorrências
INSERT INTO Ocorrencia (placa_veiculo, data_hora, lat_local, lng_local) VALUES
('DF1A234', '2024-01-10 07:30:00', -15.7941, -47.8825),
('DF3C456', '2024-01-25 16:45:00', -15.7797, -47.9297),
('DF5E678', '2024-02-05 12:15:00', -15.8404, -47.9462),
('DF6F789', '2024-01-08 08:15:00', -15.7996, -47.8643),
('DF7G890', '2024-01-12 17:30:00', -15.7677, -47.8823),
('DF8H901', '2024-01-15 12:45:00', -15.8234, -47.9215),
('DF9I012', '2024-01-20 14:20:00', -15.8556, -47.9601),
('DF0J123', '2024-01-25 09:10:00', -15.8787, -47.8376),
('DF1K234', '2024-02-01 16:50:00', -15.7289, -47.9012),
('DF2L345', '2024-02-05 07:25:00', -15.7839, -47.8992),
('DF3M456', '2024-02-10 13:15:00', -15.8012, -47.8943),
('DF4N567', '2024-02-14 18:05:00', -15.8456, -47.9123),
('DF5O678', '2024-02-18 10:40:00', -15.8923, -47.9789),
('DF6P789', '2024-02-22 15:55:00', -15.7589, -47.9234),
('DF7Q890', '2024-02-26 11:30:00', -15.8123, -47.8765),
('DF1A234', '2024-01-20 08:30:00', -15.7677, -47.8823),
('DF1A234', '2024-02-05 14:15:00', -15.8012, -47.8943),
('DF1A234', '2024-02-28 17:45:00', -15.7941, -47.8825),
('DF2B345', '2024-01-18 11:20:00', -15.7797, -47.9297),
('DF2B345', '2024-02-12 09:10:00', -15.8234, -47.9215),
('DF2B345', '2024-03-08 16:30:00', -15.8556, -47.9601),
('DF3C456', '2024-01-22 07:45:00', -15.8787, -47.8376),
('DF3C456', '2024-02-15 13:25:00', -15.7289, -47.9012),
('DF3C456', '2024-03-12 18:15:00', -15.7839, -47.8992),
('DF4D567', '2024-01-25 10:05:00', -15.8012, -47.8943),
('DF4D567', '2024-02-18 15:40:00', -15.8456, -47.9123),
('DF4D567', '2024-03-15 12:20:00', -15.8923, -47.9789),
('DF5E678', '2024-01-28 06:50:00', -15.7589, -47.9234),
('DF5E678', '2024-02-22 14:55:00', -15.8123, -47.8765),
('DF5E678', '2024-03-18 19:30:00', -15.7996, -47.8643),
('DF6F789', '2024-01-30 09:15:00', -15.7677, -47.8823),
('DF6F789', '2024-02-25 16:10:00', -15.8234, -47.9215),
('DF6F789', '2024-03-20 07:25:00', -15.8556, -47.9601),
('DF7G890', '2024-02-02 08:40:00', -15.8787, -47.8376),
('DF7G890', '2024-02-27 12:35:00', -15.7289, -47.9012),
('DF7G890', '2024-03-22 17:50:00', -15.7839, -47.8992),
('DF8H901', '2024-02-07 11:30:00', -15.8012, -47.8943),
('DF8H901', '2024-03-03 15:20:00', -15.8456, -47.9123),
('DF8H901', '2024-03-25 10:45:00', -15.8923, -47.9789),
('DF9I012', '2024-02-09 13:55:00', -15.7589, -47.9234),
('DF9I012', '2024-03-05 18:05:00', -15.8123, -47.8765),
('DF9I012', '2024-03-28 14:15:00', -15.7996, -47.8643),
('DF0J123', '2024-02-14 07:10:00', -15.7677, -47.8823),
('DF0J123', '2024-03-07 09:40:00', -15.8234, -47.9215),
('DF0J123', '2024-03-30 16:25:00', -15.8556, -47.9601),
('DF1K234', '2024-01-17 14:50:00', -16.0197, -48.0673);

-- Inserindo acidentes
INSERT INTO Acidente (id_ocorrencia, descricao, gravidade, numero_feridos, numero_mortos) VALUES
(1, 'Colisão traseira em congestionamento', 'Leve', 0, 0),
(2, 'Atropelamento de pedestre', 'Grave', 1, 0),
(4, 'Colisão lateral no cruzamento', 'Moderado', 2, 0),
(5, 'Capotamento na via expressa', 'Grave', 3, 1),
(6, 'Tombamento em curva acentuada', 'Grave', 4, 2),
(7, 'Colisão frontal com outro veículo', 'Grave', 3, 1),
(8, 'Atropelamento em faixa de pedestre', 'Leve', 1, 0),
(9, 'Colisão traseira em múltiplos veículos', 'Moderado', 3, 0),
(10, 'Saída de pista em dia chuvoso', 'Moderado', 2, 0),
(16, 'Colisão lateral durante mudança de faixa', 'Leve', 0, 0),
(17, 'Batida traseira em semáforo', 'Leve', 1, 0),
(18, 'Colisão com poste ao desviar de pedestre', 'Moderado', 0, 0),
(19, 'Atropelamento de animal na pista', 'Leve', 0, 0),
(20, 'Colisão frontal em cruzamento', 'Grave', 2, 0),
(21, 'Capotamento em via de acesso', 'Grave', 3, 1),
(22, 'Colisão múltipla em congestionamento', 'Moderado', 2, 0),
(23, 'Saída de pista em curva', 'Moderado', 1, 0),
(24, 'Colisão com muro de contenção', 'Leve', 0, 0),
(25, 'Atropelamento em faixa não sinalizada', 'Grave', 1, 0);

-- Inserindo avarias
INSERT INTO Avaria (id_ocorrencia, descricao, nivel_dano, total) VALUES
(3, 'Pane elétrica no sistema de ignição', 'Moderado', FALSE),
(11, 'Pane no motor por superaquecimento', 'Grave', TRUE),
(12, 'Ruptura do sistema de direção', 'Grave', TRUE),
(13, 'Problema no sistema de transmissão', 'Moderado', FALSE),
(14, 'Danos na carroceria por queda de árvore', 'Leve', FALSE),
(15, 'Sistema elétrico comprometido por curto', 'Moderado', FALSE),
(26, 'Superaquecimento do motor em subida', 'Moderado', FALSE),
(27, 'Problema no sistema de freios', 'Grave', TRUE),
(28, 'Pane elétrica generalizada', 'Moderado', FALSE),
(29, 'Ruptura do radiador', 'Leve', FALSE),
(30, 'Problema na transmissão automática', 'Grave', TRUE),
(31, 'Danos na suspensão dianteira', 'Moderado', FALSE),
(32, 'Vazamento de óleo no motor', 'Leve', FALSE),
(33, 'Problema no sistema de ar condicionado', 'Leve', FALSE),
(34, 'Quebra do eixo traseiro', 'Grave', TRUE),
(35, 'Danos no sistema de direção hidráulica', 'Moderado', FALSE),
(36, 'Superaquecimento em dia muito quente', 'Leve', FALSE),
(37, 'Problema no sistema de injeção eletrônica', 'Moderado', FALSE),
(38, 'Rompimento da correia do alternador', 'Leve', FALSE),
(39, 'Vazamento no sistema de combustível', 'Grave', TRUE),
(40, 'Danos no sistema de escapamento', 'Leve', FALSE),
(41, 'Problema no diferencial', 'Grave', TRUE),
(42, 'Falha no sistema de embreagem', 'Moderado', FALSE),
(43, 'Vazamento no sistema hidráulico', 'Leve', FALSE),
(44, 'Problema no turbo (veículos a diesel)', 'Moderado', FALSE),
(45, 'Danos no sistema de refrigeração', 'Leve', FALSE),
(46, 'Estouro de pneu', 'Moderado', TRUE);

-- Inserindo linhas de ônibus do DF
INSERT INTO Linha (cnpj_empresa, codigo) VALUES
('00111222000101', '001'),
('00111222000101', '002'),
('00111222000102', '101'),
('00111222000103', '201'),
('00111222000103', '202'),
('00111222000101', '003'),
('00111222000101', '004'),
('00111222000102', '102'),
('00111222000102', '103'),
('00111222000103', '203'),
('00111222000103', '204'),
('00111222000104', '301'),
('00111222000104', '302'),
('00111222000105', '401'),
('00111222000105', '402'),
('00111222000106', '501'),
('00111222000106', '502'),
('00111222000107', '601'),
('00111222000107', '602');

-- Inserindo itinerários das linhas
INSERT INTO Itinerario (codigo_linha, lat_local, lng_local, numero) VALUES
('001', -15.7941, -47.8825, 1),
('001', -15.8336, -47.8346, 2),
('001', -15.7565, -47.8695, 3),
('002', -15.7941, -47.8825, 1),
('002', -15.7797, -47.9297, 2),
('101', -15.7797, -47.9297, 1),
('101', -15.8404, -47.9462, 2),
('201', -15.8404, -47.9462, 1),
('201', -15.7941, -47.8825, 2),
('003', -15.7941, -47.8825, 1),
('003', -15.7996, -47.8643, 2),
('003', -15.7677, -47.8823, 3),
('004', -15.7941, -47.8825, 1),
('004', -15.7839, -47.8992, 2),
('004', -15.8012, -47.8943, 3),
('102', -15.7797, -47.9297, 1),
('102', -15.8234, -47.9215, 2),
('102', -15.8556, -47.9601, 3),
('103', -15.7797, -47.9297, 1),
('103', -15.8787, -47.8376, 2),
('203', -15.8404, -47.9462, 1),
('203', -15.8923, -47.9789, 2),
('203', -15.8556, -47.9601, 3),
('204', -15.8404, -47.9462, 1),
('204', -15.7589, -47.9234, 2),
('301', -16.0197, -48.0673, 1),
('301', -15.8556, -47.9601, 2),
('302', -16.0197, -48.0673, 1),
('302', -15.8923, -47.9789, 2),
('401', -15.6144, -47.6667, 1),
('401', -15.7941, -47.8825, 2),
('402', -15.6144, -47.6667, 1),
('402', -15.7839, -47.8992, 2),
('501', -16.0056, -47.9856, 1),
('501', -16.0197, -48.0673, 2),
('502', -16.0056, -47.9856, 1),
('502', -15.8556, -47.9601, 2),
('601', -15.6494, -47.7917, 1),
('601', -15.7941, -47.8825, 2),
('602', -15.6494, -47.7917, 1),
('602', -15.7839, -47.8992, 2);

-- Inserindo viagens (usando apenas funcionários com cargos corretos devido aos triggers)
INSERT INTO Viagem (codigo_linha, codigo_cobrador, codigo_motorista, placa_veiculo, data, hora_partida, hora_chegada) VALUES
('001', 2, 1, 'DF1A234', '2024-03-01', '2024-03-01 06:00:00', '2024-03-01 07:30:00'),
('002', 2, 1, 'DF2B345', '2024-03-01', '2024-03-01 08:00:00', '2024-03-01 09:45:00'),
('101', 5, 4, 'DF3C456', '2024-03-01', '2024-03-01 07:15:00', '2024-03-01 08:30:00'),
('201', 7, 6, 'DF5E678', '2024-03-01', '2024-03-01 05:45:00', '2024-03-01 07:15:00'),
('001', 2, 1, 'DF1A234', '2024-03-02', '2024-03-02 06:00:00', '2024-03-02 07:30:00'),
('001', 2, 1, 'DF1A234', '2024-03-02', '2024-03-02 08:30:00', '2024-03-02 10:00:00'),
('001', 2, 1, 'DF1A234', '2024-03-02', '2024-03-02 11:00:00', '2024-03-02 12:30:00'),
('001', 2, 1, 'DF1A234', '2024-03-02', '2024-03-02 14:00:00', '2024-03-02 15:30:00'),
('001', 2, 1, 'DF1A234', '2024-03-02', '2024-03-02 16:30:00', '2024-03-02 18:00:00'),
('002', 2, 1, 'DF2B345', '2024-03-03', '2024-03-03 05:45:00', '2024-03-03 07:15:00'),
('002', 2, 1, 'DF2B345', '2024-03-03', '2024-03-03 08:15:00', '2024-03-03 09:45:00'),
('002', 2, 1, 'DF2B345', '2024-03-03', '2024-03-03 10:45:00', '2024-03-03 12:15:00'),
('101', 5, 4, 'DF3C456', '2024-03-04', '2024-03-04 06:30:00', '2024-03-04 08:00:00'),
('101', 5, 4, 'DF3C456', '2024-03-04', '2024-03-04 09:00:00', '2024-03-04 10:30:00'),
('101', 5, 4, 'DF3C456', '2024-03-04', '2024-03-04 11:30:00', '2024-03-04 13:00:00'),
('201', 7, 6, 'DF5E678', '2024-03-05', '2024-03-05 05:30:00', '2024-03-05 07:00:00'),
('201', 7, 6, 'DF5E678', '2024-03-05', '2024-03-05 08:00:00', '2024-03-05 09:30:00'),
('201', 7, 6, 'DF5E678', '2024-03-05', '2024-03-05 10:30:00', '2024-03-05 12:00:00'),
('003', 9, 8, 'DF6F789', '2024-03-06', '2024-03-06 06:15:00', '2024-03-06 07:45:00'),
('004', 9, 8, 'DF7G890', '2024-03-06', '2024-03-06 08:45:00', '2024-03-06 10:15:00'),
('102', 13, 11, 'DF8H901', '2024-03-07', '2024-03-07 07:00:00', '2024-03-07 08:30:00'),
('103', 13, 11, 'DF9I012', '2024-03-07', '2024-03-07 09:30:00', '2024-03-07 11:00:00'),
('203', 17, 14, 'DF0J123', '2024-03-08', '2024-03-08 06:45:00', '2024-03-08 08:15:00'),
('204', 17, 14, 'DF1K234', '2024-03-08', '2024-03-08 09:15:00', '2024-03-08 10:45:00'),
('301', 21, 16, 'DF2L345', '2024-03-09', '2024-03-09 05:30:00', '2024-03-09 07:00:00'),
('302', 21, 16, 'DF3M456', '2024-03-09', '2024-03-09 08:00:00', '2024-03-09 09:30:00'),
('401', 25, 18, 'DF4N567', '2024-03-10', '2024-03-10 06:00:00', '2024-03-10 07:30:00'),
('402', 25, 18, 'DF5O678', '2024-03-10', '2024-03-10 08:30:00', '2024-03-10 10:00:00'),
('501', 27, 20, 'DF6P789', '2024-03-11', '2024-03-11 05:45:00', '2024-03-11 07:15:00'),
('502', 27, 20, 'DF7Q890', '2024-03-11', '2024-03-11 08:15:00', '2024-03-11 09:45:00'),
('601', 27, 22, 'DF8R901', '2024-03-12', '2024-03-12 06:30:00', '2024-03-12 08:00:00'),
('602', 27, 22, 'DF9S012', '2024-03-12', '2024-03-12 09:00:00', '2024-03-12 10:30:00'),
('001', 2, 1, 'DF1A234', '2024-03-13', '2024-03-13 06:00:00', '2024-03-13 07:25:00'),
('001', 2, 1, 'DF1A234', '2024-03-13', '2024-03-13 12:00:00', '2024-03-13 13:40:00'),
('001', 2, 1, 'DF1A234', '2024-03-13', '2024-03-13 17:30:00', '2024-03-13 19:15:00'),
('002', 2, 1, 'DF2B345', '2024-03-14', '2024-03-14 05:45:00', '2024-03-14 07:10:00'),
('002', 2, 1, 'DF2B345', '2024-03-14', '2024-03-14 11:45:00', '2024-03-14 13:20:00'),
('002', 2, 1, 'DF2B345', '2024-03-14', '2024-03-14 16:45:00', '2024-03-14 18:30:00'),
('101', 5, 4, 'DF3C456', '2024-03-15', '2024-03-15 06:30:00', '2024-03-15 08:20:00'),
('101', 5, 4, 'DF3C456', '2024-03-15', '2024-03-15 09:00:00', '2024-03-15 10:50:00'),
('201', 7, 6, 'DF5E678', '2024-03-16', '2024-03-16 05:30:00', '2024-03-16 07:25:00'),
('201', 7, 6, 'DF5E678', '2024-03-16', '2024-03-16 08:00:00', '2024-03-16 09:55:00'),
('003', 9, 8, 'DF6F789', '2024-03-17', '2024-03-17 06:15:00', '2024-03-17 07:40:00'),
('004', 9, 8, 'DF7G890', '2024-03-17', '2024-03-17 08:45:00', '2024-03-17 10:10:00'),
('102', 13, 11, 'DF8H901', '2024-03-18', '2024-03-18 07:00:00', '2024-03-18 08:25:00'),
('103', 13, 11, 'DF9I012', '2024-03-18', '2024-03-18 09:30:00', '2024-03-18 10:55:00');
>>>>>>> 558a1e925ffddc0820452456e21d824d5794ae43
