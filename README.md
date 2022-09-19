# Challenge de Data Science

<div align="center">
<img src="https://i.imgur.com/oxab3uu.png" width="800px" />
</div>

Somos uma equipe de dados que foi contratada para fazer parte do banco digital internacional chamado **Alura Cash**. No primeiro dia, a diretoria financeira nos convocou para uma reunião para informar que, recorrentemente, estão surgindo pessoas inadimplentes após a liberação de créditos.

Por conta disso, foi solicitada uma solução para diminuir as perdas financeiras geradas por pessoas mutuárias que não quitam suas dívidas. Nos foi informado também que teríamos o prazo de **um mês** para encontrar essa solução e apresentá-la à diretoria financeira. Sendo assim, solicitamos um conjunto de dados contendo as informações de clientes, da solicitação de empréstimo, do histórico de crédito, bem como se a pessoa mutuária é inadimplente ou não.

## Semana 1

A semana 1 é dedicada à análise e estruturação dos dados oferecidos pelo banco com MySQL. Primeiro, foi notado que os dados estavam diferentes dos usuais, pois sua fonte era um ***dump***, o que nos exigiu uma atenção especial na manipulação deles. Assim, buscamos ler todo o registro para entender nossos dados. Notamos que os valores estavam divididos por tabelas características, com valores de ID referenciando os dados de cada cliente.

Então, iniciamos analisando as informações que o conjunto de dados possuía.  Observamos que os dados estavam em inglês, os valores de texto estavam sem padronização, além de vários valores nulos.

Foi percebida também a existência de uma tabela que continha a relação de todos os IDs de uma mesma pessoa cliente do Alura Cash. Dessa forma, o primeiro passo foi tratar nossos dados para deixá-los padronizados no texto, bem como, corrigir inconsistências relacionadas ao tipo e estruturação deles.

Depois buscamos unir as tabelas pelos valores de IDs que eram correspondentes entre si, deixando todos os dados em uma única tabela de dados de clientes. Após uma conversa entre a equipe, decidimos não eliminar os valores nulos dentro do banco de dados, pois poderiam conter informações de clientes que são importantes para o banco.

A tabela de dados unidos foi exportada do MySQL como ***csv*** e será utilizada nas próximas semanas.

## Semana 2

Na semana 2 buscamos construir um modelo de ML que pudesse predizer de acordo com os dados bancários de cada cliente, se essa pessoa pode ou não se tornar inadimplente. Dessa vez, utilizamos o **Python** no ambiente do **Google Colab** para desenvolver nosso modelo.

Primeiramente, coletamos os dados da semana 1 e iniciamos uma análise focada no tratamento de dados para serem inseridos em um modelo de ML,. Desse modo, removemos valores nulos e outliers presentes nos dados, bem como aplicamos o balanceamento, normalização e enconding para tratar o conjunto de dados.

Assim, construimos três modelos de aprendizado de máquina pensando na explicabilidade do resultado final, comparamos o desempenho deles para o projeto e escolhemos o que teve melhor performance. Com isso, buscamos melhorar ainda mais o resultado final do modelo com uma otimização de hiperparâmetros e, assim que obtivemos um bom produto final, salvamos o modelo fazendo sua exportação.

## Semana 3 e 4

Na semana 3 e 4 decidimos construir uma forma de apresentar todas as análises que fizemos nos nossos dados: análises estatísticas e extração de características para fazermos o modelo de aprendizado de máquina. Pensamos assim, em utilizar o **Power BI** como ferramenta para estruturar o que encontramos e permitir que nele pudéssemos realizar ainda mais análises posteriormente.

Desse modo, para disponibilizarmos o modelo de ML, criamos uma **API** que recebe os dados de cada cliente como entrada e tem como retorno o resultado de uma possível inadimplencia ou não desse cliente. Conectamos essa API ao Power BI e assim conseguimos inserir os dados em forma de parâmetros do **Power Query** e temos o retono da API no próprio dashboard, podendo assim fazer consultas em tempo real.

Além disso, também foi feito uma análise gráfica para comparar o resultado do modelo de ML com o conjunto de dados construido na semana 1, entendendo o porquê do resultado fornecido pelo modelo.

Assim, conseguimos solucionar o problema do banco Alura Cash, através da ajuda na identificação de um possível pessoa inadimplente antes da liberação de créditos. Ademais, também tivemos sucesso ao apresentar nossa proposta à diretoria financeira através do nosso dashboard em Power BI! xD

## Equipe de Dados

### Maria Gabriela

<div align="left">
<img src="https://i.imgur.com/rtR5ClI.jpg" width="300px" />
</div>

Maria é formada em Sistemas para Internet, apaixonada por tecnologia, dados e gatos. Atuou na área de infra e desenvolvimento. É especialista em SQL, com conhecimento nos bancos de dados mais utilizados atualmente e um pézinho em BI, com o qual tem se desenvolvido tecnicamente.

<a href="https://www.linkedin.com/in/mariagcoliva/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>

### Danielle Oliveira

<div align="left">
<img src="https://i.imgur.com/JBep2hL.png" width="300px" />
</div>

Danielle é formada em Sistemas de Informação. Fez parte do Scuba Team. Atualmente é instrutora nas áreas de Banco de dados, Business Intelligence e NoSQL. É apaixonada por livros, música e tecnologia.

<a href="https://www.linkedin.com/in/danielle-oliveira-071550134/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>

### Mirla Costa

<div align="left">
<img src="https://i.imgur.com/eqC6qrV.jpg" width="300px" />
</div>

Graduanda em Engenharia elétrica pela Universidade Federal do Piauí com pesquisa focada em Aprendizado de Máquina e Inteligência Computacional. Atua como Scuba na Escola de Data Science da Alura e sempre amou muito programar, ensinar e trabalhar com tecnologia. Em seu tempo livre, dedica-se a brincar com seus animais, assistir animações e séries, além de jogar RPG de mesa.

<a href="https://www.linkedin.com/in/mirla-costa/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>

### João Miranda

<div align="left">
<img src="https://i.imgur.com/6evW05p.png" width="300px" />
</div>

Bacharel em Matemática pela UFMG e especialista em Data Science e Analytics pela USP/Esalq. Atualmente é instrutor na Escola de Dados da Alura. Gosta muito de livros, jogos eletrônicos, boardgames e tiro com arco.

<a href="https://www.linkedin.com/in/joaovmiranda/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
