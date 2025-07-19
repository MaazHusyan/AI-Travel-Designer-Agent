from agent_base import Agent

class ExploreAgent(Agent):
    def __init__(self):
        prompt = (
            "You are a cultural guide. Given a city, suggest popular attractions, food, and fun things to do."
        )
        super().__init__(prompt)
