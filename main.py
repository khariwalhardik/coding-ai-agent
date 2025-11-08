import os
# import dotenv
# import sys
# import httpx
# from google import genai
'''
dotenv.load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")


print(sys.argv)
client = genai.Client(api_key=api_key)
verbose_flag=False
if len(sys.argv) < 2:
    print("I need a prompt!")
    sys.exit(1)

elif len(sys.argv)==3 and sys.argv[2]=="--verbose":
    verbose_flag=True
prompt = sys.argv[1]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt],
    )
print(response.text)
if(verbose_flag):
    print("prompt token usage:", response.usage_metadata.prompt_token_count)
    print("thought token usage:", response.usage_metadata.thoughts_token_count)
    print("completion token usage:", response.usage_metadata.total_token_count)

'''
from tools.get_file_info import get_file_info
print(get_file_info("calculator","src"))

from tools.get_file_content import get_file_content

print(get_file_content("calculator","service.py"))

from tools.write_file import write_file
print(write_file("calculator","new_dir/new_file.txt","Hello, World!"))

from tools.run_file import run_python_file
print(run_python_file("calculator","app.py"))