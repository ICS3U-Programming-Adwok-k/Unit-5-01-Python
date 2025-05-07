#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 6th, 2025
# This converts celsius to Fahrenheit
def main():
    # Call the Fahrenheit function
    Fahrenheit()

def Fahrenheit():
    # Define the Fahrenheit function
    celsius_str = input("Enter the temperature: ")

    try:
        # Convert the user input to an integer 
        celsius = int(celsius_str)
        # Calculate the Fahrenheit 
        Fahrenheit = 9 / 5 * celsius + 32
        # Display the celsius is equivalent to a certain Fahrenheit 
        print(f"{celsius} is equivalent to {Fahrenheit} Fahrenheit")

    except:
        # Display the below code for any unknown input
        print("Please enter a valid number.")

    finally:
        # Display Thank you for playing once everything is done
        print("Thank you for playing")


if __name__ == "__main__":
    main()
