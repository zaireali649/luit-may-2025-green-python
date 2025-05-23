import random  # built-in
import math  # standard library
import os  # standard library
import datetime  # standard library
import matplotlib.pyplot as plt  # pip install matplotlib
from rich import print  # pip install rich
import hello_world_for_import

# Generate a random number
number = random.randint(0, 10)

# Get square root using math
sqrt_number = math.sqrt(number)

# Get current working directory using os
cwd = os.getcwd()

# Get current timestamp using datetime
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get "Hello World"
hello_world = hello_world_for_import.hello_world()

# Pretty print using rich
print(f"[bold cyan]Your random number is: {number}[/bold cyan]")
print(f"[green]Square root: {sqrt_number:.2f}[/green]")
print(f"[yellow]Script ran at: {timestamp}[/yellow]")
print(f"[magenta]Current working directory: {cwd}[/magenta]")
print(f"[blue]Hello World from import: {hello_world}[/blue]")

# Plot the number
plt.bar(["Random Number"], [number], color="skyblue")
plt.ylim(0, 10)
plt.title("Random Number Bar Chart")
plt.show()
