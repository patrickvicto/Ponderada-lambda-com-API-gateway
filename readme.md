# Testes

## Como realizar

1 - Para realizar os testes primero instale as as dependencias nescessarias:

pip install pytest
pip install requests

2 - A o lambda e o api gateway devem estar rodando

3- Acesse a pasta com os arquivos e de com comando para iniciar o teste com pytest

pytest

## Testes criados

1 - teste_enviar_json(), Teste de funcionamento do lambda, verifique se o envio e o retorno do json esta corretamente funcionando.

2 - teste_segurança(), Teste para verificar se caso a senha errada seja utilizada o acesso vai ser negado.

3 - teste_tipo_request():, Teste para verificar se o code de tipo errado de requisição está corretamente funcionando.

# Descrição da solução 

## Configuração Lambda

Para o lambda foram utilizas as seguintes configurações:

Criar do Zero
Nome da função: PonderadaSemana2
Tempo de execução: python 3.11

Alterar a função de execução padrão
	Usar uma função existente: LabRole
 
Gatilho: API Gateway

Codigo: O codigo utilizado foi o lambda_function.py, que se encontra nessa pasta.

## Configuração Api Gateway

Intent: create a new API
API type: Rest API
Security: Open


## Edpoint rest

## Authenticação

# Como utilizar a solução 

## Passo a passo

1 - Crie uma requisição no seguinte formato

Header: KEY: senha
	VALUE: pk

Body: um Json

'pk', como mencionado, foi a senha definida para authenticação

2 - Enviei uma requsição com metodo post para o endpoint:

https://wilzt9a9qb.execute-api.us-east-1.amazonaws.com/default/ponderadaSemana2

## Exemplo:

## Resultado esperado:

Com a solução esperase que ao enviar um json a solução devolva o json enviado pelo metodo post.







