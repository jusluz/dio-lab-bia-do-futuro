# Código da Aplicação (`src/`)

Este diretório contém a aplicação do agente financeiro em Streamlit.

## Estrutura atual

```text
src/
└── app.py    # Interface, contexto e chamada ao modelo local (Ollama)
```

## Pré-requisitos

- Python 3.10+
- Ollama instalado e em execução
- Modelo disponível no Ollama (ex.: `gemma4:e4b`)

## Dependências Python

Como não há `requirements.txt` no projeto, instale manualmente:

```bash
pip install streamlit pandas requests
```

## Como executar

No diretório raiz do projeto:

```bash
streamlit run src/app.py
```

Ou dentro de `src/`:

```bash
streamlit run app.py
```

## Configuração rápida

No arquivo `app.py`, revise:

- `OLLAMA_URL`: URL do endpoint de geração (ex.: `http://localhost:<port>/api/generate`)
- `MODEL`: nome do modelo disponível localmente

### Como obter o endpoint do Ollama

1. Inicie o serviço do Ollama:

```bash
ollama serve
```

2. Em outro terminal, valide se a API está ativa:

```bash
curl http://localhost:11434/api/tags
```

Se retornar JSON com a lista de modelos, o endpoint base é:

```text
http://localhost:11434
```

Para este projeto, use no `OLLAMA_URL`:

```text
http://localhost:11434/api/generate
```

## Base de dados esperada

A base oficial do projeto está em `data/`:

- `historico_atendimento.csv`
- `perfil_investidor.json`
- `produtos_financeiros.json`
- `transacoes.csv`

> Observação: se o `app.py` estiver apontando para nomes diferentes (como `perfil.json` e `produtos.json`), ajuste os caminhos para os arquivos acima.

## Boas práticas recomendadas

- Não versionar chaves/tokens no código.
- Manter mensagens do sistema curtas e objetivas para reduzir custo de contexto.
- Tratar erros de conexão com Ollama e de leitura dos arquivos de dados.
