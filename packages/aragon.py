import secrets 

def generate_number():
    # Generate a secure random integer between 1 and 99 
    lucky_number = secrets.randbelow(99) + 1
    # Message incorporating the generated number
    number_message = (" Your journey today is guided by the lucky number"
                      f" {lucky_number}.")
    
    return number_message