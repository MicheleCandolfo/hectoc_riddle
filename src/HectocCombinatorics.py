#!/usr/bin/env python3

# Imports
from copy import deepcopy
import itertools
from src import HectocConversionAndStrategy as hectoc_conversion
    

# Section 1 : In this section we will get all the possible combinations.
def find_combinations(char_list_of_hectoc): 
    """
    This function will return all possible combinations in a list format. 
    """
    try:
        deep_copy_of_a_hectoc_list = [deepcopy(char_list_of_hectoc)] # The original list will be copied through a "deep copy"

        for index in range(get_pos_of_paired_digit(char_list_of_hectoc), len(char_list_of_hectoc) - 1):
            tmp_array = deepcopy(char_list_of_hectoc)

            # Concatenation of the first and second digit to get a new digit [8, 9, 5, 6] -> [89, 9, 5, 6]
            # The rest digit at the end will be deleted [89,9, 5, 6] -> [89, 5, 6]
            tmp_array[index] = int(str(tmp_array[index]) + str(tmp_array[index + 1]))
            tmp_array.pop(index + 1)

            # This process will be repeated through the function until the length of the original hectoc_list is reached.
            # The new combinantions will be saved in the copy list.
            new_list_with_combinations = find_combinations(tmp_array)
            deep_copy_of_a_hectoc_list.extend(new_list_with_combinations)

        # The new list will be returned. In this variable all the possible combinantions are stored.
        return deep_copy_of_a_hectoc_list
    except Exception as error:
        print(error)

def get_pos_of_paired_digit(char_list_of_hectoc):
    """
    This function will return the index of the first double digit. 
    """
    try:
        for pos, char in enumerate(char_list_of_hectoc):
            if char >= 10:
                return pos
        return 0
    except Exception as error:
        print(error)


# Section 2: In this section we will get combinations including the operators.
def find_permutation_of_digits_and_math_op_combinantions(permutation):
    """
    This function will return a combined list with all possible combinations of digits and mathematical expressions
    """
    try:
        # operators
        ops = ["+","-","*","/","^"]
        term_list = []   

        # Creating a list with all possible combinations of operators
        operators = list(itertools.product(ops, repeat=len(permutation) - 1))

        for operator in operators:
            first_digit = str(permutation[0]) # Getting the first number of every expression
            i = 1
            for operato in operator:
                first_digit = first_digit + operato + str(permutation[i])
                i += 1
            term_list = term_list + [first_digit] # Adding the expressions in a new list

        return term_list
    except Exception as error:
        print(error)


# Section 3: In this section we will get all the needed parantheses.
def find_all_paranthese(permutations):
    """
    This function will return a list with all expressions including the parantheses
    """
    try:
        parantheses_list = []
        for permutation in permutations:
            # Getting for every expression a new list with paranthese 
            all_parantheses = parenthese(permutation)
            parantheses_list.extend(all_parantheses)
        
        return parantheses_list # Returning all parantheses in a list
    except Exception as error:
        print(error)

def parenthese(permutation):
    """
    This function will return a list of all possibilities of parantheses for the operators
    """
    try:
        # operators
        operators = ["+","-","*","/","^"]

        # Getting the amount of operators
        count_of_operators = len([val for val in permutation if val in operators])

        # Checking if there is no operator in an expression. If thats the case the number will be returned
        # Checking if there is one operator in an expression. If thats the case, two parantheses will be added.  
        if count_of_operators == 0:
            return [permutation]
        if count_of_operators == 1:
            return ['(' + permutation + ')']

        # Checking if the amount of operators is more than one. 
        # Then all parantheses on the left and right side will be added. 
        final_list_with_all_parantheses = []
        for i, ops in enumerate(permutation):
            if ops in operators:
                left = permutation[:i]
                right = permutation[(i + 1):]
                paranthese = ['('+left_side+')'+ops+'('+right_side+')' for left_side in parenthese(left) for right_side in parenthese(right)]
                final_list_with_all_parantheses.extend(paranthese)
        return final_list_with_all_parantheses
    except Exception as error:
        print(error)

