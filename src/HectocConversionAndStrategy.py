
def split_hectoc_string_and_convert(user_input):
    return list(map(int, str(user_input)))

# Convert a array[][] with integer values to float values
def convert_int_to_float(array):
    for i, values in enumerate(array):
        for j, value in enumerate(values):
            array[i][j] = float(value)
    return array

