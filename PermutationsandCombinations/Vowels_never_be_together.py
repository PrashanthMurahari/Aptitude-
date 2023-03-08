def number_of_ways_of_arranging_vowels(vowels_and_consonants_together):
    vowels = vowels_and_consonants_together[1]
    length_of_vowels = len(vowels)
    print("Number of ways of arranging the vowels : " + str(length_of_vowels) + "!")
    arranging_vowels = math.factorial(length_of_vowels)
    print("Number of ways of arranging the vowels : " + str(arranging_vowels))

    removing_similar_letters = set(vowels)
    list_of_non_similar_letters = sorted(list(removing_similar_letters))

    total_factorial_of_similar_letters = 1
    for finding_similar_letters in list_of_non_similar_letters:
        total_similar_letters = 0
        for same_letters in vowels:
            if finding_similar_letters == same_letters:
                total_similar_letters += 1

        if total_similar_letters > 1:
            print("Similar Letters : " + str(total_similar_letters) + " " + finding_similar_letters + "'s = " + str(total_similar_letters) + "!")
            similar_letters_factorial = math.factorial(total_similar_letters)
            total_factorial_of_similar_letters *= similar_letters_factorial

    number_of_ways_of_arranging_the_vowels = arranging_vowels / total_factorial_of_similar_letters
    if total_factorial_of_similar_letters > 1:
        print("Arranging the similar letters : " + str(total_factorial_of_similar_letters))
        print("Total number of ways of arranging the vowels = " + str(arranging_vowels) + "/" + str(total_factorial_of_similar_letters))
        print("Total number of ways of arranging the vowels : " + str(int(number_of_ways_of_arranging_the_vowels)))
    return number_of_ways_of_arranging_the_vowels


def number_of_ways_of_arranging_consonants(vowels_and_consonants_together):
    consonants = vowels_and_consonants_together[0]
    length_of_consonants = len(consonants)

    print("Number of ways of arranging the consonants : " + str(length_of_consonants + 1) + "!")
    arranging_consonants = math.factorial(length_of_consonants + 1)
    print("Number of ways of arranging the consonants : " + str(arranging_consonants))

    removing_similar_letters = set(consonants)
    list_of_non_similar_letters = sorted(list(removing_similar_letters))

    total_factorial_of_similar_letters = 1
    for finding_similar_letters in list_of_non_similar_letters:
        total_similar_letters = 0
        for same_letters in consonants:
            if finding_similar_letters == same_letters:
                total_similar_letters += 1

        if total_similar_letters > 1:
            print("Similar Letters : " + str(total_similar_letters) + " " + finding_similar_letters + "'s = " + str(total_similar_letters) + "!")
            similar_letters_factorial = math.factorial(total_similar_letters)
            total_factorial_of_similar_letters *= similar_letters_factorial

    number_of_ways_of_arranging_the_consonants = arranging_consonants / total_factorial_of_similar_letters
    if total_factorial_of_similar_letters > 1:
        print("Arranging the similar letters : " + str(total_factorial_of_similar_letters))
        print("Total number of ways of arranging the consonants = " + str(arranging_consonants) + "/" + str(total_factorial_of_similar_letters))
        print("Total number of ways of arranging the consonants : " + str(int(number_of_ways_of_arranging_the_consonants)))
    return number_of_ways_of_arranging_the_consonants


def separating_vowels_and_consonants(given_word, all_vowels):
    vowels = ""
    consonants = ""
    for one_letter in given_word:
        if one_letter in all_vowels:
            vowels += one_letter
        else:
            consonants += one_letter
    return consonants, vowels


def finding_number_of_ways_arranging(given_word, length_of_the_word, list_of_removing_similar_letters):
    print("Number of ways of arranging the word  = " + str(length_of_the_word) + "!")

    number_of_arranging_all_letters = math.factorial(length_of_the_word)
    print("Number of ways of arranging the word : " + str(number_of_arranging_all_letters))

    total_similar_letters = 1
    for similar_letters in list_of_removing_similar_letters:
        the_factorial_of_similar_letters = 0
        for same_letters_in_given_word in given_word:
            if similar_letters == same_letters_in_given_word:
                the_factorial_of_similar_letters += 1

        if the_factorial_of_similar_letters > 1:
            print("Similar Letters : " + str(the_factorial_of_similar_letters) + " " + similar_letters + "'s = " + str(the_factorial_of_similar_letters) + "!")
            similar_letters_factorial = math.factorial(the_factorial_of_similar_letters)
            total_similar_letters *= similar_letters_factorial
    number_of_ways_of_arranging_the_given_word = number_of_arranging_all_letters / total_similar_letters
    if total_similar_letters > 1:
        print("Arranging the similar letters : " + str(total_similar_letters))
        print("Total number of ways of arranging the word = " + str(number_of_arranging_all_letters) + "/" + str(total_similar_letters))
        print("Total number of ways of arranging the word : " + str(int(number_of_ways_of_arranging_the_given_word)))
    return number_of_ways_of_arranging_the_given_word


import math

given_word = input("Enter the word:").lower()
length_of_the_word = len(given_word)
all_vowels = ["a", "e", "i", "o", "u"]

print("Given word is : "+given_word)
removing_similar_letters = set(given_word)
list_of_removing_similar_letters = sorted(list(removing_similar_letters))
number_of_ways_of_arranging_the_given_word = finding_number_of_ways_arranging(given_word, length_of_the_word,list_of_removing_similar_letters)

vowels_and_consonants_together = separating_vowels_and_consonants(given_word, all_vowels)
print("Consonants : " + vowels_and_consonants_together[0])
print("Vowels : " + vowels_and_consonants_together[1])
number_of_ways_of_arranging_the_consonants = number_of_ways_of_arranging_consonants(vowels_and_consonants_together)
number_of_ways_of_arranging_the_vowels = number_of_ways_of_arranging_vowels(vowels_and_consonants_together)
number_of_ways_of_arranging_the_word_that_vowels_always_be_together = number_of_ways_of_arranging_the_consonants * number_of_ways_of_arranging_the_vowels
print("Total Number of ways of arranging the word that vowels always be together : " + str(int(number_of_ways_of_arranging_the_word_that_vowels_always_be_together)))
number_of_ways_of_arranging_the_word_that_vowels_never_be_together = number_of_ways_of_arranging_the_given_word - number_of_ways_of_arranging_the_word_that_vowels_always_be_together
print("Total number of ways of arranging the word that vowels never be together = Total number of ways of arranging the word - Total Number of ways of arranging the word that vowels always be together")
print("Total number of ways of arranging the word that vowels never be together = " + str(int(number_of_ways_of_arranging_the_word_that_vowels_never_be_together)))
