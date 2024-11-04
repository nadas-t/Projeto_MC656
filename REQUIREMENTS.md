# Atividade 3: Elicitação de Requisitos

O presente documento tem como objetivo a especificação de requisitos gerais obtidos por uma série de processos de elicitação de requisitos com base na temática geral da aplicação desenvolvida pelo grupo.
Nesse contexto, deve-se lembrar da ideia geral da aplicação, cujo desenvolvimento, em princípio, já foi iniciado: uma plataforma online que permite a gestão financeira pessoal. O site permite que usuários registrem gastos e receitas e se planejem de modo a gastar conscientemente, assim  ajudando-os a realizar sonhos que antes não eram possíveis alcançar por falta de organização. 
Para obtermos os requisitos, foram realizadas duas atividades separadas, uma de _brainwriting_ e outra de _benchmarking_.

## Registro da execução da técnica de elicitação de requisitos

### BrainWriting

O brainwriting é uma técnica de geração de ideias em grupo que permite que os participantes escrevam suas sugestões de forma individual, geralmente em rodadas e sem discussão verbal inicial. Cada participante anota suas ideias em um papel ou ferramenta digital e, após um tempo definido, passa para a pessoa ao lado, que complementa, expande ou sugere novos insights com base nas ideias anteriores. Esse método promove uma participação mais equitativa, evitando o bloqueio criativo e o "efeito de conformidade" causado pela influência de ideias dominantes no grupo, e é particularmente útil para sessões de brainstorming mais estruturadas e silenciosas.
A seguir estão as regras adotadas na condução da dinâmica:
- No início da dinâmica cada membro do tipo recebe uma um cartão em branco;
- Em seguida cada integrante terá 2 minutos para descrever alguma funcionalidade para o sistema;
- Imediatamente após o fim de cada rodada o integrante passa para o cartão seguinte no sentido horário;
- Assim o integrante terá mais 2 minutos para somar as ideias deixadas por outro membro no cartão(propondo mudanças na ideia original, ou adicionando funcionalidades que se relacionem de alguma forma);
- Cada cartão passará exatamente 1 vez por cada membro (no total serão 5 rodadas de 2 minutos);
- Ao fim das rodadas se abre um momento para discussão, em que cada membro lê em voz alta o cartão com o qual começou;
- O conjunto de ideias levantadas são avaliadas e delas são retiradas os requisitos do sistema em desenvolvimento (as ideias que surgiram durante a discussão foram registradas em post-its);

As adições de cada integrante estão nas cores:
1. Thiago - <span style="color: blue">azul</span>
2. Rafael - <span style="color: red">vermelho</span>
3. Lucas - <span style="color: black">preto</span>
4. Daniel - <span style="color: yellow">Amarelo</span>
5. Isac - <span style="color: green">verde</span>

Abaixo estão os prints dos cartões preenchidos ao fim da dinâmica:
![Cartão 1](/doc/images/brainwriting_cartao_1.png)
![Cartão 2](/doc/images/brainwriting_cartao_2.png)
![Cartão 3](/doc/images/brainwriting_cartao_3.png)
![Cartão 4](/doc/images/brainwriting_cartao_4.png)
![Cartão 5](/doc/images/brainwriting_cartao_5.png)

Da presente técnica de elicitação foram extraídos os seguintes requisitos:

##### Requisitos
- O sistema deve oferecer acesso a conteúdos educativos
- O sistema deve permitir acompanhar seus investimentos ( lucro ou perda)
- O sistema deve permitir que o usuário visualize o histórico de lançamentos
- O sistema deve possibilitar  registrar seus lançamentos 
- O sistema deve permitir a visualização dos lançamentos por meio de gráficos
- O sistema deve permitir a adição de diferentes contas de banco
- O sistema deve permitir a adição de diferentes cartões de crédito
- O sistema deve permitir usuários criarem contas em conjunto
- O sistema deve oferecer projeções de cenários financeiros com base em dados de despesas e rendimentos passados.
- O sistema deve permitir o usuários definir limites de gastos e acompanhá los
- O sistema deve permitir o usuários definir metas de receita e acompanhá los
- O sistema deve fornecer feedbacks sobre os padrões de gastos do usuário
- A tela inicial do sistema deve ser customizável de acordo com as preferências do usuário
- O sistema deve permitir a integração com a conta bancária 
- O sistema deve ter um design simples e intuitivo
- A ação de registrar um lançamento deve ser clara e rápida
- O sistema não deve sobrecarregar o usuário visualmente


