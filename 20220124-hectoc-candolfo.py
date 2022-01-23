#!/usr/bin/env python3

"""
Hectoc calculator project for the module Data Science

:authors: Michele Candolfo

"""

# import HectocMain to start the program
from src.HectocMain import HectocMain
import time # Measurement of the runtime
import sys

def get_input():
    """
    A 6-digit number is required for calculation, which must be entered by the user. 
    """
    print("--------------------------------------------------------------------------------")
    salutation = input("Welcome to the Hectoc Game Prof. Koot, do you wanna play a game? (0 for yes, 1 for no):")
    try:     
        if int(salutation) == 0: 
            print(" \n 1) Type a 6-digit number. \n 2) Each digit may contain a number between 1-9. \n 3) For exapmle: 123456")
            hec_input = input(" \n Please type now: ")
            hec_input_validate = validate_input(hec_input)
            print("\n--------------------------------------------------------------------------------")
            print("The machine is working......")
            return hec_input_validate
        else:
            print("Goodbye Prof. Koot you decided to quit the game too soon!")
            sys.exit()
            
    except ValueError as ve:
        print("\nPlease insert a valid number!")
        get_input()

def validate_input(hec_input):
    """
    This function validates the input from the user 
    """
    try:
        hectoc_lenght = 6
        hectoc_invalid_number = "0"
        hectoc_is_invalid = True

        while hectoc_is_invalid:
            if (len(hec_input) != hectoc_lenght) or (hectoc_invalid_number in hec_input) or (hec_input == ""):
                hectoc_is_invalid = True
                hec_input = input(" \n Try it again. Your input has to be a 6-digit number and each digit must be 1-9: ")
            else:
                hectoc_is_invalid = False
        
        return hec_input
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    hec_input = get_input()
    timer_start = time.time()
    hectoc_main = HectocMain(hec_input)
    timer_end = time.time()
    execution_time = timer_end-timer_start
    print(f'Execution Time:\n{round(execution_time, 3)} seconds')
    print("\n--------------------------------------------------------------------------------")
        
    