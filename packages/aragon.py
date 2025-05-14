import random 

def generate_number():
    # Generate a random integer between 1 and 99 
    lucky_number = random.randint(1,99)
    # Message incorporating the generated number
    number_message = ("Your journey today is guided by the lucky number"
                      f" {lucky_number}.")
    
    return number_message