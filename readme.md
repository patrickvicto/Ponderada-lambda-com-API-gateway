# Testes

## Como realizar

1 - Para realizar os testes primeiro instale as as dependências necessárias:

`pip install pytest`

`pip install requests`


2 - A o lambda e o api gateway devem estar rodando

3- Acesse a pasta com os arquivos e de com comando para iniciar o teste com pytest:

`pytest`

## Testes criados

1 - teste_enviar_json(), Teste de funcionamento do lambda, verifique se o envio e o retorno do json está corretamente funcionando.

2 - teste_segurança(), Teste para verificar se caso a senha errada seja utilizada o acesso vai ser negado.

3 - teste_tipo_request():, Teste para verificar se o code de tipo errado de requisição está corretamente funcionando.

# Descrição da solução 

## Configuração Lambda

Para o lambda foram utilizadas as seguintes configurações:

Criar do Zero

Nome da função: PonderadaSemana2

Tempo de execução: python 3.11

Alterar a função de execução padrão

Usar uma função existente: LabRole
 
Gatilho: API Gateway

Código: O código utilizado foi o lambda_function.py, que se encontra nesta pasta.

## Configuração Api Gateway

Intent: create a new API

API type: Rest API

Security: Open

## Endpoint rest

No código do endpoint foram criadas 2 classes

VerificadorTipo: Voltada para o verificação do tipo de request

VerificadorAcesso: Voltada para verificar a chave de acesso para utilização da api

Objetivo do Endpoint:

Endpoint para o recebimento e devolução de json enviado pelo úsuario com o método post, mediante a um header com a senha estipulada. Sendo o Json fornecido no Body e a senha no header.

## Authenticação

Para autenticação e controle de acesso ao endpoint foi criada a senha "pk" que deve ser passada no header da requisição no formato:

KEY: Senha

VALUE: PK

# Como utilizar a solução 

## Passo a passo

1 - Crie uma requisição no seguinte formato

Header: 

KEY: senha

VALUE: pk

Body: um Json

'pk', como mencionado, foi a senha definida para autenticação

2 - Envie uma requisição com método post para o endpoint:

https://wilzt9a9qb.execute-api.us-east-1.amazonaws.com/default/ponderadaSemana2

## Exemplo:

Header

![image](https://github.com/patrickvicto/Ponderada-lambda-com-API-gateway/assets/99202408/b6cc0327-a248-4efb-a1d4-11feae21a559)

Body:

![image](https://github.com/patrickvicto/Ponderada-lambda-com-API-gateway/assets/99202408/42376152-9bc6-473c-bfc1-e327156177ee)

Resposta:

![image](https://github.com/patrickvicto/Ponderada-lambda-com-API-gateway/assets/99202408/4b785c37-8e4b-45b9-9006-007d1c2c8fad)

## Resultado esperado:

Com a solução espera se que ao enviar um json a solução devolva o json enviado.








