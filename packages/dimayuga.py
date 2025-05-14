from quote_inspire_jokes.inspire import get_inspiration

def generate_quote():
    quote = (f"For a dose of inspiration, here’s your lucky quote"
             f" of the day: {get_inspiration()}")

    
    return quote