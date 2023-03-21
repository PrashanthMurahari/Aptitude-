print("1.Finding Lengths")
print("2.Finding Speed and Time")
print("3.Two trains and one pole")
x=int(input("which need to find:"))
if x==1:
    import Finding_lengths_of_two_trains
    print(Finding_lengths_of_two_trains)
elif x==2:
    import Finding_Speed_and_Time_of_two_trains
    print(Finding_Speed_and_Time_of_two_trains)
else:
    import Two_trains_and_pole_and_bridge
    print(Two_trains_and_pole_and_bridge)