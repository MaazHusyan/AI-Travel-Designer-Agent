# agents/travel_designer.py
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

class TravelDesignerAgent:
    def __init__(self):
        self.destination_agent = DestinationAgent()
        self.booking_agent = BookingAgent()
        self.explore_agent = ExploreAgent()

    def plan_trip(self, mood_or_interest: str):
        destination = self.destination_agent.suggest_destination(mood_or_interest)
        flights, hotels = self.booking_agent.get_flights_and_hotels(destination)
        attractions, food = self.explore_agent.suggest_experiences(destination)

        return {
            "destination": destination,
            "flights": flights,
            "hotels": hotels,
            "attractions": attractions,
            "food": food
        }
