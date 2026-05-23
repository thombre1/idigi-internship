from google import genai
from google.genai import types

client = genai.Client()

# Initialize the Google Search tool
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool],
    temperature=0.1,
    system_instruction="Talk in very sophisticated English like a distinguished gentleman, if you know about the IRON MAN movies, please talk like J.A.R.V.I.S."
)

userInput = input("Ask: ")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", # Or gemini-3.5-flash
    contents=userInput,
    config=config,
)

print(response.text)

