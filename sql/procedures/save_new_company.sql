CREATE OR REPLACE PROCEDURE save_new_company (
    cnpj VARCHAR(14),
    razao_social VARCHAR,
    nome_fantasia VARCHAR,
    lat_local float,
    lng_local float,
    local_nome VARCHAR DEFAULT NULL,
    local_descricao VARCHAR DEFAULT NULL,
    employees JSONB DEFAULT '[]',
    vehicles JSONB DEFAULT '[]'
)
LANGUAGE plpgsql
AS $$
DECLARE
    location_exists BOOLEAN;
    new_employee_id INT;
    employee JSONB;
    vehicle JSONB;
BEGIN

    -- Checa se o local existe
    SELECT EXISTS(
        SELECT 1 FROM local WHERE lat = lat_local AND lng = lng_local
    ) INTO location_exists;

    -- Cria o local se não existir
    IF NOT location_exists THEN
        INSERT INTO local (lat, lng, nome, descricao) 
        VALUES (lat_local, lng_local, local_nome, local_descricao);
    END IF;

    -- Criação da empresa
    INSERT INTO empresa VALUES (cnpj, razao_social, nome_fantasia, lat_local, lng_local);

    -- Criação dos funcionários
    FOR employee IN SELECT * FROM jsonb_array_elements(employees)
    LOOP
        -- Cria o funcionário
        INSERT INTO funcionario (cnpj_empresa, nome, sexo, cargo, data_nascimento, data_contratacao)
        VALUES (
            cnpj,
            employee->>'nome',
            employee->>'sexo',
            (employee->>'cargo')::cargo,
            (employee->>'data_nascimento')::date,
            (employee->>'data_contratacao')::date
        ) RETURNING codigo INTO new_employee_id;

        -- Registra seus números de telefone, se houver
        IF (employee ? 'telefones')::BOOLEAN THEN
            INSERT INTO telefone_funcionario
            SELECT new_employee_id, telefone
            FROM jsonb_array_elements_text(employee->'telefone') AS telefone
            WHERE telefone != '';
        END IF;

        -- Registra dados específicos de motorista, se aplicável
        IF (employee->>'cargo' = 'Motorista')::BOOLEAN THEN
            INSERT INTO motorista (cnh, codigo_funcionario, status_cnh, data_validade_cnh) VALUES (
                employee->'motorista_data'->>'cnh',
                new_employee_id,
                (employee->'motorista_data'->>'status_cnh')::status_cnh,
                (employee->'motorista_data'->>'data_validade_cnh')::date
            );
        END IF;
    END LOOP;

    -- Criação dos veículos
    FOR vehicle IN SELECT * FROM jsonb_array_elements(vehicles)
    LOOP
        -- Cria o veículo
        INSERT INTO veiculo VALUES (
            vehicle->>'placa',
            cnpj,
            (vehicle->>'codigo_modelo')::INT,
            (vehicle->>'km')::FLOAT,
            (vehicle->>'ano_fabricacao')::INT
        );
    END LOOP;

END;
$$