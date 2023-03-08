def arranging_at_two_ends(separating_vowels_and_consonants, given_word):
    vowels = separating_vowels_and_consonants[0]
    consonants = separating_vowels_and_consonants[1]

    length_of_vowels = len(vowels)
    length_of_consonants = len(consonants)
    length_of_word = len(given_word)

    print("There are two ends and arranging the vowels at two ends")

    number_of_arranging_vowels = 2
    number_of_arranging_consonants = length_of_word - number_of_arranging_vowels
    if number_of_arranging_vowels < length_of_vowels:
        number_of_arranging_vowels = length_of_vowels
        print("Number of ways of arranging vowels " + str(number_of_arranging_vowels) + "P" + str(length_of_vowels))
        number_of_ways_of_arranging_vowels = math.factorial(number_of_arranging_vowels)
        total_number_of_ways_of_arranging_vowels= number_of_ways_of_arranging_vowels // (math.factorial(number_of_arranging_vowels - length_of_vowels))
        print("Total number of arranging vowels = " + str(total_number_of_ways_of_arranging_vowels))

    else:
        print("Number of ways of arranging vowels " + str(number_of_arranging_vowels) + "P" + str(length_of_vowels))
        number_of_ways_of_arranging_vowels = math.factorial(number_of_arranging_vowels)
        total_number_of_ways_of_arranging_vowels = number_of_ways_of_arranging_vowels // (math.factorial(number_of_arranging_vowels - length_of_vowels))
        print("Total number of arranging vowels = " + str(total_number_of_ways_of_arranging_vowels))

    if number_of_arranging_consonants < length_of_consonants:
        number_of_arranging_consonants = length_of_consonants
        print("Number of ways of arranging consonants " + str(number_of_arranging_consonants) + "P" + str(length_of_consonants))
        number_of_ways_of_arranging_consonants = math.factorial(number_of_arranging_consonants)
        total_number_of_ways_of_arranging_consonants = number_of_ways_of_arranging_consonants // (
            math.factorial(number_of_arranging_consonants - length_of_consonants))
        print("Total number of arranging consonants = " + str(total_number_of_ways_of_arranging_consonants))

    else:
        print("Number of ways of arranging consonants " + str(number_of_arranging_consonants) + "P" + str(
            length_of_consonants))
        number_of_ways_of_arranging_consonants = math.factorial(number_of_arranging_consonants)
        total_number_of_ways_of_arranging_consonants = number_of_ways_of_arranging_consonants // (
            math.factorial(number_of_arranging_consonants - length_of_consonants))
        print("Total number of arranging consonants = " + str(total_number_of_ways_of_arranging_consonants))
    total_number_of_ways_of_arranging = total_number_of_ways_of_arranging_consonants * total_number_of_ways_of_arranging_vowels
    print("Total number of ways of arranging = " + str(total_number_of_ways_of_arranging))


def vowels_and_consonants(given_word, all_vowels):
    vowels = ""
    consonants = ""
    for each_letter in given_word:
        if each_letter in all_vowels:
            vowels += each_letter
        else:
            consonants += each_letter
    return vowels, consonants


import math

given_word = input("Enter the word:").lower()
all_vowels = ['a', 'e', 'i', 'o', 'u']
print("Given word is : " + given_word.upper())

separating_vowels_and_consonants = vowels_and_consonants(given_word, all_vowels)
arranging_at_two_ends(separating_vowels_and_consonants, given_word)