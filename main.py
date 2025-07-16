# basic imports
import openai
import os
from dotenv import load_dotenv
# importing the agents
from agents.explore_agent import exploringAgent
from agents.destination_agent import destinationAgent


# Load environment variables from .env file
load_dotenv()   

# Set Openrouter AI model
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL")
openai.api_key = os.getenv("OPEN_ROUTER_API_KEY")


def travelAssistant():
    print("Welcome to the Travel Assistant!")
    # Step 1: ExploreAgent - suggest destinations
    interest = input("What is your travel mood or interest? ")
    destinations = exploringAgent(interest)
    print("Suggested Destinations:")
    print(destinations)
    
if __name__ == "__main__":
    travelAssistant()