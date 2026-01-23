📊 SincroEstoque: Automação de Inventário e Dashboard de Monitoramento
O SincroEstoque é uma solução robusta de automação de back-end desenvolvida para otimizar a sincronização de estoques e preços em operações de Marketplace. O projeto integra processamento de dados com Python, persistência em SQLite e uma interface visual para tomada de decisão em tempo real.

🚀 Funcionalidades
Automação de Sincronização: Processamento em lote de produtos com simulação de integração via API.

Validação de Regras de Negócio: Filtros automáticos para impedir a entrada de dados inconsistentes (preços negativos ou estoque zerado).

Arquitetura Resiliente: Implementação de logs detalhados para auditoria e rastreabilidade de erros.

Segurança de Dados: Uso de variáveis de ambiente (.env) para proteção de chaves de API e configurações sensíveis.

Dashboard Executivo: Interface visual desenvolvida em Streamlit para acompanhamento de KPIs de estoque e taxas de sucesso da automação.

🤖 IA como Copiloto de Desenvolvimento
Este projeto foi desenvolvido utilizando Inteligência Artificial como Copiloto. A adoção desta tecnologia permitiu:

Aceleração da Prototipagem: Estruturação rápida do esqueleto do código e das integrações entre bibliotecas.

Segurança e Melhores Práticas: Garantia de implementação de padrões como ambientes virtuais (.venv) e tratamento de exceções robusto.

Foco no Negócio: A IA cuidou da sintaxe técnica, permitindo que eu focasse na lógica de validação de inventário e na experiência do usuário final no dashboard.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.14+

Manipulação de Dados: Pandas

Banco de Dados: SQLite (SQL)

Interface Visual: Streamlit

Segurança: Python-Dotenv

Logs: Logging (Nativo do Python)

📁 Estrutura do Projeto
main.py: Core da automação (lógica de sincronização e validação).

app.py: Interface do dashboard visual.

.env: Arquivo de configuração de ambiente (segurança).

automacao.log: Registro histórico de todas as execuções do sistema.

database_profissional.db: Banco de dados persistente do projeto.

⚙️ Como Executar
Instale as dependências:

Bash

pip install -r requirements.txt
Execute a automação:

Bash

python main.py
Inicie o Dashboard:

Bash

streamlit run app.py

Sobre a Autora
Simone Analista com sólida experiência em gestão administrativa e resolução de incidentes, agora aplicando engenharia de software para transformar processos manuais em fluxos digitais eficientes e seguros.
