# Testes de Nivelamento Intuitive Care

Avaliado: Andrey Matheus Brambilla

Comentarios extras:

Exercicio dois:
Muito embora eu já soubesse que era possível extrair tabelas de arquivos PDF, nunca havia feito isso. Após algumas pesquisas, 
encontrei algumas bibliotecas que realizam essa tarefa, como: pdfplumber, tabula e camelot. Como o tabula necessita
de Java além do Python, e o camelot exige duas dependências adicionais, optei por utilizar o pdfplumber por ser mais 
simples.

Exercício três:

3.3 E 3.4 -

Definir os tipos de dados no banco e estruturar o banco de dados. Creio que esses sejam os dois pontos principais aqui.

Na tabela referente aos relatórios de cadastro de operadores (CADOP), ao analisá-la, me incomodou o fato de o endereço estar 
diretamente na tabela, sem ser separado em outra tabela com uma chave estrangeira indicando-o. Contudo, refleti que essa abordagem 
poderia ser o padrão da empresa e que tentar separá-los poderia acarretar problemas. Empresas grandes, que têm filiais, poderiam 
enfrentar desconexão de dados ao mudar a estrutura do banco, já que nem todas as filiais mudariam seus sistemas ao mesmo tempo. Além
disso, essa mudança poderia gerar erros simplesmente pela falta de costume dos usuários. Sendo assim, mesmo que não seja uma boa 
prática, decidi deixar tudo em uma única tabela.

Após isso, para definir os tipos de variáveis, tentei optar por configurações mais abrangentes, pois não conhecia a origem dos dados
nem sua aplicação. Também considerei possíveis problemas, como salvar o DDD no formato `+5511` em vez de apenas `11`. Por conta
disso, defini o DDD como `VARCHAR(5)`. Sei que existem processamentos para normalizar esses dados antes de serem enviados ao banco
de dados; porém, neste teste, não tenho esse conhecimento e preferi salvar os dados assim, evitando retornos de erro. Dessa forma,
os dados não serão perdidos e poderão ser tratados futuramente.

Já as tabelas trimestrais foram onde os maiores desafios surgiram... Todas as tabelas são muito grandes e muitos dados estavam 
despadronizados. 

Ao analisar essas tabelas, percebi que os arquivos dos últimos dois anos das contábeis compartilhavam as mesmas colunas. Assim, 
enfrentei um dilema: poderia optar por fundir as tabelas no banco de dados, o que reduziria a complexidade das consultas, mas aumentaria o custo de processamento. Por outro lado, poderia mantê-las separadas, o que exigiria consultas mais complexas, mas manteria os dados melhor organizados e reduziria o custo de processamento.
Minha decisão foi baseada no fato de que consultas mais complexas quase não geram custos adicionais, seja em tempo ou dinheiro, 
enquanto o aumento no custo de processamento pode causar atrasos em relatórios ou similares. Além disso, há questões de 
escalabilidade, considerando que estamos lidando com cerca de 750 mil linhas por trimestre, chegando a 3 milhões por ano. Em pouco
tempo, usar uma tabela única poderia causar grandes problemas. Por isso, mantive as tabelas separadas.

Após definir isso, tentei criar a chave estrangeira para indicar a operadora. Contudo, alguns registros eram provenientes de 
operadoras não registradas, por motivos desconhecidos. Isso tornava a importação inviável. Enfrentei, então, duas opções: criar 
entradas na tabela principal com todos os campos, exceto a chave primária, nulos; ou excluir os dados sem pares. 

Acabei tomando uma decisão que considero parcialmente errada, pois envolve perda de dados: optei por excluir as linhas sem pares, 
utilizando tabelas temporárias durante a importação.

Também percebi que não existiam colunas únicas nas tabelas. Utilizei um código simples em Python, com a biblioteca Pandas, para 
testar essa condição, e adicionei uma coluna de ID auto-incremental como chave primária.

Outro ponto a ser mencionado é que a coluna de data da tabela 4T2023 fugiu do padrão das demais. Além disso, ao tentar importar, 
percebi que várias colunas apresentavam erros. Como o pedido era para produzir um arquivo SQL, entendi que não deveria realizar o 
tratamento dos dados diretamente. Dessa forma, optei por fazer ajustes mínimos e algumas modificações de acordo com minhas 
preferências pessoais, organizando tudo em um arquivo separado chamado Adicional.sql. No arquivo principal, ImportCSV.sql, 
realizei a importação dos dados, usando em sua maioria o tipo `VARCHAR`, devido aos problemas encontrados.


Exercicio quatro: 

 Muito embora eu ja tenha feito alguns projetos academicos com angular e react, esta foi minha primeira interação com vue porem
como todo framework de html a estrutura não muda muito, outro ponto que utilizei pela primeira vez foi o back com python em outros
projetos sempre utilizei do javascript apenas.
Apesar da falta de conhecimento inicial creio que consegui atender os requesitos da atividade.
