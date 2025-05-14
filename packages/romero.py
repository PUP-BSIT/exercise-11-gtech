import datetime  

def get_current_time():    
    # Get the current local time (as a time object)
    current_time = datetime.datetime.now().time()
    
    # Extract the hour component from the current time
    hour = current_time.hour

    # Determine the message based on the current hour
    if 1 <= hour < 12:
        message = "Good morning! Embrace the moment, your time has come."
    elif 12 <= hour < 17:
        message = "Good afternoon! It's the right time to take action."
    elif 17 <= hour < 21:
        message = "Good evening! The time is ripe for new beginnings."
    else:
        message = "Good night! Patience is your virtue at this hour."

    # Return the current time (as a time object)

    return message, current_time
