def different_ways_of_doing(number_of_inputs, number_of_combined_outcomes, length_number_of_outputs,length_number_of_inputs):
    factorial_of_the_given_inputs = 1
    factorial_of_the_given_outputs = 1
    for i in range(length_number_of_inputs):
        if number_of_combined_outcomes[i] != 0:
            number_of_ways_of_selecting = (number_of_inputs[i] - number_of_combined_outcomes[i]) + 1
            print("Different Ways of forming  : " + str(number_of_inputs[i]) + "C" + str(number_of_combined_outcomes[i]))
        else:
            continue
        for factorial_of_inputs in range(number_of_ways_of_selecting, number_of_inputs[i] + 1):
            factorial_of_the_given_inputs *= factorial_of_inputs
        factorial_of_outputs = math.factorial(number_of_combined_outcomes[i])
        factorial_of_the_given_outputs *= factorial_of_outputs
    total_number_of_ways = factorial_of_the_given_inputs // factorial_of_the_given_outputs
    print("Total number of ways of forming = " + str(total_number_of_ways))


import math

number_of_inputs = input("Enter number of inputs given:")

number_of_combined_outcomes = input("Enter the number of outputs given:")
print("Total number of inputs = " + number_of_inputs)
print("Total number of inputs = " + number_of_combined_outcomes)
number_of_inputs = list(map(int, number_of_inputs.split()))
number_of_combined_outcomes = list(map(int, number_of_combined_outcomes.split()))
length_number_of_inputs = len(number_of_inputs)
length_number_of_outputs = len(number_of_combined_outcomes)
different_ways_of_doing(number_of_inputs, number_of_combined_outcomes, length_number_of_outputs,length_number_of_inputs)