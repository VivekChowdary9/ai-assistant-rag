import streamlit as st
from endee_store import EndeeStore
from retriever import Retriever
from llm import ChatGPT
from file_loader import load_file

st.set_page_config(page_title="AI Assistant (Endee RAG)", layout="centered")
st.title("🤖 AI Assistant using Endee (RAG)")

if "store" not in st.session_state:
    st.session_state.store = EndeeStore()

if "chat" not in st.session_state:
    st.session_state.chat = []

store = st.session_state.store
retriever = Retriever(store)
llm = ChatGPT()

uploaded_files = st.file_uploader(
    "📎 Upload files",
    type=["txt", "pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        text = load_file(file)
        chunks = text.split("\n")
        store.add_documents(chunks)
    st.success("Documents indexed using Endee")

query = st.text_input("Ask a question")

if query:
    docs = retriever.retrieve(query)
    context = "\n".join(docs)
    answer = llm.generate(query, context)
    st.session_state.chat.append((query, answer))

for q, a in st.session_state.chat:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**AI:** {a}")