### Benchmark

Benchmark é o processo de medir e comparar o desempenho, qualidade ou características de um produto, serviço ou processo em relação a um padrão ou referência de mercado, geralmente representado pelos melhores concorrentes ou práticas da indústria. O objetivo é identificar onde uma empresa ou produto se posiciona em relação aos concorrentes, entender boas práticas e buscar melhorias contínuas.
Benchmarking ajuda a entender o que já existe no mercado e quais práticas são consideradas eficientes, permitindo que o novo sistema seja desenvolvido com funcionalidades competitivas e adequadas às expectativas dos usuários.
Nesse sentido segue abaixo os sistemas usados para Benchmark:


#### Organizze

O “Organizze” é uma sistema de gestão financeira pessoal, ele permite através de suas plataforma o registro de entradas e saídas, cadastrar contas, visualizar relatórios, importar arquivos e muito mais. A empresa possui a plataforma versão web e mobile, iremos analisar a versão web já que condiz com a modalidade do nosso projeto. Em geral, o Site se mostra bem intuitivo e minimalista, analisemos então mais a fundo suas telas e funcionalidades.

![Organizze images](/doc/images/organizze_historico_lancamentos.png)
![Organizze images](/doc/images/organizze_lancamento.png)
![Organizze images](/doc/images/organizze_limites.png)
![Organizze images](/doc/images/organizze_relatorio.png)
![Organizze images](/doc/images/organizze_visao_geral.png)


As telas acima representam as mais relevantes do aplicativo com suas principais features. 
O site se mostrou bem simples e objetivo contando com apenas 4 páginas principais ( tela inicial, lançamentos, relatórios e limite de gastos) com um design de bastante “espaço vazio”, o que contribui para evitar que o usuário não se sinta sobrecarregado ao utilizar o sistema.
Apresenta as principais funcionalidades abaixo:
- adicionar gasto e receita que envolve também adicionar tag,categoria,data, descrição, adicionar anexo, permite também selecionar se o gasto já foi debitado ou não e também uma funcionalidade de“repetir o lançamento”
- Na página “lançamentos” , possibilita duas visualizações dos lançamentos “fluxo de caixa” e “todos lançamentos”, permite filtrar,exportar o fluxo e importar além de imprimir
-Na página de “relatórios” gera relatórios personalizados podendo alterar o tipo de gráfico, o período , impor filtros, gerar relatórios em pdf
-permite impor um limite de gastos mensal para diferentes categorias e acompanhá-lo ao decorrer do tempo com gráficos de barras indicando em quais categorias o limite está sendo extrapolado e a visão geral de todas categorias.
- Na tela inicial há uma espécie de dash, com um overview da sua situação financeira assim como shortcuts. Possui o saldo mensal, e também o de receitas e gastos,possui a lista de  contas a pagar e a receber,conta com notícias do blog , overview do limite imposto e dos maiores gastos do mês atual. Ademais, a maioria dos componentes da home podem ser ocultados e movidos sobre a tela de modo a personalizar ainda mais a experiência do usuário.
- Além disso conta com a página de configurações que permitem adicionar e remover contas cartões e categorias, adicionar preferências de uso do sistema entre outros
- O sistema possui também um modo de vizualização de calendário dos gastos
- contêm uma calculadora, um conversor de moedas e um meio de estabelecer metas de receitas assim como tem o de gastos

**Pontos positivos**:

