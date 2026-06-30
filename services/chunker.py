def chunk_text(text, chunk_size=1000):
    """
    Split text into chunks of approximately
    1000 characters.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start = end

    return chunks