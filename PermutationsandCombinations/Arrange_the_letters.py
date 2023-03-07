def finding_number_of_ways_arranging(given_word, length_of_the_word, list_of_removing_similar_letters):
    print("Number of ways of arranging the word  = " + str(length_of_the_word) + "!")

    number_of_arranging_all_letters=math.factorial(length_of_the_word)
    print("Number of ways of arranging the word : " + str(number_of_arranging_all_letters))

    total_similar_letters_factorial = 1
    for similar_letters in list_of_removing_similar_letters:
        counting_the_factorial_of_similar_letters = 0
        for same_letters_in_given_word in given_word:
            if similar_letters == same_letters_in_given_word:
                counting_the_factorial_of_similar_letters += 1

        if counting_the_factorial_of_similar_letters > 1:
            print("Similar Letters : " + str(counting_the_factorial_of_similar_letters) + " " + similar_letters + "'s = " + str(counting_the_factorial_of_similar_letters) + "!")
        similar_letters_factorial=math.factorial(counting_the_factorial_of_similar_letters)
        total_similar_letters_factorial*=similar_letters_factorial
    if total_similar_letters_factorial > 1:
        print("Arranging the similar letters : " + str(total_similar_letters_factorial))
        number_of_ways_of_arranging_the_given_word = number_of_arranging_all_letters / total_similar_letters_factorial
        print("Total number of ways of arranging the word = " + str(number_of_arranging_all_letters) + "/" + str(total_similar_letters_factorial))
        print("Total number of ways of arranging the word : " + str(int(number_of_ways_of_arranging_the_given_word)))
    else:
        pass
import math
given_word = input("Enter the word :").lower()
condition = input("Enter the condition like arrange the letters:").lower()
length_of_the_word = len(given_word)

if condition == "arrange the letters":
    print("Given condition is " + condition.upper() )
    removing_similar_letters = set(given_word)
    list_of_removing_similar_letters = sorted(list(removing_similar_letters))
    finding_number_of_ways_arranging(given_word, length_of_the_word, list_of_removing_similar_letters)
else:
    print("Enter a valid input!!")