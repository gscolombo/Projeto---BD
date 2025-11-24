# Sistema de Gestão de Frota de Ônibus do Distrito Federal
### Bancos de Dados - 2025/2 - Universidade de Brasília
#### Integrantes:
- Gabriel de Souza Colombo - 222014062
- Eduardo de Paula Carvalho - 251039175
<br>

## Introdução
O presente projeto visa a construção de um sistema para monitoramento da frota de ônibus atuante no Distrito Federal, assim como o gerenciamento dos dados por um administrador do governo (GDF). No caso, espera-se que o produto final possibilite ao usuário tanto a visualização de um *dashboard* com informações relevantes sobre a frota do DF a partir dos dados cadastrados, assim como o registro e atualização desses dados. De maneira geral, espera-se que o sistema seja possibilite o/a: registro, atualização e visualização de dados de empresas, funcionários e veículos do transporte público do DF; registro e monitoramento de viagens, com visualização de itinerário e outras informações associadas; visualização de estatísticas e informações relevantes sobre a frota de ônibus do DF.

A princípio, o sistema será desenvolvido considerando sua utilização por um único usuário, para evitar lidar com questões de autenticação presentes em um sistema multiusuário.<br>
É apresentado em seguida a especificação do sistema que auxiliou na elaboração do modelo conceitual.

#### Especificação do sistema

>O objetivo do sistema é possibilitar o gerenciamento da frota de ônibus do Distrito Federal por um administrador do governo. A frota de ônibus é fornecida por empresas de transporte público. Cada empresa é identificada por um CNPJ e possui razão social, nome fantasia, o local da sede e um ou mais funcionários, veículos e linhas de ônibus.
>
>Cada funcionário é identificado por um código e possui CPF, nome, data de nascimento, idade, data de contratação, data de demissão, tempo de serviço, sexo, um ou mais números de telefones e cargo, que deve ser um de três opções: fiscal, motorista ou cobrador. Um funcionário não pode fazer parte de mais de uma empresa ao mesmo tempo. Caso o funcionário seja um motorista, ele deve possuir um número de CNH, junto ao status e a data de validade da CNH.
>
>Um veículo faz parte de somente uma empresa e é identificado pela placa. Todo veículo possui modelo, ano de fabricação, quilometragem e 0 ou mais ocorrências identificadas e manutenções. Todo modelo possui um nome e uma categoria, que por sua vez possui um nome e descrição. Ambos são identificados por um código.\
Toda manutenção veicular possui uma data, hora e 1 ou mais serviços realizados e é identificada por um código atribuído no momento do registro da manutenção. Cada serviço de manutenção é identificado por um código e possui descrição e preço (em reais).
>
>Toda ocorrência pode ser uma avaria ou um acidente. Cada avaria possui descrição, nível de dano leve, moderado ou grave, e uma indicação se o veículo é ou não inoperante devido à avaria (*i.e.*, se é uma avaria total). Um acidente deve possuir descrição, gravidade, número de feridos e número de mortos. Toda ocorrência também deve possuir um local, data, horário e é identificada por um código atribuído no momento do registro da ocorrência.
>
>Uma linha de ônibus faz parte de somente uma empresa e é identificada por um código. Cada linha está associada a um itinerário, que consiste em um local de origem, um local de destino e uma sequência de pontos de parada, que é um local com uma posição específica na sequência. Um local possui e é identificado por uma coordenada geográfica, representada pela latitude e longitude, e pode possuir um nome e/ou descrição.
>
>Por fim, toda viagem possui um horário de partida, de chegada, tempo de duração estimado e um motorista, cobrador, linha de ônibus e veículo que fazem parte da mesma empresa. Logo, uma viagem só pode estar associada a uma empresa.

---
## Modelo Conceitual
Abaixo, é apresentado o modelo conceitual com base na especificação. O nome de relacionamentos deve ser interpretado da esquerda para a direita ou de cima para baixo, com prevalência do primeiro caso. Por exemplo, para a relação entre **Linha** e **Local**, lê-se 
```text
1 Linha compõem o itinerário de N Local
```

