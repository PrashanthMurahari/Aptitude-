def calculating_speed_and_length_of_train(length_of_platform,time_taken_to_cross_man,time_taken_to_cross_platform):
    speed_of_train=length_of_platform/(time_taken_to_cross_platform-time_taken_to_cross_man)
    length_of_train=speed_of_train*time_taken_to_cross_man
    print("Length of platform = "+str(length_of_platform))
    print("Time taken to cross the pole = "+str(time_taken_to_cross_man))
    print("Time taken to cross the platform = "+str(time_taken_to_cross_platform))
    print("Speed of train = ("+str(length_of_platform)+" / ("+str(time_taken_to_cross_platform)+" - "+str(time_taken_to_cross_man)+"))*18/5 ")
    print("Speed of train = "+str(speed_of_train*18/5)+" km/hr")
    print("Length of train = "+str(speed_of_train)+"*5/18 *"+str(time_taken_to_cross_man))
    print("Length of train = "+str(length_of_train)+" m")
def calculating_time_taken_to_cross_pole(time_taken_to_cross_platform,speed_of_train,length_of_platform):
    length_of_train=((speed_of_train*5/18)*time_taken_to_cross_platform) - length_of_platform
    time_taken_to_cross_man=length_of_train/(speed_of_train*5/18)
    print("Speed of train = "+str(speed_of_train))
    print("Length of platform = "+str(length_of_platform))
    print("Time taken to cross the platform = "+str(time_taken_to_cross_platform))
    print("Length of the train = "+str(speed_of_train)+"*5/18 *"+str(time_taken_to_cross_platform)+" - "+str(length_of_platform))
    print("Length of the train = "+str(length_of_train))
    print("Time taken to cross the pole = "+str(length_of_train)+" / "+str(speed_of_train)+"*5/18")
    print("Time taken to cross the pole = "+str(time_taken_to_cross_man)+" secs")

def calculating_length_of_platform(time_taken_to_cross_platform,time_taken_to_cross_man,speed_of_train):
    train_length=(speed_of_train*5/18)*time_taken_to_cross_man
    length_of_the_platform =((speed_of_train*5/18)*time_taken_to_cross_platform)-train_length
    print("Speed of the train = "+str(speed_of_train))
    print("Time taken to cross the man = "+str(time_taken_to_cross_man))
    print("Length of the train = "+str(speed_of_train)+"*5/18 * "+str(time_taken_to_cross_man))
    print("Length of the train = "+str(train_length))
    print("Time taken to cross the platform = "+str(time_taken_to_cross_platform))
    print("Length of the platform = "+str(speed_of_train)+"*5/18 *"+str(time_taken_to_cross_platform)+" - "+str(train_length))
    print("Length of the platform = "+str(length_of_the_platform)+" m")

need_to_find=input("Enter the input which need need to find:").lower()
if need_to_find=="length of platform":
    time_taken_to_cross_platform=float(input("Enter the time taken to cross the platform:"))
    time_taken_to_cross_man=float(input("Enter the time taken to cross the man:"))
    speed_of_train=float(input("Enter the speed of the train:"))
    calculating_length_of_platform(time_taken_to_cross_platform,time_taken_to_cross_man,speed_of_train)
elif need_to_find=="time taken to cross pole":
    time_taken_to_cross_platform = float(input("Enter the time taken to cross the platform:"))
    speed_of_train = float(input("Enter the speed of the train:"))
    length_of_platform=float(input("Enter the length of the platform:"))
    calculating_time_taken_to_cross_pole(time_taken_to_cross_platform,speed_of_train,length_of_platform)
elif need_to_find=="speed and length of train":
    length_of_platform = float(input("Enter the length of the platform:"))
    time_taken_to_cross_platform = float(input("Enter the time taken to cross the platform:"))
    time_taken_to_cross_man = float(input("Enter the time taken to cross the man:"))
    calculating_speed_and_length_of_train(length_of_platform,time_taken_to_cross_man,time_taken_to_cross_platform)
else:
    print("Enetr the valid input!!")

