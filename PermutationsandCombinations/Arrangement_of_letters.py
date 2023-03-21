print("1.Arrange the letters ")
print("2.Vowels always be together")
print("3.Vowels never be together")
print("4.Vowels in odd places")
print("5.Vowels at two ends")
x=int(input("which type of arrangement do you need :"))
if x==1:
    import Arrange_the_letters
    print(Arrange_the_letters)
elif x==2:
    import Vowels_always_be_together
    print(Vowels_always_be_together)
elif x==3:
    import Vowels_never_be_together
    print(Vowels_never_be_together)
elif x==4:
    import Vowels_in_odd_places
    print(Vowels_in_odd_places)
else:
    import Vowels_at_two_ends
    print(Vowels_at_two_ends)