- Design objetivo e simples é uma boa abordagem para desmistificar o tópico que é tido como complicado pela maioria das pessoas. 
- possui dashboards e relatórios
- permite cadastrar e categorizar gastos
- medir despesas
- tela inicial customizável
- dá acesso aos post do blog 

**Pontos negativos**:

- não possui versão gratuita
- não sincroniza com a conta bancária
- certas funcionalidades como calculadora, calendário e metas de receita estão escondidas, dificultando o acesso do usuário
- não possui um suporte para o usuário

#### Meu Dinheiro
"Meu Dinheiro" é uma aplicação web que promete ao usuário auxiliar em sua gestão financeira. Neste contexto ele possuí um conjunto amplo de ferramentas que auxiliam em questões que vão desde do seu controle de gastos a sua gestão de investimentos e estabelecimento de metas financeiras. No entanto, seu uso é baseado em planos de assinatura, sendo assim a experiência do usuário pode ser fortemente impactada pelo plano a qual ele está vinculado, que se relaciona diretamente com restrição das funcionalidades que estarão disponíveis na aplicação. Dito isso, para este estudo, foi utilizado o plano gratuito do "Meu Dinheiro", focando especialmente nas funções que remetem ao controle de gastos.

1. **Visão Geral (Página inicial)**:

Assim que o usuário faz login no site, ele se depara com um dashboard que contém as representações gráficas dos dados que ele registrou na aplicação, que fornecem de forma compreensível e resumida uma visão do usuário sobre o estado geral das suas finanças no último mês. Dentre os painéis mostrados na interface, o que mais se destacam do ponto de vista da equipe foram:

- Despesas por categoria:

    Mostra de forma gráfica as despesas do usuário separando-as por categorias, possibilitando ao usuário ter uma visão mais compartimentalizada dos seus gastos, oferecendo uma noção de quais questões no contexto particular do usuário estão gerando maior ou menor saída de capital;
- Contas a pagar / Contas a receber:

    Agrupam saídas e entradas futuras do caixa do usuário, funcionando como um lembrete das operações financeiras serão realizadas, e facilitando o planejamento do usuário em relação a operações futuras;
- Fluxo de caixa:

    Apresenta uma visualização do montante no caixa do usuário ao longo de um determinado período, dando uma visão geral das saídas e entradas de capital, incluindo operações futuras registradas;

    ![Meu Dinheito Dashboard](/doc/images/meudinheiro_dashboard.png)
    ![Meu Dinheito Dashboard](/doc/images/meudinehiro_dashboard_conf.png)

O dashboard possui opções de customização, permitindo que o usuário defina quais e quantas informações estarão presentes na tela, além de poder ajustar a disposição delas arrastando os blocos. Isso permite que a página seja modificada para apresentar de forma mais imediata as informações que cada usuário considera mais relevante para seu contexto

2. **Cadastro de operação**:

    Ainda na página de cadastro existe um botão no canto inferior direito da tela que na interação abre um modal onde o usuário pode registrar operações financeiras. Exitem 3 tipos de operações que podem ser adicionadas: despesa, receita e transferência, e para cada uma delas o modal assume um layout em que seus campos de preenchimento indicam o que precisa ser inserido. 
    Alguns campos que valem destaque são:
    - Categoria: contém uma lista de contexto que podem ser associadas a um gasto específico, o usuário pode tanto escolher entre um conjunto de valores pré-definidos quando criar categorias personalizadas (opção que aparece ao final da lista). Elas são uteis tanto para o usuário organizar melhorar seus gastos, quanto para a aplicação fazer análises que dependem da categoria das operações;

    - Tag: campo de preenchimento livre que funciona como uma identificação do gasto, não é utilizada propriamente pelas análises do sistema, mas funciona como uma forma identificar um conjunto qualquer de operações seguindo uma regra própria, é usada em funções de pesquisa e filtragem de operações, além de ser indicada em cada registro;

    - Conta: é um campo de seleção que lista as contas bancarias registradas na aplicação, com ela o usuário pode facilmente gerenciar múltiplas contas no mesmo sistema, separando no registro as operações que ocorrem em cada uma.

        ![Meu Dinheito Cadastro Lançamento](/doc/images/meudinheiro_cadastro_lancamento.png)
        ![Meu Dinheito Cadastro Transação](/doc/images/meudinheiro_cadastro_transferencia.png)
        ![Meu Dinheito Categorias Cadastradas](/doc/images/meudinheiro_categorias.png)

