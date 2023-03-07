def calculating_time_to_cross_the_man(speed_of_train, length_of_train, speed_condition):
    if speed_condition == "kmph":
        time_taken_to_cross_the_man = length_of_train / (speed_of_train * 5 / 18)
        print("Speed of train = " + str(speed_of_train) + " * 5/18")
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(length_of_train) + "/(" + str(
            speed_of_train) + "*5/18)")
        print("Time taken to cross " + str(given_situation) + " = " + str(
            round(time_taken_to_cross_the_man, 2)) + " secs")
    elif speed_condition == "metres":
        time_taken_to_cross_the_man = length_of_train / (speed_of_train)
        print("Speed of train = " + str(speed_of_train) + " ")
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(length_of_train) + "/" + str(speed_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(
            round(time_taken_to_cross_the_man, 2)) + " secs")


def calculating_speed_of_train(time_taken_to_cross_the_man, length_of_train, speed_condition):
    if speed_condition == "kmph":
        speed_of_train = (length_of_train / time_taken_to_cross_the_man) * 18 / 5
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(time_taken_to_cross_the_man))
        print("Speed of train = (" + str(length_of_train) + "/" + str(time_taken_to_cross_the_man) + ")*18/5")
        print("Speed of train = " + str(round(speed_of_train, 2)) + " kmph")
    elif speed_condition == "metres":
        speed_of_train = (length_of_train / time_taken_to_cross_the_man)
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(time_taken_to_cross_the_man))
        print("Speed of train = " + str(length_of_train) + "/" + str(time_taken_to_cross_the_man))
        print("Speed of train = " + str(round(speed_of_train, 2)) + " m/s")


def calculating_length_of_the_train(time_taken_to_cross_the_man, speed_of_train, speed_condition):
    if speed_condition == "kmph":
        length_of_train = (speed_of_train * 5 / 18) * time_taken_to_cross_the_man
        print("Speed of train = " + str(speed_of_train) + " * 5/18")
        print("Time taken to cross " + str(given_situation) + " = " + str(time_taken_to_cross_the_man))
        print("Length of train = (" + str(speed_of_train) + "*5/18) * " + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(round(length_of_train, 2)))
    elif speed_condition == "metres":
        length_of_train = speed_of_train * time_taken_to_cross_the_man
        print("Speed of train = " + str(speed_of_train))
        print("Time taken to cross " + str(given_situation) + " = " + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(speed_of_train) + " * " + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(round(length_of_train, 2)))


given_situation = input("Enter the input like man or pole:").lower()
need_to_find = input("Enter the input what need to find:").lower()
speed_condition = input("Enter the measurement of speed in kmph or metres:").lower()
if given_situation == "man" or given_situation == "pole" or given_situation == "telegraph post":
    if need_to_find == "time":
        speed_of_train = float(input("Enter the speed of train:"))
        length_of_train = float(input("Enter the length of train:"))
        calculating_time_to_cross_the_man(speed_of_train, length_of_train, speed_condition)
    elif need_to_find == "speed":
        time_taken_to_cross_the_man = float(input("Enter the time taken to cross the man:"))
        length_of_train = float(input("Enter the length of  train:"))
        calculating_speed_of_train(time_taken_to_cross_the_man, length_of_train, speed_condition)
    elif need_to_find == "length of train":
        time_taken_to_cross_the_man = float(input("Enter the time taken to cross the man:"))
        speed_of_train = float(input("Enter the speed of train:"))
        calculating_length_of_the_train(time_taken_to_cross_the_man, speed_of_train, speed_condition)
    else:
        print("Enter valid input")