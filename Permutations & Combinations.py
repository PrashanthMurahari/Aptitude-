# Permutations & Combinations
# First Input should be in the Format Of String
# Second Input Should be in the format of  Arrange the letters, always be together ,never be together , arrange in even places , -> arrange in odd places


# Always be together
given_letter = input("enter the string input")
given_condition = input("Enter the input as 'arrange the letters' or 'vowels always be together' or 'vowels never be together' or 'arrange the vowels in even places' or 'arrange the vowels in odd places'")
condition = given_condition.lower()
if condition == "vowels always be together":

    word = given_letter.lower()
    length_of_word = len(word)
    list_of_vowels = ["a", "e", "i", "o", 'u']
    vowels = ""
    consonants = ""
    for each_letter in word:
        if each_letter in list_of_vowels:
            vowels += each_letter
        else:
            consonants += each_letter

    length_of_total_letter = len(consonants) + 1
    length_of_vowels = len(vowels)
    print("The word '" + given_letter + "' contains " + str(length_of_word) + " letters = " + str(length_of_word) + "!")
    print("Consonants In The Given Word - '" + consonants + "'" + "\n" + "Vowels In The Given Word - '" + vowels + "'")
    print("Number Of Ways - '" + consonants + "+" + vowels + "' = " + str(length_of_total_letter) + "!" + " * " + str(
        length_of_vowels) + "!" + "\n" + "(Consider All the vowels as 1 unit )")
    total_numerator = 1
    for numerator_part_for_consonants in range(1, length_of_total_letter + 1):
        total_numerator *= numerator_part_for_consonants
    for numerator_part_for_vowels in range(1, length_of_vowels + 1):
        total_numerator *= numerator_part_for_vowels

    set_of_consonants = set(consonants)
    list_of_consonants = list(set_of_consonants)
    list_of_single_number_consonants = sorted(list_of_consonants)

    set_of_vowels = set(vowels)
    list_of_vowels_in_word = list(set_of_vowels)
    list_of_single_number_vowels = sorted(list_of_vowels_in_word)

    total_denominator = 1
    for denominator_part_of_consonants in list_of_single_number_consonants:
        count_of_consonants = 0
        for same_letters_of_consonants in consonants:
            if denominator_part_of_consonants == same_letters_of_consonants:
                count_of_consonants += 1
        if count_of_consonants > 1:
            for count_greater_than_1_in_consonants in range(1, count_of_consonants + 1):
                similar_letters_of_consonants = ""
                total_denominator *= count_greater_than_1_in_consonants
            similar_letters_of_consonants += str(count_of_consonants) + "'" + denominator_part_of_consonants + "'"
            print("Similar Letters - " + similar_letters_of_consonants + " = " + str(count_of_consonants) + "!")

    for denominator_part_of_vowels in list_of_single_number_vowels:
        count_of_vowels = 0
        for same_letters_of_vowels in vowels:
            if denominator_part_of_vowels == same_letters_of_vowels:
                count_of_vowels += 1
        if count_of_vowels > 1:
            for count_greater_than_1_in_vowels in range(1, count_of_vowels + 1):
                similar_letters_of_vowels = ""
                total_denominator *= count_greater_than_1_in_vowels
            similar_letters_of_vowels += str(count_of_vowels) + "'" + denominator_part_of_vowels + "'"
            print("Similar Letters - " + similar_letters_of_vowels + " = " + str(count_of_vowels) + "!")
    let_number_of_ways_of_arranging_the_letters = int(total_numerator / total_denominator)
    print("Number Of Ways = " + str(total_numerator) + "\n" + "Similar Letters = " + str(total_denominator))

    print("Total Number Of Ways That Vowels Always be together= Number of ways / Similar Letters")
    print("Total Number Of Ways That Vowels Always be together" + " - " + str(
        let_number_of_ways_of_arranging_the_letters))


