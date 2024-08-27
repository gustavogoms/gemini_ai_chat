import google.generativeai as genai
from key import key

genai.configure(api_key= key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Qual o sentido da vida?")

print(response.text)