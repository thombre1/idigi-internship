from google import genai
import numpy as np

client = genai.Client()
result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the cheatcode for easy life?"
)

print(result.embeddings)

# Check embeddings
response = client.models.embed_content(
    model="gemini-embedding-2",
    contents=["potato", "rhubarb"]
)

potato = response.embeddings[0].values
rhubarb = response.embeddings[1].values

simScore = np.dot(potato, rhubarb)
print(str(simScore))

# Check embeddings
response = client.models.embed_content(
    model="gemini-embedding-2",
    contents=["potato", "The starship Enterprise"]
)

potato = response.embeddings[0].values[0]
enterprise = response.embeddings[0].values[1]

simScore = np.dot(potato, enterprise)
print(str(simScore))
