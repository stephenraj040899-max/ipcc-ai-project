import os
import sys
import base64

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

import streamlit as st

from services.llm_service import ask_question_with_sources
from services.document_service import get_documents, get_pdf_base64, get_document_text
from services.summary_service import summarize_document
from services.review_service import review_document
from services.improvement_service import improve_document


st.set_page_config(
    page_title="IPCC Climate AI",
    page_icon="🌍",
    layout="wide",
)

documents = get_documents()


def document_selector(label="Choose a document"):
    return st.selectbox(
        label,
        documents,
        format_func=lambda x: x["display"],
    )


st.sidebar.title("🌍 IPCC Climate AI")
st.sidebar.caption("Climate report assistant powered by BigQuery Vector Search and Gemini.")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "💬 Ask Questions",
        "📚 Browse Documents",
        "📄 Summarize Document",
        "📝 Review Document",
        "💡 Improvement Suggestions",
        "ℹ️ About",
    ],
)

st.title("🌍 IPCC Climate AI Assistant")


if page == "🏠 Dashboard":
    st.subheader("📊 Project Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Documents", len(documents))
    col2.metric("Text Chunks", sum(doc["chunks"] for doc in documents))
    col3.metric("PDF Size", f"{round(sum(doc['size_mb'] for doc in documents), 2)} MB")

    st.divider()
    st.subheader("📚 Available Reports")

    for doc in documents:
        with st.container(border=True):
            st.markdown(f"### 📄 {doc['display']}")
            c1, c2 = st.columns(2)
            c1.write(f"**Chunks:** {doc['chunks']}")
            c2.write(f"**Size:** {doc['size_mb']} MB")


elif page == "💬 Ask Questions":
    st.subheader("💬 Ask the IPCC AI")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_area(
        "Enter your question",
        height=120,
        placeholder="Example: How can cities reduce greenhouse gas emissions?",
    )

    c1, c2 = st.columns([3, 1])

    with c1:
        ask_clicked = st.button("🚀 Ask AI", use_container_width=True)

    with c2:
        clear_clicked = st.button("🧹 Clear Chat", use_container_width=True)

    if clear_clicked:
        st.session_state.chat_history = []
        st.rerun()

    if ask_clicked:
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Searching IPCC reports and generating answer..."):
                answer, sources = ask_question_with_sources(question)

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer,
                    "sources": sources,
                }
            )

    for item in reversed(st.session_state.chat_history):
        with st.container(border=True):
            st.markdown("### 🧑 Question")
            st.markdown(item["question"])

            st.markdown("### 🤖 Answer")
            st.markdown(item["answer"])

            with st.expander("📚 Sources Used"):
                for source in item["sources"]:
                    st.markdown(
                        f"**{source['document']} — Chunk {source['chunk']}**"
                    )
                    st.caption(f"Distance: {source['distance']}")
                    st.write(source["content"])
                    st.divider()


elif page == "📚 Browse Documents":
    st.subheader("📚 Browse Original IPCC PDFs")

    selected = document_selector()

    st.info(f"Chunks: {selected['chunks']} | Size: {selected['size_mb']} MB")

    with st.spinner("Preparing PDF..."):
        pdf_base64 = get_pdf_base64(selected["real"])

    pdf_bytes = base64.b64decode(pdf_base64)

    st.download_button(
        label="⬇️ Download / Open Original PDF",
        data=pdf_bytes,
        file_name=selected["real"],
        mime="application/pdf",
        use_container_width=True,
    )


elif page == "📄 Summarize Document":
    st.subheader("📄 Summarize Document")

    selected = document_selector("Select a report to summarize")

    if st.button("📄 Generate Summary", use_container_width=True):
        with st.spinner("Reading document and generating summary..."):
            text = get_document_text(selected["real"])
            summary = summarize_document(text)

        st.subheader("📌 Summary")
        st.markdown(summary)


elif page == "📝 Review Document":
    st.subheader("📝 Review Document")

    selected = document_selector("Select a report to review")

    if st.button("📝 Generate Review", use_container_width=True):
        with st.spinner("Reviewing document..."):
            text = get_document_text(selected["real"])
            review = review_document(text)

        st.subheader("📋 AI Review")
        st.markdown(review)


elif page == "💡 Improvement Suggestions":
    st.subheader("💡 Improvement Suggestions")

    selected = document_selector("Select a report for improvement suggestions")

    if st.button("💡 Generate Suggestions", use_container_width=True):
        with st.spinner("Analyzing document and preparing suggestions..."):
            text = get_document_text(selected["real"])
            suggestions = improve_document(text)

        st.subheader("✨ Suggestions")
        st.markdown(suggestions)


elif page == "ℹ️ About":
    st.subheader("ℹ️ About This Project")

    st.markdown(
        """
This application is an AI-powered IPCC report assistant.

It supports:

- 💬 Question answering using RAG
- 📚 Original PDF browsing
- 📄 Document summaries
- 📝 AI document reviews
- 💡 Improvement suggestions

Technologies used:

- Google Cloud Storage
- BigQuery
- BigQuery Vector Search
- Vertex AI Embeddings
- Gemini
- Streamlit
"""
    )