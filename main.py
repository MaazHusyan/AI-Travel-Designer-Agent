from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def main():
    mood = input("🧠 What's your travel mood? (relax, adventure, romantic, culture): ")
    dates = input("📅 Enter your travel dates (e.g., 2025-08-10 to 2025-08-20): ")
    budget = input("💸 What's your hotel budget per night (USD)? ")

    print("\n🎯 Finding the perfect destination...")
    dest_agent = DestinationAgent()
    destination = dest_agent.run(mood).strip()
    print(f"🌍 Destination Suggested: {destination}")

    print("\n🛫 Planning Flights and Hotels...")
    book_agent = BookingAgent()
    booking = book_agent.run(destination, dates, budget).strip()

    # Optional: try splitting booking string if needed
    print("\n📦 Booking Summary:")
    print(booking)

    print("\n🗺 Exploring fun stuff to do...")
    exp_agent = ExploreAgent()
    explore = exp_agent.run(destination).strip()

    print("\n🎉 Final Travel Plan")
    print("==========================")
    print(f"🌍 Destination: {destination}")
    print(f"📅 Dates: {dates}")
    print(f"💰 Budget: ${budget}/night")
    print("\n✈️ Flights & Hotels:\n" + booking)
    print("\n🍽️ Things to Explore:\n" + explore)
    print("==========================")
    print("✅ Trip designed successfully!")

if __name__ == "__main__":
    main()
