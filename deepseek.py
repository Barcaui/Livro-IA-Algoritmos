import streamlit as st
from langchain_ollama import ChatOllama

llm = ChatOllama(model='deepseek-r1:1.5b', base_url="http://localhost:11434")
st.set_page_config(page_title='Chat with BARCAUI', layout='centered')
st.title('Talk to me - BARCAUI DeepSeek')

if "mensagens" not in st.session_state:
    st.session_state['mensagens'] = []

mensagens = st.session_state['mensagens']
for tipo, conteudo in mensagens:
    chat = st.chat_message(tipo)
    chat.markdown(conteudo)

prompt = st.chat_input('Tell me what you want to know...')

if prompt:
    mensagens.append(('human', prompt))

    chat = st.chat_message('human')
    chat.markdown(prompt)

    resposta = llm.invoke(prompt).content
    mensagens.append(('ai', resposta))

    chat = st.chat_message('ai')
    chat.markdown(resposta)