Buscou-se utilizar a mesma notação do livro *Fundamentals of Database Systems*, do Navathe. O programa para confecção do modelo foi o aplicativo *web* [\underline{drawio}](https://www.drawio.com/).<br>
Para facilitar a visualização, a imagem também pode ser acessada pelo [\underline{navegador}](https://raw.githubusercontent.com/gscolombo/Projeto---BD/refs/heads/main/drawio/conceptual_model.drawio.svg).

![Modelo conceitual](./drawio/conceptual_model.drawio.png)

Um dos pontos principais do modelo acima é a relação entre **Local** e **Linha**, representada por um itinerário. Como especificado, toda linha de ônibus é um código que referencia uma sequência de pontos de parada do ônibus. Por exemplo, a linha `0.110` da viação (empresa) Piracicabana aponta somente para um itinerário, que também pode ser referenciado por outra linha de outra empresa. O itinerário em si consiste somente de de uma sequẽncia de locais, isto é, um ou mais locais ordenados. Nesse caso, para manter a generalidade da entidade **Local**, o atributo que define onde o local está posicionado na sequência foi incluído na relação entre **Local** e **Linha**, visto que só possui significado quando se refere a um itinerário.

\newpage
## Modelo Relacional
Abaixo é apresentado o modelo relacional com base no modelo conceitual elaborado. Foi utilizado o aplicativo *web* [\underline{dbdiagram}](https://dbdiagram.io/home/) para sua criação. Esse aplicativo também permite a geração de uma documentação para o banco de dados, que pode ser acessada [\underline{aqui}](https://dbdocs.io/gscolombo404/Projeto-BD).

![Modelo relacional](./images/Projeto_BD.png)

\newpage
## Geração do banco de dados
Com base no modelo relacional elaborado, o *script* SQL abaixo foi utilizado para gerar o banco de dados. Além dos comandos para criação das tabelas, também há a criação dos tipos `ENUM` para algumas das colunas. Ao final do *script*, também foram criados dois *triggers* para checar se os funcionários a serem cadastrados nas tabelas `Motorista` e `Viagem` possuem o cargo esperado, como definido na especificação.

```sql
/* Criação de tipos ENUM */
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'status_cnh') THEN
    CREATE TYPE status_cnh AS ENUM ('Válida', 'Vencida', 'Suspensa');
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'cargo') THEN
    CREATE TYPE cargo AS ENUM ('Fiscal', 'Motorista', 'Cobrador');
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'grau') THEN
    CREATE TYPE grau AS ENUM ('Leve', 'Moderado', 'Grave');
  END IF;
END$$;

/* Criação de tabelas */
CREATE TABLE IF NOT EXISTS Local (
  lat float NOT NULL,
  lng float NOT NULL,
  nome varchar,
  descricao varchar,
  PRIMARY KEY (lat, lng)
);

CREATE TABLE IF NOT EXISTS Empresa (
  cnpj char(14) PRIMARY KEY,
  razao_social varchar NOT NULL,
  nome_fantasia varchar,
  lat_local float NOT NULL,
  lng_local float NOT NULL,
  FOREIGN KEY (lat_local, lng_local) REFERENCES Local (lat, lng) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Funcionario (
  cnpj_empresa char(14) NOT NULL,
  codigo BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  nome varchar NOT NULL,
  sexo varchar,
  cargo cargo NOT NULL,
  data_nascimento date,
  data_contratacao date,
  data_demissao date,
  FOREIGN KEY (cnpj_empresa) REFERENCES Empresa (cnpj)
);

CREATE TABLE IF NOT EXISTS Telefone_Funcionario (
  codigo_func bigint NOT NULL,
  telefone varchar(12) UNIQUE,
  PRIMARY KEY (codigo_func, telefone),
  FOREIGN KEY (codigo_func) REFERENCES Funcionario (codigo)
);

CREATE TABLE IF NOT EXISTS Motorista (
  cnh char(9) PRIMARY KEY,
  codigo_funcionario bigint NOT NULL UNIQUE,
  status_cnh status_cnh NOT NULL,
  data_validade_cnh date NOT NULL, 
  FOREIGN KEY (codigo_funcionario) REFERENCES Funcionario (codigo) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Categoria (
  codigo int PRIMARY KEY,
  nome varchar UNIQUE NOT NULL,
  descricao varchar
);

CREATE TABLE IF NOT EXISTS Modelo (
  codigo int PRIMARY KEY,
  codigo_categoria int NOT NULL,
  nome varchar UNIQUE NOT NULL,
  FOREIGN KEY (codigo_categoria) REFERENCES Categoria (codigo)
);

CREATE TABLE IF NOT EXISTS Veiculo (
  placa char(7) PRIMARY KEY,
  cnpj_empresa char(14) NOT NULL,
  codigo_modelo int NOT NULL,
  km float,
  ano_fabricacao int,
  FOREIGN KEY (cnpj_empresa) REFERENCES Empresa (cnpj),
  FOREIGN KEY (codigo_modelo) REFERENCES Modelo (codigo)
);

CREATE TABLE IF NOT EXISTS Manutencao (
  id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  placa_veiculo char(7) NOT NULL,
  data_hora timestamp,
  FOREIGN KEY (placa_veiculo) REFERENCES Veiculo (placa) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Servico (
  codigo bigint PRIMARY KEY,
  descricao varchar,
  valor float
);

CREATE TABLE IF NOT EXISTS Manutencao_Servico (
  id_manutencao int NOT NULL,
  codigo_servico int NOT NULL,
  PRIMARY KEY (id_manutencao, codigo_servico),
  FOREIGN KEY (id_manutencao) REFERENCES Manutencao (id),
  FOREIGN KEY (codigo_servico) REFERENCES Servico (codigo)
);

CREATE TABLE IF NOT EXISTS Ocorrencia (
  id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  placa_veiculo char(7) NOT NULL,
  data_hora timestamp NOT NULL,
  lat_local float NOT NULL,
  lng_local float NOT NULL,
  FOREIGN KEY (placa_veiculo) REFERENCES Veiculo (placa),
  FOREIGN KEY (lat_local, lng_local) REFERENCES Local (lat, lng)
);

CREATE TABLE IF NOT EXISTS Acidente (
  id_ocorrencia int PRIMARY KEY,
  descricao varchar,
  gravidade grau NOT NULL,
  numero_feridos int,
  numero_mortos int,
  FOREIGN KEY (id_ocorrencia) REFERENCES Ocorrencia (id)
);

CREATE TABLE IF NOT EXISTS Avaria (
  id_ocorrencia int PRIMARY KEY,
  descricao varchar,
  nivel_dano grau NOT NULL,
  total bool DEFAULT FALSE,
  FOREIGN KEY (id_ocorrencia) REFERENCES Ocorrencia (id)
);

CREATE TABLE IF NOT EXISTS Linha (
  cnpj_empresa char(14) NOT NULL,
  codigo varchar(5) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Itinerario (
  codigo_linha varchar(5) NOT NULL,
  lat_local float NOT NULL,
  lng_local float NOT NULL,
  numero int NOT NULL,
  PRIMARY KEY (codigo_linha, lat_local, lng_local, numero),
  FOREIGN KEY (codigo_linha) REFERENCES Linha (codigo) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (lat_local, lng_local) REFERENCES Local (lat, lng) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Viagem (
  codigo_linha varchar(5) NOT NULL,
  codigo_cobrador bigint NOT NULL,
  codigo_motorista bigint NOT NULL,
  placa_veiculo char(7) NOT NULL,
  data date NOT NULL,
  hora_partida timestamp NOT NULL,
  hora_chegada timestamp,
  PRIMARY KEY (
    codigo_linha,
    codigo_cobrador,
    codigo_motorista,
    placa_veiculo,
    data,
    hora_partida
  ),
  FOREIGN KEY (codigo_linha) REFERENCES Linha (codigo),
  FOREIGN KEY (codigo_cobrador) REFERENCES Funcionario (codigo),
  FOREIGN KEY (codigo_motorista) REFERENCES Funcionario (codigo),
  FOREIGN KEY (placa_veiculo) REFERENCES Veiculo (placa)
);


/* Criação de triggers e funções auxiliares */

-- Função para checar se o cargo de um funcionário é igual ao cargo esperado
CREATE OR REPLACE FUNCTION checkFuncRole (func_id BIGINT, expected_role cargo) RETURNS BOOLEAN AS $$
DECLARE
    actual_role cargo;
BEGIN
    SELECT cargo INTO actual_role
    FROM Funcionario
    WHERE codigo = func_id;

    IF NOT FOUND THEN
      RETURN FALSE;
    END IF;

    RETURN actual_role = expected_role;
END;
$$ LANGUAGE plpgsql;

-- Trigger function para bloquear operações INSERT inválidas
CREATE OR REPLACE FUNCTION prevent_invalid_insert()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_TABLE_NAME = 'motorista' THEN
    RAISE EXCEPTION 'Operação inválida: Funcionário de código % não possui cargo "Motorista"', 
    NEW.codigo_funcionario;
    IF NOT checkFuncRole(NEW.codigo, 'Motorista') THEN
      RAISE EXCEPTION 'Operação inválida: Funcionário de código % não possui cargo "Motorista"', 
      NEW.codigo_funcionario;
    END IF;
  END IF;
  
  IF TG_TABLE_NAME = 'viagem' THEN
    IF NOT checkFuncRole(NEW.codigo_cobrador, 'Cobrador') THEN
      RAISE EXCEPTION 'Operação inválida: Funcionário de código % não possui cargo "Cobrador"', 
      NEW.codigo_cobrador;
    END IF;
    IF NOT checkFuncRole(NEW.codigo_motorista, 'Motorista') THEN
      RAISE EXCEPTION 'Operação inválida: Funcionário de código % não possui cargo "Motorista"', 
      NEW.codigo_motorista;
    END IF;
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para checar se um motorista possui o cargo "Motorista"
CREATE OR REPLACE TRIGGER block_invalid_driver_insert 
  BEFORE INSERT ON Motorista
  FOR EACH ROW
  EXECUTE FUNCTION prevent_invalid_insert();

-- Trigger para checar se o cobrador e o motorista de uma viagem possuem os cargos
-- correspondentes
CREATE OR REPLACE TRIGGER block_invalid_travel_insert 
  BEFORE INSERT ON Viagem
  FOR EACH ROW
  EXECUTE FUNCTION prevent_invalid_insert();
```