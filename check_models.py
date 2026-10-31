import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the same .env file
load_dotenv()

try:
    # Configure the API with your key
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)

    print("✅ API Key configured. Checking for available models...")

    # List all models and check for the one we need
    found_model = False
    for m in genai.list_models():
        print(f"Found model: {m.name}")
        if 'generateContent' in m.supported_generation_methods:
            if m.name == 'models/gemini-pro-vision':
                found_model = True

    print("-" * 20)
    if found_model:
        print("✅ SUCCESS: Your API key has access to 'gemini-pro-vision'.")
    else:
        print("❌ FAILURE: Your API key does NOT have access to 'gemini-pro-vision'.")
        print("➡️ Please ensure you have completed Step 1 (Billing Setup).")

except Exception as e:
    print(f"🔴 An error occurred while trying to list models: {e}")
    print("➡️ This strongly indicates a problem with your API Key or Google Cloud project setup.")