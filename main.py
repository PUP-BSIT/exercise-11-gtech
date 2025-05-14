# Import custom modules from the packages and rich library for styled output
from packages import aragon, dimayuga, lim, lopez, romero
from rich.console import Console
from rich.panel import Panel 
from rich import box 

# Initialize a Console object to enable rich, styled output to terminal
console = Console()

# Display the welcome message as the program title 
console.print(f"\n\t\t\t\t\t[bold magenta]Welcome to CharMeter!"
              f" Ready to discover your luck today?[/bold magenta]")
# Prompt the user to input their name and display their name with styled text
user_name = input("Enter your name: ")
console.print(f"\n[bold magenta]Hello, {user_name}!"
              f" Here's your CharMeter reading:[/bold magenta]\n")

# Generate the full message from functions in the imported modules 
lucky_message = (f"{romero.get_current_time()} {lim.display_weekday()}"
                 f"{aragon.generate_number()} {lopez.lucky_charm()}"
                 f"\n\n{dimayuga.generate_quote()}")

# Display the final generated message in a styled panel 
console.print(Panel(lucky_message, title="CharMeter Message", 
                    box=box.DOUBLE_EDGE, expand=True))