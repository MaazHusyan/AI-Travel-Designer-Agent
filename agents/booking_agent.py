from agent_base import Agent
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

class BookingAgent(Agent):
    def __init__(self):
        prompt = (
            "You are a booking assistant. Given a destination, date, and budget, "
            "use available data to describe a flight and hotel booking."
        )
        super().__init__(prompt)

    def run(self, destination, dates, budget):
        flights = get_flights(destination, dates)
        hotels = suggest_hotels(destination, budget)
        user_input = f"Destination: {destination}, Dates: {dates}, Budget: ${budget}\nFlights: {flights}\nHotels: {hotels}"
        return super().run(user_input)
