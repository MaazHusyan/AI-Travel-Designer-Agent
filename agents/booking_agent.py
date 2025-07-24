# agents/booking_agent.py
import json

class BookingAgent:
    def get_flights_and_hotels(self, destination):
        with open("mock_data/flights_hotels.json") as f:
            data = json.load(f)
        return (
            data["flights"].get(destination, ["Mock Flight 1", "Mock Flight 2"]),
            data["hotels"].get(destination, ["Mock Hotel 1", "Mock Hotel 2"])
        )
