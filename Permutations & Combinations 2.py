number_of_inputs = list(map(int, input("Enter the Inputs").split()))
total_outcome = int(input("Enter total no of outcomes"))
number_of_combined_outcomes = list(map(int, input("Enter required Individual outcomes ").split()))
condition = input("enter the condition like 'and' (or) 'or' ")
condition = condition.lower()
length_of_no_of_inputs = len(number_of_inputs)
length_of_no_of_combined_outputs = len(number_of_combined_outcomes)
if condition == "and" and length_of_no_of_inputs == length_of_no_of_combined_outputs:
    factorial_in_the_numerator = 1
    factorial_in_the_denominator = 1
    for i in range(length_of_no_of_inputs):
        no_of_ways_selection_from_the_inputs = (number_of_inputs[i] - number_of_combined_outcomes[i]) + 1

        for factorial in range(no_of_ways_selection_from_the_inputs, number_of_inputs[i] + 1):
            factorial_in_the_numerator *= factorial
            

        for factorial_no_of_ways in range(1, number_of_combined_outcomes[i] + 1):
            factorial_in_the_denominator *= factorial_no_of_ways
            
    list_of_factors_denominator = []
    for factors_of_denominator in range(1, factorial_in_the_denominator):
        if factorial_in_the_denominator % factors_of_denominator == 0:
            list_of_factors_denominator.append(factors_of_denominator)

    list_of_factors_numerator = []
    for factors_of_numerator in range(1, factorial_in_the_numerator):
        if factorial_in_the_numerator % factors_of_numerator == 0:
            list_of_factors_numerator.append(factors_of_numerator)

    if factorial_in_the_denominator in list_of_factors_numerator:
        print("Required Number of Ways = "+str(factorial_in_the_numerator // factorial_in_the_denominator))
    else:
        list_of_common_factors = []
        for j in factors_of_denominator:
            for k in factors_of_numerator:
                if j == k:
                    list_of_common_factors.append(j)

        max_number_which_is_a_common_factor = max(list_of_common_factors)

        print("Required Number of Ways = " +str(factorial_in_the_numerator // max_number_which_is_a_common_factor))
else:
    print("Please enter the valid input")
