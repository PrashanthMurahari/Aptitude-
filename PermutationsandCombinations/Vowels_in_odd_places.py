def arrangement_of_vowels(vowels_and_consonants, number_of_even_odd_places):
    vowels = vowels_and_consonants[0]
    number_of_odd_places = number_of_even_odd_places[0]

    if number_of_odd_places < len(vowels):
        number_of_odd_places = len(vowels)
        factorial_of_arranging_vowels = math.factorial(number_of_odd_places)

    else:
        factorial_of_arranging_vowels = (math.factorial(number_of_odd_places)) / math.factorial(
            number_of_odd_places - len(vowels))
    print("Number of ways of arraning vowels = " + str(number_of_odd_places) + "P" + str(len(vowels)))
    print("Number of ways of arraning vowels = " + str(int(factorial_of_arranging_vowels)))

    return factorial_of_arranging_vowels


def arrangement_of_consonants(vowels_and_consonants, number_of_even_odd_places):
    consonants = vowels_and_consonants[1]
    number_of_even_places = number_of_even_odd_places[1]

    if number_of_even_places < len(consonants):
        number_of_even_places = len(consonants)
        factorial_of_arranging_consonants = math.factorial(number_of_even_places)

    else:
        factorial_of_arranging_consonants = (math.factorial(number_of_even_places)) / math.factorial(
            number_of_even_places - len(consonants))
    print("Number of ways of arraning consonants = " + str(number_of_even_places) + "P" + str(len(consonants)))
    print("Number of ways of arraning vowels = " + str(int(factorial_of_arranging_consonants)))

    return factorial_of_arranging_consonants


def separating_vowels_and_consonants(given_word, all_vowels):
    vowels = ""
    consonants = ""

    for letter in given_word:
        if letter in all_vowels:
            vowels += letter
        else:
            consonants += letter

    print("Vowels : '" + vowels + "'")
    print("Consonants : '" + consonants + "'")

    return vowels, consonants


def separating_odd_even_places(length_of_word):
    number_of_odd_places = 0
    number_of_even_places = 0

    for separating_odd_even in range(1, length_of_word + 1):
        if separating_odd_even % 2 == 0:
            number_of_even_places += 1

        else:
            number_of_odd_places += 1

    print("Number of odd places = " + str(number_of_odd_places))
    print("Number of even places = " + str(number_of_even_places))

    return number_of_odd_places, number_of_even_places


import math

given_word = input("Enter the word:").lower()
condition = input("Enter the condition like vowels in odd places:").lower()
all_vowels = ['a', 'e', 'i', 'o', 'u']
length_of_word = len(given_word)

print("Given word : " + given_word.upper())
print("Given condition : " + condition.upper())

number_of_even_odd_places = separating_odd_even_places(length_of_word)
vowels_and_consonants = separating_vowels_and_consonants(given_word, all_vowels)
arranging_of_consonants = arrangement_of_consonants(vowels_and_consonants, number_of_even_odd_places)
arranging_of_vowels = arrangement_of_vowels(vowels_and_consonants, number_of_even_odd_places)

arranging_vowels_in_odd_places = arranging_of_vowels * arranging_of_consonants
print("Arraning vowels in odd places = " + str(int(arranging_of_vowels)) + " * " + str(int(arranging_of_consonants)))
print("Arraning vowels in odd places = " + str(int(arranging_vowels_in_odd_places)))