# For Vowels never be together
elif condition == "vowels never be together":
    word = given_letter.lower()
    # numerator FOR never be together
    length_of_word = len(word)
    numerator_of_total_word = 1
    for factorial in range(1, length_of_word + 1):
        numerator_of_total_word *= factorial
    # demoninator for never be together
    list_of_vowels = ["a", "e", "i", "o", 'u']
    vowels = ""
    consonants = ""
    for each_letter in word:
        if each_letter in list_of_vowels:
            vowels += each_letter
        else:
            consonants += each_letter
    set_of_total_word = set(word)
    list_of_word = list(set_of_total_word)
    list_of_total_word = sorted(list_of_word)
    print("The word '" + given_letter + "' contains " + str(length_of_word) + " letters = " + str(length_of_word) + "!")
    total_denominator_for_never_be_together = 1
    for counting_of_letter in list_of_total_word:
        count_of_each_letter_in_word = 0
        for same_latters_in_word in word:
            if counting_of_letter == same_latters_in_word:
                count_of_each_letter_in_word += 1
        if count_of_each_letter_in_word > 1:
            for factorial_in_denominator in range(1, count_of_each_letter_in_word + 1):
                similar_letters = ""
                total_denominator_for_never_be_together *= factorial_in_denominator
            similar_letters += str(count_of_each_letter_in_word) + "'" + counting_of_letter + "'"
            print("Similar Letters - " + similar_letters + " = " + str(count_of_each_letter_in_word) + "!")
    let_number_of_ways_of_vowels_never_be_together = int(
        numerator_of_total_word / total_denominator_for_never_be_together)

    print("Total Number Of Ways " + " - " + str(let_number_of_ways_of_vowels_never_be_together))

    length_of_total_letter = len(consonants) + 1
    length_of_vowels = len(vowels)
    total_numerator = 1
    for numerator_part_for_consonants in range(1, length_of_total_letter + 1):
        total_numerator *= numerator_part_for_consonants
    for numerator_part_for_vowels in range(1, length_of_vowels + 1):
        total_numerator *= numerator_part_for_vowels
    print("Consonants In The Given Word - '" + consonants + "'" + "\n" + "Vowels In The Given Word - '" + vowels + "'")
    print("Number Of Ways - '" + consonants + "+" + vowels + "'" + " = " + str(length_of_total_letter) + "!")

    set_of_consonants = set(consonants)
    list_of_consonants = list(set_of_consonants)
    list_of_single_number_consonants = sorted(list_of_consonants)

    set_of_vowels = set(vowels)
    list_of_vowels_in_word = list(set_of_vowels)
    list_of_single_number_vowels = sorted(list_of_vowels_in_word)

    total_denominator = 1
    for denominator_part_of_consonants in list_of_single_number_consonants:
        count_of_consonants = 0
        for same_letters_of_consonants in consonants:
            if denominator_part_of_consonants == same_letters_of_consonants:
                count_of_consonants += 1
        if count_of_consonants > 1:
            for count_greater_than_1_in_consonants in range(1, count_of_consonants + 1):
                similar_letters_of_consonants = ""
                total_denominator *= count_greater_than_1_in_consonants
            similar_letters_of_consonants += str(count_of_consonants) + "'" + denominator_part_of_consonants + "'"
            print("Similar Letters Of Consonants - " + similar_letters_of_consonants + " = " + str(
                count_of_consonants) + "!")

    for denominator_part_of_vowels in list_of_single_number_vowels:
        count_of_vowels = 0
        for same_letters_of_vowels in vowels:
            if denominator_part_of_vowels == same_letters_of_vowels:
                count_of_vowels += 1
        if count_of_vowels > 1:
            for count_greater_than_1_in_vowels in range(1, count_of_vowels + 1):
                similar_letters_of_vowels = ""
                total_denominator *= count_greater_than_1_in_vowels
            similar_letters_of_vowels += str(count_of_vowels) + "'" + denominator_part_of_vowels + "'"
            print("Similar Letters Of Vowels - " + similar_letters_of_vowels + " = " + str(count_of_vowels) + "!")
    let_number_of_ways_of_vowels_always_together = int(total_numerator / total_denominator)
    print("Number Of Ways = " + str(total_numerator) + "\n" + "Similar Letters = " + str(total_denominator))
    print("Number of Ways that Vowels always be Together = Number Of Ways / Similar Letters")
    print("Number of Ways that Vowels always be Together " + " - " + str(let_number_of_ways_of_vowels_always_together))
    print(
        "Number of Ways that Vowels Never Be Together = Total Number Of Ways - Total Number of Ways that Vowels always be Together")
    print("Number of Ways that Vowels Never Be Together" + " - " + str(
        let_number_of_ways_of_vowels_never_be_together - let_number_of_ways_of_vowels_always_together))

