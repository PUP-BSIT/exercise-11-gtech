from quote_inspire_jokes.inspire import get_inspiration
from quote_inspire_jokes.quote import get_quote
from quote_inspire_jokes.joke import get_joke
import random

def generate_inspiration():
    inspiration = (f"For a dose of inspiration, here’s your lucky quote"
             f" of the day: {get_inspiration()}")

    return inspiration

def generate_quote():
    quote = (f"To get you through the day, here is a quote: {get_quote()}")
    
    return quote

def generate_joke():
    joke = (f"Here's a joke that will brigthen up your day: {get_joke()}")
    
    return joke

def random_message():
    message = random.choice([generate_joke(), 
                            generate_inspiration(), 
                            generate_quote()])
    
    return message