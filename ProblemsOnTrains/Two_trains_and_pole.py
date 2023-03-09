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
