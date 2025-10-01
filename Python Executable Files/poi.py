import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# List available models
for model in genai.list_models():
    print(model.name, "->", model.supported_generation_methods)
