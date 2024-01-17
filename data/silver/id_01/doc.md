
# Documentação dos dados do McDonald's Brasil.

Este documento fornece uma documentação da tabela gerada, aqui possuimos tanto informações de localizações do McDonald's, quanto produtos e serviços ofertados e horparios de funcionamento.

## Descrição das Colunas

- `_id` (object): Identificador único do local do McDonald's.
- `active` (bool): Indica se o local está ativo (True) ou inativo (False).
- `name` (object): Código identificador do local.
- `code` (object): Nome do local do McDonald.
- `country` (object): País onde o local está situado.
- `timezone` (object): Fuso horário do local.
- `address` (object): Endereço completo do local.
- `city` (object): Cidade onde o local está situado.
- `neighborhood` (object): Bairro onde o local está situado.
- `cep` (object): Código de Endereçamento Postal (CEP) do local.
- `createdAt` (object): Data e hora de criação do registro do local.
- `updatedAt` (object): Data e hora da última atualização do registro do local.
- `timeSlotsService` (object): Informações sobre os horários de serviço do local.
- `alias` (object): Nome alternativo ou apelido do local.
- `ecommerce` (bool): Indica se o local oferece serviços de e-commerce (True ou False).
- `promotions` (bool): Indica se o local oferece promoções (True ou False).
- `loyalty` (bool): Indica se o local participa de programas de fidelidade (True ou False).
- `distance` (float64): -
- `id` (object): Outro identificador único do local.
- `siglas` (object): Siglas ou abreviações relacionadas ao local.
- `coordinates.longitude` (float64): Longitude geográfica do local do McDonald's.
- `coordinates.latitude` (float64): Latitude geográfica do local do McDonald's.
- `coordinates.lng` (float64): Longitude geográfica alternativa do local do McDonald's.
- `coordinates.lat` (float64): Latitude geográfica alternativa do local do McDonald's.
- `services.breakfast` (bool): Indica se o local oferece serviço de café da manhã.
- `services.mcCafe` (bool): Indica se o local possui um McCafé.
- `services.driveThru` (bool): Indica se o local possui serviço de drive-thru.
- `services.dcOut` (bool): -
- `services.dcIn` (bool): -
- `services.mcDelivery` (bool): Indica se o local oferece o serviço de McDelivery.
- `services.timeExtended` (bool): Indica se o local possui horário de funcionamento estendido.
- `services.mcParty` (bool): Indica se o local oferece serviços para festas.
- `services.playPlace` (bool): Indica se o local possui área de recreação infantil.
- `services.parking` (bool): Indica se o local possui estacionamento.
- `services.wifi` (bool): Indica se o local oferece Wi-Fi gratuito.
- `services.wheelchairAccess` (bool): Indica se o local é acessível para cadeirantes.
- `services.dessertCenter` (object): -
- `services.shoppingCenter` (object): -
- `generalHour.daysOfWeek` (object): Informações sobre os horários de funcionamento nos diferentes dias da semana.

## Informação Adicional

Os dados completos e atualizados sobre estas localizações do McDonald's estão disponíveis em um conjunto de dados privado no Kaggle. 
