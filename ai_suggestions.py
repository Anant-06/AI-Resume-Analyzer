from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key) if api_key else None


def generate_suggestions(text):

    if client is None:
        return "Error: GEMINI_API_KEY is missing from the .env file."

    prompt = f"""
    Analyze this resume and provide:

    1. Missing skills
    2. Resume improvements
    3. ATS optimization tips
    4. Suggested projects
    5. Career recommendations

    Resume:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text or "No suggestions generated."

    except Exception as e:
        return f"Error generating AI suggestions: {e}"
