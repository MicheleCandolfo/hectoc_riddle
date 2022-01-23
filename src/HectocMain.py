#!/usr/bin/env python3

from src import HectocConversionAndStrategy as hectoc_conversion
from src import HectocCombinatorics as hec_combi
from src import HectocSolve as hec_solve

class HectocMain:
    def __init__(self, user_input):
        self.user_input = user_input
        self.start_programm()

    def start_programm(self) -> None:
        user_input = self.user_input
        char_list_of_hectoc = hectoc_conversion.split_hectoc_string_and_convert(user_input)

        # find all combinations and convert it to float
        combinations = hec_combi.find_combinations(char_list_of_hectoc)
        combinations = hectoc_conversion.convert_int_to_float(combinations)

        # get all permutations with the combinations and operators
        permutations = []
        for permutation in combinations:
            # Getting the expressions for each combinantion
            permutations_with_hectoc_and_operators = hec_combi.find_permutation_of_digits_and_math_op_combinantions(permutation)
            permutations.extend(permutations_with_hectoc_and_operators)

        # find all parantheses
        expressions_with_parantheses = hec_combi.find_all_paranthese(permutations)

        # solve the problem
        hec_solve.solve_hectoc(expressions_with_parantheses)



