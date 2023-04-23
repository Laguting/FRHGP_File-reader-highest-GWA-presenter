# Laguting, Maricon Jane G.
# BSCPE 1-4 
# Task: Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of 
# the student who got the highest GWA (including the GWA).

# Welcome the user to the program
from pyfiglet import Figlet
from termcolor import colored
ti_tle = Figlet(font = "starwars")
print("\33[7m-+°\33[0m" * 45)
print ("")
print(colored(ti_tle.renderText("WELCOME !"), "blue"))
print("\33[7m-+°\33[0m" * 45)

# Introduce FRHGP
file_reader_hgp = "\n\n\33[36m\33[1m'This program will help read a file containing the general weighted average (GWA) of the students and displays the name of the student that got the highest GWA.\U0001F9D0'\33[0m"
print(file_reader_hgp)
# Open gwalist.txt
# Read the contents
# Get the highest GWA
# Display the Highest GWA
# Close the Program