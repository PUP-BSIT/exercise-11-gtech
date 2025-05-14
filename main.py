# Import custom modules from the packages and rich library for styled output
from packages import aragon, dimayuga, lim, lopez, romero
from rich.console import Console
from rich.panel import Panel 
from rich.align import Align
from rich import box
import random

# Initialize a Console object to enable rich, styled output to terminal
console = Console()

# Display the welcome message as the program title 
console.print(Align.center(f"[bold magenta]Welcome to CharMeter!"
              f" Ready to discover your luck today?[/bold magenta]"))
# Prompt the user to input their name and display their name with styled text
user_name = input("Enter your name: ")
console.print(
            f"\n[bold magenta]Hello, {user_name}!"
            f" Here's your CharMeter reading:[/bold magenta]\n"
            )

# Generate the full message from functions in the imported modules 
lucky_message = (
                f"{romero.get_current_time()}"
                f"{lim.display_weekday()}"
                f"{aragon.generate_number()}"
                f"{lopez.lucky_charm()}"
                "\n\n"
                f"{dimayuga.random_message()}"
                )

# Display the final generated message in a styled panel 
console.print(Panel((f"[italic yellow] {lucky_message} [/italic yellow]"), 
                    title="CharMeter Message", 
                    box=box.DOUBLE_EDGE, 
                    expand=True))