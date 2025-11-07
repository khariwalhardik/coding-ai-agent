import os
import dotenv
from google import genai
from google.genai import types
from PIL import Image
dotenv.load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain linked list in few words"
# )
# print(response.text)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="How does AI work in few words?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=1) # Disables thinking
#     ),
# )
# print(response.text)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a cat. Your name is Neko."),
#     contents="Hello there"
# )

# print(response.text)



# image = Image.open("organ.png")
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=[image, "Tell me about this instrument"]
# )
# print(response.text)



# response = client.models.generate_content_stream(
#     model="gemini-2.5-flash",
#     contents=["Explain how AI works"]
# )
# for chunk in response:
#     print(chunk.text, end="")


from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

# Retrieve and upload both PDFs using the File API
doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_pdf_1, sample_pdf_2, prompt])
print(response.text)
print("prompt token usage:", response.token_usage.prompt_tokens)
print("completion token usage:", response.token_usage.completion_tokens)