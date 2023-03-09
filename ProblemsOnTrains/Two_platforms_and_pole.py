def calculating_speed_and_length_and_time_taken_to_cross(length_of_platform, length_of_second_platform , time_taken_to_cross_man, time_taken_to_cross_platform):
    speed_of_train = length_of_platform / (time_taken_to_cross_platform - time_taken_to_cross_man)
    length_of_train = speed_of_train * time_taken_to_cross_man
    time_taken_to_cross_second_platform=(length_of_train+length_of_second_platform)/speed_of_train
    print("Length of platform = " + str(length_of_platform))
    print("Length of second platform = "+str(length_of_second_platform))
    print("Time taken to cross the pole = " + str(time_taken_to_cross_man))
    print("Time taken to cross the platform = " + str(time_taken_to_cross_platform))
    print("Speed of train = (" + str(length_of_platform) + " / (" + str(time_taken_to_cross_platform) + " - " + str(time_taken_to_cross_man) + "))*18/5 ")
    print("Speed of train = " + str(speed_of_train * 18 / 5) + " km/hr")
    print("Length of train = " + str(speed_of_train) + "*5/18 *" + str(time_taken_to_cross_man))
    print("Length of train = " + str(length_of_train) + " m")
    print("Time taken to cross second platform = "+str(time_taken_to_cross_second_platform)+" secs")


def calculating_speed_and_length_of_the_train(length_and_time_of_first_platform,length_and_time_of_second_platform):
    length_of_first_platform=length_and_time_of_first_platform[0]
    time_taken_to_cross_first_platform=length_and_time_of_first_platform[1]
    length_of_second_platform=length_and_time_of_second_platform[0]
    time_taken_to_cross_second_platform=length_and_time_of_second_platform[1]

    if time_taken_to_cross_second_platform>time_taken_to_cross_first_platform:
        length_of_train=((length_of_second_platform*time_taken_to_cross_first_platform)-(length_of_first_platform*time_taken_to_cross_second_platform))/(time_taken_to_cross_second_platform-time_taken_to_cross_first_platform)
    else:
        length_of_train=((length_of_second_platform*time_taken_to_cross_first_platform)-(length_of_first_platform*time_taken_to_cross_second_platform))/(time_taken_to_cross_first_platform-time_taken_to_cross_second_platform)
    speed_of_train=(length_of_train+length_of_first_platform)/time_taken_to_cross_first_platform

    print("Length of first platform = "+str(length_of_first_platform))
    print("Length of second platform = "+str(length_of_second_platform))
    print("Time taken to cross first platform = "+str(time_taken_to_cross_first_platform))
    print("Time taken to cross second platform = "+str(time_taken_to_cross_second_platform))
    print("Length of train = "+str(length_of_train)+" m")
    print("Speed of train = "+str(speed_of_train*18/5)+" km/hr")

def calculating_time_taken_to_cross_second_platform(length_of_first_platform,length_of_second_platform,length_of_train,time_taken_to_cross_first_platform):
    speed_of_train=(length_of_train+length_of_first_platform)/time_taken_to_cross_first_platform
    time_taken_to_cross_second_platform=(length_of_second_platform+length_of_train)/speed_of_train

    print("Length of first platform = "+str(length_of_first_platform))
    print("Length of second platform = "+str(length_of_second_platform))
    print("Time taken to cross first platform = "+str(time_taken_to_cross_first_platform))
    print("Length fo train = "+str(length_of_train))
    print("Speed of train = "+str(speed_of_train))
    print("Time taken to cross the second platform = "+str(time_taken_to_cross_second_platform)+" secs")

need_to_find=input("Enter the input what need to find:")
if need_to_find=="time taken to cross the second platform":
    length_of_train=float(input("Enter the length of train:"))
    length_of_first_platform=float(input("Enter the length of first platform:"))
    time_taken_to_cross_first_platform=float(input("Enter the time taken to cross first platform:"))
    length_of_second_platform=float(input("Enter the length of second platform:"))
    calculating_time_taken_to_cross_second_platform(length_of_first_platform,length_of_second_platform,length_of_train,time_taken_to_cross_first_platform)

elif need_to_find=="speed and length of train":
    length_and_time_of_first_platform=list(map(float,input("Enter the length and time of first platform:").split()))
    length_and_time_of_second_platform=list(map(float,input("Enter the length and time of second platform:").split()))
    calculating_speed_and_length_of_the_train(length_and_time_of_first_platform,length_and_time_of_second_platform)
elif need_to_find=="speed and length and time taken to cross second platform":
    length_of_platform = float(input("Enter the length of the platform:"))
    time_taken_to_cross_platform = float(input("Enter the time taken to cross the platform:"))
    time_taken_to_cross_man = float(input("Enter the time taken to cross the man:"))
    length_of_second_platform=float(input("Enter the length of second platform:"))
    calculating_speed_and_length_and_time_taken_to_cross(length_of_platform,length_of_second_platform, time_taken_to_cross_man, time_taken_to_cross_platform)


else:
    print("Enter the valid input!!")