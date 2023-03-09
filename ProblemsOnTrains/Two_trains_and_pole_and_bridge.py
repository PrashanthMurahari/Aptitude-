def calculating_time_taken_to_cross_second_train(length_of_platform,length_of_second_train,speed_of_first_train,speed_of_second_train,time_taken_to_cross_platform):
    length_of_first_train = (speed_of_first_train*5/18 *time_taken_to_cross_platform) - length_of_platform
    time_taken_to_cross_second_train=(length_of_second_train+length_of_first_train)/((speed_of_first_train+speed_of_second_train)*5/18)
    print("Speed of first train = "+str(speed_of_first_train))
    print("Time taken to cross the platform = "+str(time_taken_to_cross_platform))
    print("Length of platform = "+str(length_of_platform))
    print("Length of first train = "+str(length_of_first_train))
    print("Speed of second train = "+str(speed_of_second_train))
    print("Length of second train = "+str(length_of_second_train))
    print("Time taken to cross the second train = "+str(time_taken_to_cross_second_train))

def calculating_speed_and_time_taken_to_cross_second_train(length_of_first_train,time_taken_to_cross_second_train,time_taken_to_cross_pole):
    speed_of_train=length_of_first_train/time_taken_to_cross_pole
    length_of_second_train=(speed_of_train*time_taken_to_cross_second_train) - length_of_first_train
    print("Time taken to cross pole = "+str(time_taken_to_cross_pole))
    print("Length of first train = "+str(length_of_first_train))
    print("Speed of train = "+str(speed_of_train*18/5))
    print("Time taken to cross second train = "+str(time_taken_to_cross_second_train))
    print("Length of second train = "+str(length_of_second_train))

def calculating_speed_and_time_taken_to_cross_each_other(length_and_time_of_second_train,length_and_time_of_first_train):
    length_of_first_train=length_and_time_of_first_train[0]
    length_of_second_train=length_and_time_of_second_train[0]
    time_taken_by_first_train=length_and_time_of_first_train[1]
    time_taken_by_second_train=length_and_time_of_second_train[1]

    speed_of_first_train=length_of_first_train/time_taken_by_first_train
    speed_of_second_train=length_of_second_train/time_taken_by_second_train
    time_taken_to_cross_each_other=(length_of_first_train+length_of_second_train)/(speed_of_first_train+speed_of_second_train)

    print("Length of first train = "+str(length_of_first_train))
    print("Length of second train = "+str(length_of_second_train))
    print("Time taken by first train to cross pole = "+str(time_taken_by_first_train))
    print("Time taken by second train to cross pole = "+str(time_taken_by_second_train))
    print("Speed of first train = "+str(speed_of_first_train*18/5))
    print("Speed of second train = "+str(speed_of_second_train*18/5))
    print("Time taken to cross each other = "+str(length_of_first_train)+" + "+str(length_of_second_train)+" / "+str(speed_of_first_train)+" + "+str(speed_of_second_train))
    print("Time taken to cross each other = "+str(time_taken_to_cross_each_other)+" secs")

need_to_find=input("Enter the input what to be find:").lower()
if need_to_find=="time taken to cross each other in opposite direction":
    length_and_time_of_first_train=list(map(float,input("Enter the length and time of first train:").split()))
    length_and_time_of_second_train=list(map(float,input("Enter the length and time of second train:").split()))
    calculating_speed_and_time_taken_to_cross_each_other(length_and_time_of_second_train,length_and_time_of_first_train)
elif need_to_find=="length of second train":
    length_of_first_train=float(input("Enter the length of first train:"))
    time_taken_to_cross_pole=float(input("Enter the time taken to cross the pole:"))
    time_taken_to_cross_second_train=float(input("Enter the time taken to cross second train:"))
    calculating_speed_and_time_taken_to_cross_second_train(length_of_first_train,time_taken_to_cross_second_train,time_taken_to_cross_pole)
elif need_to_find=="time taken to cross the second train":
    length_of_platform=float(input("Enter the length of platform:"))
    time_taken_to_cross_platform=float(input("Enter the time taken to cross the platform:"))
    speed_of_first_train=float(input("Enter the speed of first train:"))
    speed_of_second_train=float(input("Enter the speed of second train:"))
    length_of_second_train=float(input("Enter the length of second train:"))
    calculating_time_taken_to_cross_second_train(length_of_platform,length_of_second_train,speed_of_first_train,speed_of_second_train,time_taken_to_cross_platform)
else:
    print("Enter the valid input!!")