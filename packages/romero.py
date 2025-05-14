import pendulum

def get_current_time():
    # Get the current local time using Pendulum
    now = pendulum.now()
    hour = now.hour

    # Determine the message based on the current hour
    if 1 <= hour < 12:
        message = "Good morning! Embrace the moment, your time has come."
    elif 12 <= hour < 17:
        message = "Good afternoon! It's the right time to take action."
    elif 17 <= hour < 21:
        message = "Good evening! The time is ripe for new beginnings."
    else:
        message = "Good night! Patience is your virtue at this hour."

    # Format the time in a friendly string
    time_message = f"The current time is: {now.format('HH:mm:ss')}\n\n{message}"
    
    return time_message
