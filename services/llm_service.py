from google import genai

from config import (
    PROJECT_ID,
    LOCATION,
    GEMINI_MODEL,
)

# ----------------------------------------
# Create GenAI Client
# ----------------------------------------

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

# ----------------------------------------
# Generate response
# ----------------------------------------

def generate_response(prompt: str) -> str:
    """
    Generate a response using Gemini.
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text