import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="MediBot — Dr. Aya Selmani",
    page_icon="✚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Lora:wght@500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #f7f9fc;
    color: #0d1f3c;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #dde4f0;
}

[data-testid="stChatMessage"] {
    background-color: #f0f5ff;
    border: 1px solid #dde4f0;
    border-radius: 14px;
    padding: 12px 16px;
}

[data-testid="stChatInput"] textarea {
    border-radius: 24px;
    border: 1.5px solid #dde4f0;
    background: #f7f9fc;
    font-family: 'DM Sans', sans-serif;
}

.stButton > button {
    background: transparent;
    border: 1px solid #dde4f0;
    color: #6b7fa3;
    border-radius: 20px;
    font-size: 12px;
    padding: 4px 14px;
    font-family: 'DM Sans', sans-serif;
}
.stButton > button:hover {
    border-color: #0098a6;
    color: #0098a6;
    background: #e6f7f9;
}

.warning-box {
    background: #fff8f0;
    border: 1px solid #fdd9b0;
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 12px;
    color: #a06020;
    margin: 6px 0;
}

.source-chip {
    display: inline-block;
    background: #e6f7f9;
    border: 1px solid #b3e8ee;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 11px;
    color: #0098a6;
    margin: 2px;
}
</style>
""", unsafe_allow_html=True)


# ── Dr. Sara SVG bitmoji ──────────────────────────────────────
DOCTOR_SVG = """
<svg viewBox="0 0 130 170" xmlns="http://www.w3.org/2000/svg" width="140" height="180">
  <circle cx="65" cy="38" r="26" fill="#FDDBB4"/>
  <path d="M39 38 Q39 12 65 12 Q91 12 91 38" fill="#3a2a1a"/>
  <path d="M39 38 Q36 30 40 26 Q38 42 39 50" fill="#3a2a1a"/>
  <path d="M91 38 Q94 30 90 26 Q92 42 91 50" fill="#3a2a1a"/>
  <ellipse cx="55" cy="42" rx="4" ry="5" fill="#F5C99A"/>
  <ellipse cx="75" cy="42" rx="4" ry="5" fill="#F5C99A"/>
  <circle cx="56" cy="41" r="2.5" fill="#4a3000"/>
  <circle cx="76" cy="41" r="2.5" fill="#4a3000"/>
  <circle cx="57" cy="40" r="1" fill="#fff"/>
  <circle cx="77" cy="40" r="1" fill="#fff"/>
  <path d="M58 50 Q65 55 72 50" stroke="#c0706a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M39 64 Q42 58 65 58 Q88 58 91 64 L96 130 Q65 138 34 130 Z" fill="#ffffff"/>
  <rect x="58" y="58" width="14" height="28" fill="#ffffff"/>
  <path d="M55 62 L75 62 L72 86 L65 90 L58 86 Z" fill="#e8f0fe"/>
  <path d="M62 68 L68 68" stroke="#0098a6" stroke-width="2" stroke-linecap="round"/>
  <path d="M65 65 L65 71" stroke="#0098a6" stroke-width="2" stroke-linecap="round"/>
  <rect x="56" y="86" width="18" height="10" rx="2" fill="#0098a6"/>
  <text x="65" y="94" text-anchor="middle" font-size="7" fill="#fff" font-family="sans-serif" font-weight="500">DOCTOR</text>
  <path d="M34 130 Q28 105 32 90 Q36 75 39 64" fill="#ffffff" stroke="#dde4f0" stroke-width="0.5"/>
  <path d="M96 130 Q102 105 98 90 Q94 75 91 64" fill="#ffffff" stroke="#dde4f0" stroke-width="0.5"/>
  <path d="M32 90 Q20 88 18 100 Q16 115 30 118" fill="none" stroke="#dde4f0" stroke-width="8" stroke-linecap="round"/>
  <path d="M98 90 Q110 88 112 100 Q114 115 100 118" fill="none" stroke="#dde4f0" stroke-width="8" stroke-linecap="round"/>
  <path d="M34 130 Q40 148 42 165 L52 165 L54 138 Q65 142 76 138 L78 165 L88 165 Q90 148 96 130" fill="#1a3560"/>
</svg>
"""


# ── Sidebar — Dr. Sara panel ──────────────────────────────────
with st.sidebar:
    st.markdown(DOCTOR_SVG, unsafe_allow_html=True)
    st.markdown("<h3 style='font-family:Lora,serif;margin:0;color:#0d1f3c'>Dr. Aya</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:12px;color:#6b7fa3;margin:2px 0 10px'>Medical AI Assistant</p>", unsafe_allow_html=True)
    st.divider()
    
    st.divider()
    st.markdown("**Suggested questions**")
    q1 = st.button("What is diabetes?", use_container_width=True)
    q2 = st.button("Symptoms of hypertension?", use_container_width=True)
    q3 = st.button("How is epilepsy treated?", use_container_width=True)
    q4 = st.button("What causes migraines?", use_container_width=True)
    st.divider()
    st.markdown('<div class="warning-box">For emergencies call your local emergency number immediately.</div>', unsafe_allow_html=True)


# ── Main area ─────────────────────────────────────────────────
st.markdown("<h2 style='font-family:Lora,serif;color:#0d1f3c;margin-bottom:4px'>Dr. Aya — Medical Assistant</h2>", unsafe_allow_html=True)
st.markdown('<div class="warning-box">MediBot provides general medical information only. Always consult a licensed healthcare professional for diagnosis and treatment.</div>', unsafe_allow_html=True)


@st.cache_resource
def load_chain():
    from langchain_groq import ChatGroq
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_pinecone import PineconeVectorStore
    from langchain_huggingface import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = PineconeVectorStore(index_name=os.getenv("PINECONE_INDEX","medicalbot"), embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(model="moonshotai/kimi-k2-instruct-0905", api_key=os.environ["Grok_API"], temperature=0.3)

    system_prompt = (
        "You are Dr. Aya, an expert medical AI assistant. "
        "Answer based ONLY on the retrieved context. "
        "If insufficient, say: 'I don't have enough information. Please consult a physician.' "
        "Structure: definition → causes → symptoms → treatment. "
        "Be clear, concise, and professional.\n\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    return create_retrieval_chain(retriever, create_stuff_documents_chain(llm, prompt))


# ── Session & chat ────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hello! I'm **Dr. Aya**, your medical information assistant. I can help you understand diseases, symptoms, medications, and treatments based on verified medical literature.\n\nWhat would you like to know today?"
    }]
    

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

quick_q = None
if q1: quick_q = "What is diabetes?"
if q2: quick_q = "What are the symptoms of hypertension?"
if q3: quick_q = "How is epilepsy treated?"
if q4: quick_q = "What causes migraines?"

user_input = st.chat_input("Ask Dr. Aya a medical question...") or quick_q

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Dr. Aya is reviewing your question..."):
            try:
                rag_chain = load_chain()
                result = rag_chain.invoke({"input": user_input})
                answer = result["answer"]
                sources = list({doc.metadata.get("source", "") for doc in result.get("context", []) if doc.metadata.get("source")})

                st.markdown(answer)
                if sources:
                    chips = " ".join(f'<span class="source-chip">{s}</span>' for s in sources[:3])
                    st.markdown(f"**Sources:** {chips}", unsafe_allow_html=True)
                st.markdown('<div class="warning-box">This is for informational purposes only — not a substitute for professional medical advice.</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {str(e)}")
                answer = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": answer})