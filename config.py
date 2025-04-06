import os
import logging
from dotenv import load_dotenv
import openai
import google.generativeai as genai

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar OpenAI API
api_key = os.getenv('API_KEY')
if not api_key:
    logging.error("API key not found. Please set the API_KEY environment variable.")
    raise ValueError("API key not found. Please set the API_KEY environment variable.")
openai.api_key = api_key
logging.info("OpenAI API key configured successfully.")

# Configurar Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    logging.warning("Gemini API key not found. Some features may not work.")
else:
    genai.configure(api_key=gemini_api_key)
    logging.info("Gemini API key configured successfully.")