# Arrange The Letters
elif condition == "arrange the letters":
    word = given_letter.lower()
    length_of_word = len(word)
    numerator_of_total_word = 1
    for factorial in range(1, length_of_word + 1):
        numerator_of_total_word *= factorial
    list_of_vowels = ["a", "e", "i", "o", 'u']
    vowels = ""
    consonants = ""
    for each_letter in word:
        if each_letter in list_of_vowels:
            vowels += each_letter
        else:
            consonants += each_letter
    print("The word '" + given_letter + "' contains " + str(length_of_word) + " letters = " + str(length_of_word) + "!")
    set_of_total_word = set(word)
    list_of_word = list(set_of_total_word)
    list_of_total_word = sorted(list_of_word)

    total_denominator_for_never_be_together = 1
    for counting_of_letter in list_of_total_word:
        count_of_each_letter_in_word = 0
        for same_latters_in_word in word:
            if counting_of_letter == same_latters_in_word:
                count_of_each_letter_in_word += 1
        if count_of_each_letter_in_word > 1:

            for factorial_in_denominator in range(1, count_of_each_letter_in_word + 1):
                similar_letters = ""
                total_denominator_for_never_be_together *= factorial_in_denominator
            similar_letters += str(count_of_each_letter_in_word) + "'" + counting_of_letter + "'"
            print("Similar Letters - " + similar_letters + " = " + str(count_of_each_letter_in_word) + "!")

    let_number_of_ways_of_vowels_never_be_together = int(
        numerator_of_total_word / total_denominator_for_never_be_together)
    print("Number Of Ways = " + str(numerator_of_total_word) + "\n" + "Similar Letters = " + str(
        total_denominator_for_never_be_together))
    print("Required Number Of Ways = Number Of Ways / Similar Letters ")

    print("Required Number Of ways  = " + str(let_number_of_ways_of_vowels_never_be_together))


# odd place arrangement
elif condition == "arrange the vowels in odd places":
    word = given_letter.lower()
    length_of_word = len(word)
    number_of_even_places = 0
    number_of_odd_places = 0
    even_places_as_string = ""
    odd_places_as_string = ""
    for each_number in range(1, length_of_word + 1):
        if each_number % 2 == 0:
            number_of_even_places += 1
            even_places_as_string += str(each_number) + " "
        else:
            number_of_odd_places += 1
            odd_places_as_string += str(each_number) + " "
    print("The word '" + given_letter + "' contains " + str(length_of_word) + " letters = " + str(length_of_word) + "!")

    print("Even Places - " + even_places_as_string + "\n" + "Odd Places - " + odd_places_as_string)
    list_of_vowels = ["a", "e", "i", "o", 'u']
    vowels = ""
    consonants = ""
    for each_letter in word:
        if each_letter in list_of_vowels:
            vowels += each_letter
        else:
            consonants += each_letter
    print("Vowels - '" + str(vowels) + "'" + "\n" + "Consonants - '" + str(consonants) + "'")
    length_of_vowels = len(vowels)
    length_of_consonants = len(consonants)

    factorial_of_odd_places_in_numerator = 1
    factorial_of_even_places_in_numerator = 1
    if number_of_odd_places < length_of_vowels:
        number_of_odd_places = length_of_vowels
    for odd_places in range(1, number_of_odd_places + 1):
        factorial_of_odd_places_in_numerator *= odd_places
    if number_of_even_places < length_of_consonants:
        number_of_even_places = length_of_consonants
    for even_places in range(1, number_of_even_places + 1):
        factorial_of_even_places_in_numerator *= even_places

    if number_of_even_places > length_of_consonants:
        even_places_permutations = number_of_even_places - length_of_consonants
    else:
        even_places_permutations = length_of_consonants - number_of_even_places
    factorial_of_even_places_in_denominator = 1
    for even_places_in_denominators in range(1, even_places_permutations + 1):
        factorial_of_even_places_in_denominator *= even_places_in_denominators

    if number_of_odd_places > length_of_vowels:
        odd_places_permutations = number_of_odd_places - length_of_vowels
    else:
        odd_places_permutations = length_of_vowels - number_of_odd_places
    factorial_of_odd_places_in_denominator = 1
    for odd_places_in_denominators in range(1, odd_places_permutations + 1):
        factorial_of_odd_places_in_denominator *= odd_places_in_denominators

    let_number_of_ways_of_consonants = int(
        factorial_of_even_places_in_numerator / factorial_of_even_places_in_denominator)
    let_number_of_ways_of_vowels = int(factorial_of_odd_places_in_numerator / factorial_of_odd_places_in_denominator)

    print("Number Of  Ways Of arranging Vowels = " + str(number_of_even_places) + "P" + str(length_of_consonants))
    print("Number Of  Ways Of arranging Consonants = " + str(number_of_odd_places) + "P" + str(length_of_vowels))
    print(
        "Total No of Ways of arranging the word =  Number Of  Ways Of arranging Vowels * Number Of  Ways Of arranging Consonants")
    print("Total No of Ways of arranging the word = " + str(
        let_number_of_ways_of_vowels * let_number_of_ways_of_consonants))


