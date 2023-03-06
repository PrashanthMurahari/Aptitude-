def finding_number_of_ways_arranging(given_word, length_of_the_word, list_of_removing_similar_letters):
    print("Number of ways of arranging the word  = " + str(length_of_the_word) + "!")

    number_of_arranging_all_letters = 1
    for factorial_of_arranging_all_letters in range(1, length_of_the_word + 1):
        number_of_arranging_all_letters *= factorial_of_arranging_all_letters
    print("Number of ways of arranging the word : " + str(number_of_arranging_all_letters))

    similar_letters_factorial = 1
    for similar_letters in list_of_removing_similar_letters:
        counting_the_factorial_of_similar_letters = 0
        for same_letters_in_given_word in given_word:
            if similar_letters == same_letters_in_given_word:
                counting_the_factorial_of_similar_letters += 1

        if counting_the_factorial_of_similar_letters > 1:
            print("Similar Letters : " + str(counting_the_factorial_of_similar_letters) + " " + similar_letters + "'s = " + str(counting_the_factorial_of_similar_letters) + "!")
        for factorial in range(1, counting_the_factorial_of_similar_letters + 1):
            similar_letters_factorial *= factorial

    if similar_letters_factorial > 1:
        print("Arranging the similar letters : " + str(similar_letters_factorial))
        number_of_ways_of_arranging_the_given_word = number_of_arranging_all_letters / similar_letters_factorial
        print("Total number of ways of arranging the word = " + str(number_of_arranging_all_letters) + "/" + str(similar_letters_factorial))
        print("Total number of ways of arranging the word : " + str(int(number_of_ways_of_arranging_the_given_word)))
    else:
        pass

given_word = input().lower()
condition = input().lower()
length_of_the_word = len(given_word)

if condition == "arrange the letters":
    print("Given condition is " + condition + " :")
    removing_similar_letters = set(given_word)
    list_of_removing_similar_letters = sorted(list(removing_similar_letters))
    finding_number_of_ways_arranging(given_word, length_of_the_word, list_of_removing_similar_letters)
else:
    print("Enter a valid input!!")