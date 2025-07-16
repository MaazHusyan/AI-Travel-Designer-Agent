import openai
import os
from dotenv import load_dotenv

load_dotenv()
# Set Openrouter AI model
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")

def destinationAgent(city_name: str) -> str:
    """
    Accepts a city name and returns a short travel description or confirmation.
    """
    if not city_name:
        return "Please enter a destination to continue."

    system_prompt = """
    You are a smart travel guide. When a city name is selected, respond with a short 2-3 line message that:
    - Confirms the choice
    - Highlights 1 unique cultural or travel-friendly aspect of the city
    """

    response = openai.ChatCompletion.create(
        model=AI_MODEL,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"My chosen destination is: {city_name}"}
        ]
    )

    return response["choices"][0]["message"]["content"]
