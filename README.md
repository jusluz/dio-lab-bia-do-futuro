# Agente Financeiro com IA Generativa

Protótipo de um agente educador financeiro que usa IA para responder dúvidas sobre finanças pessoais com base em dados estruturados do cliente (perfil, transações, histórico e produtos).

## Status do projeto

Projeto finalizado como entrega do laboratório, com:

- aplicação funcional em Streamlit (`src/app.py`);
- base de conhecimento em CSV/JSON (`data/`);
- documentação principal do agente e prompts (`docs/01`, `docs/02`, `docs/03`).

## Funcionalidades implementadas

- interface de chat para interação com o usuário;
- montagem de contexto com dados do cliente;
- uso de modelo local via Ollama;
- regras de segurança no prompt (foco educacional, sem recomendação direta de investimento);
- tratamento de perguntas fora de escopo financeiro.

## Stack

- Python
- Streamlit
- Pandas
- Requests
- Ollama (LLM local)

## Estrutura do repositório

```text
dio-lab-bia-do-futuro/
├── README.md
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── src/
    ├── app.py
    └── README.md
```

## Como executar

1. Instale dependências:

```bash
pip install streamlit pandas requests
```

2. Inicie o Ollama:

```bash
ollama serve
```

3. Valide o endpoint:

```bash
curl http://localhost:11434/api/tags
```

4. Ajuste no `src/app.py`:

- `OLLAMA_URL` para `http://localhost:11434/api/generate`;
- `MODEL` para um modelo disponível localmente;
- caminhos dos arquivos de `data/` conforme os nomes reais do projeto.

5. Execute a aplicação:

```bash
streamlit run src/app.py
```

## Documentação complementar

- Definição do agente: `docs/01-documentacao-agente.md`
- Base de conhecimento: `docs/02-base-conhecimento.md`
- Prompt engineering e edge cases: `docs/03-prompts.md`
- Métricas e pitch: `docs/04-metricas.md` e `docs/05-pitch.md`

## Observações

Este projeto tem caráter educacional e não substitui orientação financeira profissional certificada.
