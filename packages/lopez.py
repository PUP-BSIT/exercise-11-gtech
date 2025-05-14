import random 

def lucky_charm():
    # Dictionary of charms with their associated messages
    charms = {
        "Clover": "luck is blooming along your path.",
        "Crystal Ball": "pay attention to the whispers of your inner voice.",
        "Evil Eye": "do not worry! You are shielded from negativity.",
        "Star": "a wish you made is closer to coming true.",
        "Shell": "new adventures are on the horizon.",
        "Butterfly": "transformation is coming. Embrace the change."
    }

    # Randomly select a charm from the dictionary keys
    charm = random.choice(list(charms))

    # Construct the daily charm message
    daily_charm = (f"Today's charm is {charm}, {charms[charm]}")

    return daily_charm