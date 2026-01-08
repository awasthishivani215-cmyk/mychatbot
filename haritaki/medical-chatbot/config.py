# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GPT_MODEL = "gpt-3.5-turbo"

    # Paths
    PATIENT_RECORDS_PATH = "patient_records"
    REPORT_PATH = "reports"

    # App
    SECRET_KEY = os.getenv("SECRET_KEY", "medical-chatbot-secret-key-2024")
    DEBUG = False

    # Chatbot
    MAX_SYMPTOMS = 10
    MIN_SYMPTOMS = 1
    MAX_CONVERSATION_HISTORY = 20
