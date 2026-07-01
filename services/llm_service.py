import vertexai
from vertexai.generative_models import GenerativeModel

from config import PROJECT_ID, LOCATION, GEMINI_MODEL
from services.prompt_loader import load_prompt
from services.retrieval_service import retrieve_context

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

model = GenerativeModel(GEMINI_MODEL)

qa_prompt = load_prompt("qa_prompt.txt")


def build_context(contexts):
    context_text = ""

    for i, item in enumerate(contexts, start=1):
        context_text += (
            f"\nSource {i}\n"
            f"Document: {item['document']}\n"
            f"Chunk: {item['chunk']}\n\n"
            f"{item['content']}\n\n"
        )

    return context_text


def ask_question_with_sources(question: str):
    contexts = retrieve_context(question)

    context_text = build_context(contexts)

    prompt = (
        qa_prompt
        .replace("{context}", context_text)
        .replace("{question}", question)
    )

    response = model.generate_content(prompt)

    return response.text, contexts


def ask_question(question: str):
    answer, _ = ask_question_with_sources(question)
    return answer