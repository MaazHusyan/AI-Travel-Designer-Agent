# main.py
from agents.travel_designer import TravelDesignerAgent

def main():
    agent = TravelDesignerAgent()
    mood = input("What's your travel mood (romantic, adventure, beach, etc.)? ")
    plan = agent.plan_trip(mood)

    print(f"\n🌍 Destination: {plan['destination']}")
    print("✈️ Flights:", ", ".join(plan['flights']))
    print("🏨 Hotels:", ", ".join(plan['hotels']))
    print("🗺️ Attractions:", ", ".join(plan['attractions']))
    print("🍽️ Food:", ", ".join(plan['food']))

if __name__ == "__main__":
    main()
