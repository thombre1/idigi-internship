from google import genai
from google.genai import types
import time

client = genai.Client()


config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())],
    system_instruction="Answer things formally and with brevity. A little bit smart humour will be appreciated",
)
chat = client.chats.create(model="gemini-2.5-flash", config=config)

while True:
    try:
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit"]:
            print("Goodbye, Sir.")
            break

        if not userInput.strip():
            continue

        response = chat.send_message(userInput)
        print(f"\nSky: {response.text}")

    except Exception as err:
        if "429" in str(err):
            print("Try Again, Sir.")

        else:
            print(f"err: {err}")

