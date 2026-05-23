import os
import io
from google import genai
from google.genai import types
from PIL import Image

# Initialize the SDK client
client = genai.Client()

prompt_text = "A futuristic cyberpunk cityscape at sunset with flying vehicles, highly detailed digital art"

print("Generating image via Gemini generate_content endpoint...")

# CORRECT METHOD: Use generate_content for multimodal image output
response = client.models.generate_content(
    model='gemini-3.1-flash-image-preview',
    contents=prompt_text,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="1:1"
        )
    )
)

# Extract and save the generated image from response parts
image_found = False
for part in response.parts:
    # Check if the part contains inline image data
    if part.inline_data:
        # Use the SDK's built-in image conversion helper
        generated_image = part.as_image()
        generated_image.save("cyberpunk_city.jpg")
        print("Success! Image saved as 'cyberpunk_city.jpg'.")
        image_found = True
        break

if not image_found:
    print("No image data found in the response. Check API console logs.")