Existe ainda uma tela em que o usuário pode criar novas categorias ou visualizar, deletar, e editar as categorias que já estão registradas. Essa página ainda apresenta uma visualização de como as categorias são organizadas, além da separação entre despesas e receitas, o sistema também permite a criação de subcategorias, o que trazem mais estrutura para definição de novas categorias, partindo com que o usuário visualize cada contexto de forma mais natural e possa agrupar certas categorias compartilham um contexto maior.

3. **Relatórios**:

    Essa tela agrupa um conjunto de relatórios que podem ser acessados pelo usuário e que trazem analises simples, mas mais específicas em relação a suas finanças.

    ![Meu Dinheito Relatórios](/doc/images/meudinheiro_relatorios.png)

    Apesar de no geral as informações apresentadas nos relatórios serem bem semelhantes ao que já era visualizado no dashboard da página inicial, nestas telas o usuário é capaz de realizar algumas operações adicionais sobre esses dados, como aplicação de filtros (por tags ou classes) e definição do momento dos dados que devem ser apresentados.

    ![Meu Dinheito Relatório Exemplo](/doc/images/meudinheiro_relatorio_exemplo.png)
    ![Meu Dinheito Fluxo de Caixa Exemplo](/doc/images/meudinheiro_fluxo_caixa.png)

4. **Configurações de utilização**: 

    Permite que usuário configure parte do comportamento da aplicação, que dá espaço para que ele decida o comportamento questões como o cadastro de operações, segurança, análise dos dados, e acessibilidade da aplicação. 
    ![Meu Dinheito Configuração de Utilização](/doc/images/meudinheiro_conf_usabilidade.png)

    **Pontos positivos**:
    - A aplicação apresenta os dados de interesse do usuário de uma forma clara e acessível por um dashboard;
    - As categorias de lançamentos são bem organizadas, incluindo uma ideia de hierarquia que ajuda a dar mais contexto para cada gasto;
    - O usuário é capaz de registrar gastos e entradas futuras, que são usadas análises da aplicação (como no fluxo de caixa), o que permite que o usuário se planeje;
    - A página inicial possui um certo nível de customização, permitindo o usuário alterar a interface para mostrar informações que sejam mais relevantes para ele;
    - O cadastro de novas operações financeiras é simples e instrui bem o usuário no preenchimento de informações;
    - O cadastro de operações financeiras permite um certo nível de customização, pela criação de categorias e tags próprias do usuário, adaptando-se melhor ao contexto de cada indivíduo;
    - É possível fazer a sincronização com a conta bancaria do usuário, dispensado o preenchimento manual de operações financeiras;

    **Pontos negativos**:
    - Os relatórios não são autoexplicativos e precisam que o usuário tenha um certo conhecimento prévio em gestão financeira;
    - Não é possível alterar o intervalo de tempo que será mostrado no dashboard, limitando-se somente ao mês, tornando a apresentação e análise dos dados menos versátil;
    - Nos relatórios, apesar de ser possível alterar o momento dos dados apresentados, não é possível alterar a janela de tempo considera, tornado a visualização mais limitada em alguns casos;
    - A interface é pouco autoexplicativa e minimalista demais, um usuário inexperiente no sistema pode ter dificuldade de localizar seus recursos, tais como relatórios, registros de gastos passados e até cadastrar uma nova operação, que estão dispersos pelo menu da aplicação;
    - A pouca descrição também gera uma dificuldade em customizar o sistema, como na tela de “Configurações de utilização” em que não é claro a consequência de cada opção, nomeadas e descritas por termos técnicos que não são acessíveis a um usuário leigo.


