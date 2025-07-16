def bookingAgent(destination: str, tools: dict) -> str:
    """
    Handles the booking phase using dynamic tools.
    Returns flight and hotel options for the given destination.
    """

    if not destination:
        return "Please select a destination to proceed with bookings."

    response = []

    if "get_flights" in tools:
        response.append("✈️ Flights:\n" + tools["get_flights"](destination))
    else:
        response.append("❌ Flight tool not available.")

    if "suggest_hotels" in tools:
        response.append("\n🏨 Hotels:\n" + tools["suggest_hotels"](destination))
    else:
        response.append("❌ Hotel tool not available.")

    return "\n".join(response)
