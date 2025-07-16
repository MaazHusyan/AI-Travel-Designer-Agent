import openai
import os 
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Set Openrouter AI model
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")

def exploringAgent(user_interest: str):
    """
    Suggests interesting destinations based on user mood or interest.
    Returns a list of 3-4 city names with 1-line descriptions.
    """
    if not user_interest:
        return "Please describe your travel mood or interest."

    system_prompt = """
    You are a travel experience advisor. Based on user interest or mood, suggest 3 exciting international cities to visit.
    Include a one-line reason why each place matches the interest.
    Keep it short and travel-friendly.
    """

    response = openai.ChatCompletion.create(
        model=AI_MODEL,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"My travel mood is: {user_interest}"},
        ],
    )
    return response["choices"][0]["message"]["content"]