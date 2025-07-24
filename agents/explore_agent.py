# agents/explore_agent.py

class ExploreAgent:
    def suggest_experiences(self, destination):
        suggestions = {
            "Paris": (["Eiffel Tower", "Louvre"], ["Croissants", "Macarons"]),
            "Queenstown": (["Bungee Jumping", "Lake Wakatipu"], ["Fergburger"]),
            "Maldives": (["Snorkeling", "Resort Spa"], ["Seafood BBQ"]),
            "Rome": (["Colosseum", "Pantheon"], ["Pizza", "Pasta"]),
            "Kyoto": (["Fushimi Inari", "Bamboo Grove"], ["Ramen", "Matcha Ice Cream"])
        }
        return suggestions.get(destination, (["Explore town"], ["Local food"]))
