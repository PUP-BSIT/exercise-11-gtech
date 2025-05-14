import random2
from rich import print

def lucky_charm():
    # Dictionary of charms with their associated messages
    charms = {
        "Clover :four_leaf_clover:": "luck is blooming along your path.",
        "Crystal Ball :white_circle:": "pay attention to the"
        " whispers of your inner voice.",
        "Evil Eye :eye:": "do not worry! You are shielded from negativity.",
        "Star :white_medium_star:": "a wish you made is closer to coming true.",
        "Shell :shell:": "new adventures are on the horizon.",
        "Butterfly :butterfly:": "transformation is coming. Embrace the change."
    }

    # Randomly select a charm from the dictionary keys
    charm = random2.choice(list(charms))

    # Construct the daily charm message
    daily_charm = (f" Today's charm is {charm}, {charms[charm]}")

    return daily_charm