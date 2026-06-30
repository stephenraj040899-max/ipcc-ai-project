from google.cloud import bigquery
import vertexai
from vertexai.language_models import TextEmbeddingModel
import numpy as np

from config import PROJECT_ID, LOCATION, DATASET_ID, TABLE_ID

# Initialize Vertex AI
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION
)

embedding_model = TextEmbeddingModel.from_pretrained(
    "text-embedding-005"
)

client = bigquery.Client()


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


def search_documents(question, top_k=5):

    # Generate embedding for user question
    query_embedding = embedding_model.get_embeddings(
        [question]
    )[0].values

    table = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    query = f"""
    SELECT
        document_name,
        page,
        content,
        embedding
    FROM `{table}`
    WHERE embedding IS NOT NULL
    """

    rows = client.query(query).result()

    results = []

    for row in rows:

        score = cosine_similarity(
            query_embedding,
            row.embedding
        )

        results.append({
            "document": row.document_name,
            "page": row.page,
            "content": row.content,
            "score": score
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]