#### Orçamento fácil
O "Orçamento Fácil" é um sistema que tem como proposta principal o gerenciamento das finanças pessoais dos usuários e o controle de despesas. Também oferece planos anuais que incluem recursos adicionais, como a possibilidade de salvar os dados online, sincronização bancária automática e acesso à aplicação web. Lamentavelmente, o foco do nosso projeto é web, e o “Orçamento Fácil” disponibiliza essa funcionalidade como um recurso pago.

1. **Tela inicial**:

    ![Tela inicial](/doc/images/Facil1.png)

    A tela inicial possui vários itens, o que pode tornar o design cansativo para os usuários. No entanto, há a opção de acrescentar e remover itens da tela, o que proporciona maior conforto. Além disso, é possível organizar os itens mais utilizados no topo da aplicação, tornando o uso mais eficiente.

2. **Sincronização com várias contas bancárias de maneira automática**:

    Apesar de ser uma função paga, isso oferece ainda mais facilidade no controle financeiro dos usuários, permitindo que vejam o saldo a qualquer momento. Essa visibilidade pode ajudar o usuário a tomar decisões mais precisas.

    ![Varias contas](/doc/images/Facil2.png)

3. **Realização de orçamentos**:

    É possível, neste sistema, acrescentar valores a serem gastos e ver como isso influencia o seu saldo bancário.

    ![Orçamento](/doc/images/Facil3.png)

4. **Gerenciamento de transações**:

    O sistema oferece a opção de controlar todas as transações realizadas dentro de um determinado período, além de permitir a categorização das transações, o que proporciona ainda mais praticidade aos usuários.

    ![Orçamento](/doc/images/Facil4.png)

5. **Gráficos**:

    O “Orçamento Fácil” oferece a opção de visualizar os gastos por meio de gráficos, tornando o controle das despesas mais visual e intuitivo.

    ![Orçamento](/doc/images/Facil5.png)

6. **Multi plataformas**:

    Uma das opções mais interessantes deste aplicativo é que ele é multiplataforma, ou seja, é possível usá-lo em diversos tipos de dispositivos, como smartphones, tablets e na web.

    - **Smartphone**
        ![Smartphone](/doc/images/Facil6.png)

    - **Tablet**
    ![Tablet](/doc/images/Facil7.png)

    - **Web**
    ![Web](/doc/images/Facil8.png)

7. **Outras funcionalidades**:

    Esse sistema possui outras funcionalidades interessantes, como a opção de salvar seus dados online, permitindo que o controle financeiro seja realizado em qualquer dispositivo e em qualquer lugar, desde que haja conexão com a internet. Além disso, é possível importar dados de outro aplicativo de controle de gastos por meio de um arquivo CSV. Fora isso, o sistema também conta com suporte online para ajudar os usuários.

**Pontos positivos**:
-  A aplicação oferece diversos tipos de customizações;
-  Oferece uma transição fácil de outras aplicações do mesmo tipo;
- Sincronização com contas de vários bancos;
- Possibilidade de adicionar e remover categorias;
- Ser multi plataformas;

**Pontos negativos**:
- Boa parte de seus recursos serem limitados a planos anuais;
 - Ser limitado a controle de gastos e controle financeiro apenas, ou seja, não apresenta nenhuma orientação aos usuários de como gerir o seu dinheiro;
- Falta de opções de investimentos;

Dos benchmarks foram extraídos os seguintes requisitos:
##### Requisitos
- O sistema deve oferecer projeções de cenários financeiros com base em dados de despesas e rendimentos passados;
- O sistema deve permitir a simulação de compras ou despesas futuras;
- O sistema deve permitir exportar relatórios via PDF;
- O sistema deve permitir importar dados a partir de planilhas e CSVs;

