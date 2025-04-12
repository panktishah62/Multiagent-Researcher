# config.py
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from a .env file if it exists


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
# Use the latest flash model for speed and cost-effectiveness
GEMINI_MODEL = "gemini-1.5-flash-latest"

