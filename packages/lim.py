import arrow

# Returns an inspirational message based on the current weekday
def display_weekday():
    # Get the current weekday name using Arrow
    current_weekday = arrow.now().format('dddd')  # e.g., "Monday"

    weekday_messages = {
        "Monday": "a fresh start begins with endless possibilities.",
        "Tuesday": "your effort today will yield results.",
        "Wednesday": "take it easy, success is approaching.",
        "Thursday": "trust your decisions and move forward with confidence.",
        "Friday": "believe in yourself, you are getting there.",
        "Saturday": "the weekend offers opportunities for growth.",
        "Sunday": "reflect and recharge, great things lie ahead.",
    }

    message = weekday_messages.get(current_weekday, "Have a great day!")
    daily_message = (f"As it is {current_weekday}, let this thought carry you"
                     f" through the day, {message}")

    return daily_message