# Even place arrangement
elif condition == "arrange the vowels in even places":
    word = given_letter.lower()
    length_of_word = len(word)
    number_of_even_places = 0
    number_of_odd_places = 0
    odd_places_as_string = ""
    even_places_as_string = ""
    for each_number in range(1, length_of_word + 1):
        if each_number % 2 == 0:
            number_of_even_places += 1
            even_places_as_string += str(each_number) + " "

        else:
            number_of_odd_places += 1
            odd_places_as_string += str(each_number) + " "

    print("The word '" + given_letter + "' contains " + str(length_of_word) + " letters = " + str(length_of_word) + "!")

    print("Even Places - " + even_places_as_string + "\n" + "Odd Places - " + odd_places_as_string)

    list_of_vowels = ["a", "e", "i", "o", 'u']
    vowels = ""
    consonants = ""
    for each_letter in word:
        if each_letter in list_of_vowels:
            vowels += each_letter
        else:
            consonants += each_letter
    print("Vowels - '" + str(vowels) + "'" + "\n" + "Consonants - '" + str(consonants) + "'")
    length_of_vowels = len(vowels)
    length_of_consonants = len(consonants)

    factorial_of_odd_places_in_numerator = 1
    factorial_of_even_places_in_numerator = 1
    if number_of_even_places < length_of_vowels:
        number_of_even_places = length_of_vowels
    for odd_places in range(1, number_of_odd_places + 1):
        factorial_of_odd_places_in_numerator *= odd_places
    if number_of_odd_places < length_of_consonants:
        number_of_odd_places = length_of_consonants
    for even_places in range(1, number_of_even_places + 1):
        factorial_of_even_places_in_numerator *= even_places

    if number_of_even_places > length_of_consonants:
        even_places_permutations = number_of_even_places - length_of_consonants
    elif number_of_even_places == length_of_consonants:
        even_places_permutations = 1
    else:
        even_places_permutations = length_of_consonants - number_of_even_places
    factorial_of_even_places_in_denominator = 1
    for even_places_in_denominators in range(1, even_places_permutations + 1):
        factorial_of_even_places_in_denominator *= even_places_in_denominators

    if number_of_odd_places > length_of_vowels:
        odd_places_permutations = number_of_odd_places - length_of_vowels
    elif number_of_odd_places == length_of_vowels:
        odd_places_permutations = 1
    else:
        odd_places_permutations = length_of_vowels - number_of_odd_places
    factorial_of_odd_places_in_denominator = 1
    for odd_places_in_denominators in range(1, odd_places_permutations + 1):
        factorial_of_odd_places_in_denominator *= odd_places_in_denominators

    let_number_of_ways_of_consonants = int(
        factorial_of_even_places_in_numerator / factorial_of_even_places_in_denominator)
    let_number_of_ways_of_vowels = int(factorial_of_odd_places_in_numerator / factorial_of_odd_places_in_denominator)
    print("Number Of  Ways Of arranging Vowels = " + str(number_of_even_places) + "P" + str(length_of_vowels))
    print("Number Of  Ways Of arranging Consonants = " + str(number_of_odd_places) + "P" + str(length_of_consonants))
    print(
        "Total No of Ways of arranging the word =  Number Of  Ways Of arranging Vowels * Number Of  Ways Of arranging Consonants")
    print("Total No of Ways of arranging the word = " + str(
        let_number_of_ways_of_vowels * let_number_of_ways_of_consonants))

else:
    print("Please Enter The Valid Input")
