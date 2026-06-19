from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_response(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text