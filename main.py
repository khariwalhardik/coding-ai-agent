import os
import dotenv
from google import genai

dotenv.load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how to find the loop in linked list in python"
)
print(response.text)
