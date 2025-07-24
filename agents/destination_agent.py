# agents/destination_agent.py

class DestinationAgent:
    def suggest_destination(self, mood):
        mood_map = {
            "romantic": "Paris",
            "adventure": "Queenstown",
            "beach": "Maldives",
            "history": "Rome",
            "nature": "Kyoto"
        }
        return mood_map.get(mood.lower(), "Bali")
