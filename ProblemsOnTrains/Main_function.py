print("1.One Train")
print("2.Two trains")
print("3.Measurement Conversion")
x=int(input("which need to find:"))
if x==1:
    import Single_train
    print(Single_train)
elif x==2:
    import Two_trains
    print(Two_trains)
else:
    import Conversion_of_measurements
    print(Conversion_of_measurements)


