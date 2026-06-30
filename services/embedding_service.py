import vertexai
from vertexai.language_models import TextEmbeddingModel

from config import (
    PROJECT_ID,
    LOCATION,
    EMBEDDING_MODEL,
)

# ----------------------------------------
# Initialize Vertex AI once
# ----------------------------------------

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

# ----------------------------------------
# Load embedding model once
# ----------------------------------------

model = TextEmbeddingModel.from_pretrained(
    EMBEDDING_MODEL
)


# ----------------------------------------
# Generate embedding for one text
# ----------------------------------------

def get_embedding(text: str) -> list[float]:
    """
    Returns embedding for a single text.
    """

    response = model.get_embeddings([text])

    return response[0].values


# ----------------------------------------
# Generate embeddings for multiple texts
# ----------------------------------------

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Returns embeddings for multiple texts.
    """

    response = model.get_embeddings(texts)

    return [embedding.values for embedding in response]