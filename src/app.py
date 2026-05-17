import json
import pandas as pd
import requests
import streamlit as st

# ================== Definições ==================
OLLAMA_URL = "http://localhost:<example_port>/api/generate"
MODEL = "gemma4:e4b"

# ================== Carregar dados ==================
perfil = json.load(open("data/perfil.json"))
transacoes = pd.read_csv("data/transacoes.csv")
historico = pd.read_csv("data/transacoes.csv")
produtos = json.load(open("data/produtos.json"))

# ================== Montar contexto ==================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia']}

TRANSAÇÔES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

# ================== SYSTEM PROMPT ==================
SYSTEM_PROMPT = """

## PERSONA
Você é um educador financeiro, especializado em finanças pessoais e investimentos.

## OBJETIVO
Ajudar os usuários a entenderem melhor seus gastos e a fazerem investimentos de acordo com o seu perfil.

## REGRAS
- Use os dados fornecidos sempre que possível para responder às perguntas.
- NUNCA recomende investimentos específicos; apenas simule cenários com base no perfil do usuário e explique como funcionam.
- Caso não saiba algo, admita e ofereça alternativas: "Não tenho essa informação, mas posso ajudar com [...]".
- Mantenha sempre um tom de voz amigável e acessível.
- Seja objetivo e claro em suas respostas com uma linguagem simples e objetiva.
- Sempre questione o entendimento do cliente.
- JAMAIS responda perguntas que não tenham relação com finanças pessoais e investimentos, quando ocorrer, 
deixe claro que voce é um educador financeiro e que só poderá auxiliar com informações relacionadas ao escopo.
"""

# ================== CHAMAR OLLAMA ==================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO:
    {contexto}

    Pergunta:
    {msg}"""

    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    
    return r.json()['response']

# ============= Interface =============
st.title("Educador financeiro")

if pergunta := st.text_input("Sua duvida sobre finanças: "):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))