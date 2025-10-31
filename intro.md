# Sistema de Gestão de Frota de Ônibus do Distrito Federal
### Bancos de Dados - 2025/2 - Universidade de Brasília
#### Integrantes:
- Gabriel de Souza Colombo - 222014062
<br><br>

## Introdução


## Especificação

O objetivo do sistema é possibilitar o gerenciamento da frota de ônibus do Distrito Federal por um administrador do governo. A frota de ônibus é fornecida por empresas de transporte público. Cada empresa é identificada por um CNPJ e possui razão social, nome fantasia, o local da sede e um ou mais funcionários, veículos e linhas de ônibus.

Cada funcionário é identificado por um código e possui CPF, nome, data de nascimento, idade, data de contratação, data de demissão, tempo de serviço, sexo, um ou mais números de telefones e cargo, que deve ser um de três opções: fiscal, motorista ou cobrador. Um funcionário não pode fazer parte de mais de uma empresa ao mesmo tempo. Caso o funcionário seja um motorista, ele deve possuir um número de CNH, junto ao status e a data de validade da CNH.

Um veículo faz parte de somente uma empresa e é identificado pela placa. Todo veículo possui modelo, ano de fabricação, quilometragem e 0 ou mais ocorrências identificadas e manutenções. Todo modelo possui um nome e uma categoria, que por sua vez possui um nome e descrição. Ambos são identificados por um código.\
Toda manutenção veicular possui uma data, hora e 1 ou mais serviços realizados e é identificada por um código atribuído no momento do registro da manutenção. Cada serviço de manutenção é identificado por um código e possui descrição e preço (em reais).

Toda ocorrência pode ser uma avaria ou um acidente. Cada avaria possui descrição, nível de dano leve, moderado ou grave, e uma indicação se o veículo é ou não inoperante devido à avaria (*i.e.*, se é uma avaria total). Um acidente deve possuir descrição, gravidade, número de feridos e número de mortos. Toda ocorrência também deve possuir um local, data, horário e é identificada por um código atribuído no momento do registro da ocorrência.

Uma linha de ônibus faz parte de somente uma empresa e é identificada por um código. Cada linha está associada a um itinerário, que consiste em um local de origem, um local de destino e uma sequência de pontos de parada, que é um local com uma posição específica na sequência. Um local possui e é identificado por uma coordenada geográfica, representada pela latitude e longitude, e pode possuir um nome e/ou descrição.

Por fim, toda viagem possui um horário de partida, de chegada, tempo de duração estimado e um motorista, cobrador, linha de ônibus e veículo que fazem parte da mesma empresa. Logo, uma viagem só pode estar associada a uma empresa.



