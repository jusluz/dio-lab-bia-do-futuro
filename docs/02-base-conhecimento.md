# Base de Conhecimento

## Dados Utilizados

Arquivos da pasta `data` usados pelo agente:

| Arquivo | Formato | Utilização no Agente | Status |
|---------|---------|----------------------|--------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores do cliente | Usado |
| `perfil_investidor.json` | JSON | Personalizar explicações e recomendações por perfil | Usado |
| `produtos_financeiros.json` | JSON | Filtrar e sugerir produtos adequados ao perfil | Usado |
| `transacoes.csv` | CSV | Analisar padrão de gastos para apoiar recomendações | Usado |


---

## Adaptações nos Dados

No arquivo `produtos_financeiros.json`, foi adicionado o produto **FII XP Malls** como opção de renda variável.

- **Motivo:** incluir um exemplo de fundo imobiliário no catálogo.
- **Impacto esperado:** ampliar recomendações para perfis moderados/arrojados com foco em renda passiva e diversificação.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos são carregados via código no início da execução (etapa de inicialização), antes da montagem do prompt.

```python
import json
import pandas as pd

historico_atendimento = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")

with open("data/perfil_investidor.json", encoding="utf-8") as f:
    perfil_investidor = json.load(f)
with open("data/produtos_financeiros.json", encoding="utf-8") as f:
    produtos_financeiros = json.load(f)
```

### Como os dados são usados no prompt?
Os dados são carregados em memória e consultados dinamicamente.  
No `system prompt` ficam apenas regras de conduta; os dados do cliente e produtos entram no prompt de usuário em formato resumido.

```text
Contexto do cliente:
- Perfil de investidor: <conservador/moderado/arrojado>
- Objetivo principal: <objetivo>
- Patrimônio e reserva de emergência: <valores>

Resumo financeiro:
- Receitas e despesas por categoria (último período)
- Padrões relevantes de consumo

Produtos elegíveis:
- Lista filtrada por perfil, risco e liquidez
```

---

## Exemplo de Contexto Montado

Exemplo de contexto enviado ao agente:

```
Cliente: Maria, perfil moderado, objetivo de aposentadoria em 20 anos.
Patrimônio: R$ 120.000 | Reserva de emergência: R$ 15.000.
Capacidade de aporte mensal: R$ 1.500.

Resumo de gastos mensais:
- Moradia: R$ 1.200
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188

Produtos sugeridos (compatíveis com perfil moderado):
1. Tesouro Selic 2025 (liquidez diária, baixo risco) para reserva.
2. Fundo Multimercado XP Capital (risco médio) para diversificação.
3. FII XP Malls (risco médio) para exposição imobiliária e renda recorrente.
```

---

## Checklist de Completude

- [x] Fontes de dados listadas
- [x] Adaptações nos dados descritas
- [x] Estratégia de integração explicada
- [x] Exemplo real de contexto inserido
