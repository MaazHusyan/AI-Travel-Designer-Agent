from agent_base import Agent

class DestinationAgent(Agent):
    def __init__(self):
        prompt = (
            "You are a travel advisor. Based on the user's mood or interest, "
            "suggest the best travel destination. Keep the answer short."
        )
        super().__init__(prompt)