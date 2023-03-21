print("1.Trains and Bridges")
print("2.Train and platform and pole")
print("3.Two platforms and pole ")
x=int(input("which need to find:"))
if x==1:
    import Trains_and_bridge
    print(Trains_and_bridge)
elif  x==2:
    import Train_and_bridge_and_man
    print(Train_and_bridge_and_man)
else:
    import Two_platforms_and_pole
    print(Two_platforms_and_pole)