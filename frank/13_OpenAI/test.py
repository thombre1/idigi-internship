import numpy as np
from google import genai
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the modern genai client
client = genai.Client()

def get_embedding(text: str):
    """Fetches a clean 1D numpy array vector for a single string."""
    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    # response.embeddings.values contains the full list of floating-point numbers
    return np.array(response.embeddings[0].values).reshape(1, -1)

# 1. Fetch individual embeddings safely
potato_vec = get_embedding("potato")
rhubarb_vec = get_embedding("potato")
enterprise_vec = get_embedding("The starship Enterprise")

# 2. Calculate Standardized Cosine Similarity
score_vegetable = cosine_similarity(potato_vec, rhubarb_vec)[0][0]
score_sci_fi = cosine_similarity(potato_vec, enterprise_vec)[0][0]

# 3. Print clean scores
print(f"Similarity (potato vs potato): {score_vegetable:.4f}")
print(f"Similarity (potato vs Enterprise): {score_sci_fi:.4f}")

