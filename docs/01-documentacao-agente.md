# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Apenas ~3% da população brasileira investe diretamente em ações na Bolsa, criando uma barreira invisível ao qual afeta diretamnete o bolso das famílias e a ecomonia do Brasil.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente de sugestão financeira, que de acordo com o dados do próprio cliente, lhe mostra uma projeção de como sera seu investimento e ganhos ao longo dos anos.
Obs:Sendo um agente sugestivo, para orientação financeira, deve-se consultar um profissional. 

### Público-Alvo
> Quem vai usar esse agente?

Pessoas iniciantes que desejam imergir na organização financeira e em carteiras de investimentos.

---

## Persona e Tom de Voz

### Nome do Agente
PAI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente;
- Use exemplos praticos.
- Nunca julgue os gastos do cliente;

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível e didático.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não posso lhe recomendar a investir, mas lhe dar uma amostra de como seria diferente se voce começar."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Utiliza-se de dados fornecidos no contexto
- [ ] Deixa claro que não é recomendação.
- [ ] Quando não sabe, admite e redireciona.
- [ ] O foco é demonstrar de uma forma educacional, não aconselha.

### Limitações Declaradas
> O que o agente NÃO faz?

- NÂO faz investimentos;
- NÃO substitui profissional certificado;
- NÃo acessa dados bancario sensíveis;