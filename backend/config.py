import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_TITLE = "HOME-TAKER API"
API_VERSION = "1.0.0"

# CORS Configuration
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
]

# OpenAI Configuration
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = "gpt-4o"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 500

# Data Storage Configuration
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
PREFERENCES_FILE = DATA_DIR / "preferences.json"
