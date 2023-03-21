def total_ways_of_forming(separating_atleast_selection, total_no_of_outputs):
    atleast_selecting_output = separating_atleast_selection[0]
    atleast_selecting_input = separating_atleast_selection[1]
    not_atleast_inputs = separating_atleast_selection[2]

    total_number_of_ways = 0

    atleast_chances = 1
    while (atleast_chances <= total_no_of_outputs and atleast_chances <= atleast_selecting_input):
        atleast_choosing = 1
        atleast_starting_number = (atleast_selecting_input - atleast_chances) + 1
        for doing_factorial in range(atleast_starting_number, atleast_selecting_input + 1):
            atleast_choosing *= doing_factorial
        atleast_factorial_of_selection = math.factorial(atleast_chances)
        atleast_ways_of_selection = (atleast_choosing // atleast_factorial_of_selection)

        non_atleast_choosing = 1
        non_strating_number = (not_atleast_inputs - (total_no_of_outputs - atleast_chances)) + 1
        for do_factorial in range(non_strating_number, not_atleast_inputs + 1):
            non_atleast_choosing *= do_factorial
        non_factorial_of_selection = math.factorial((total_no_of_outputs - atleast_chances))
        non_atleast_ways_of_selection = (non_atleast_choosing // non_factorial_of_selection)

        total_number_of_ways += (atleast_ways_of_selection * non_atleast_ways_of_selection)
        atleast_chances += 1
    print("Total number of ways of forming = " + str(total_number_of_ways))


def different_ways_of_selecting(number_of_inputs, number_of_outputs):
    length_of_number_of_inputs = len(number_of_inputs)
    length_of_number_of_outputs = len(number_of_outputs)

    for i in range(length_of_number_of_outputs):
        if number_of_outputs[i] != 0:
            atleast_selecting_output = number_of_outputs[i]
            atleast_selecting_input = number_of_inputs[i]
    print("Now selecting atleast'" + str(atleast_selecting_output) + "' From '" + str(atleast_selecting_input) + "'")

    not_atleast_inputs = 0
    for j in range(length_of_number_of_outputs):
        if atleast_selecting_output != number_of_outputs[j]:
            not_atleast_inputs += number_of_inputs[j]
        else:
            continue

    return atleast_selecting_output, atleast_selecting_input, not_atleast_inputs


import math

number_of_inputs = input("Enter the number of inputs:")
total_no_of_outputs = int(input("Enter total number of outputs:"))
number_of_outputs = input("Enter the individual number of outputs:")

print("Number of inputs = " + number_of_inputs)
print("Total number of outputs = " + str(total_no_of_outputs))
print("-> For atleast selecting one given as non zero value and remaining outputs given as zeros")
print("Number of outputs = " + number_of_outputs)

number_of_inputs = list(map(int, number_of_inputs.split()))
number_of_outputs = list(map(int, number_of_outputs.split()))

separating_atleast_selection = different_ways_of_selecting(number_of_inputs, number_of_outputs)
total_ways_of_forming(separating_atleast_selection, total_no_of_outputs)