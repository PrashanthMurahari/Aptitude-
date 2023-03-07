def calculating_length_of_train(total_speed_of_train_and_man, time_taken_to_cross_the_man, speed_condition):
    if speed_condition == "kmph":
        length_of_train = (total_speed_of_train_and_man * 5 / 18) * time_taken_to_cross_the_man
        print("Time taken to cross = " + str(time_taken_to_cross_the_man))
        print("Length of train = (" + str(total_speed_of_train_and_man) + "*5/18) *" + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(round(length_of_train, 2)))
    elif speed_condition == "metres":
        length_of_train = (total_speed_of_train_and_man) * time_taken_to_cross_the_man
        print("Time taken to cross = " + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(total_speed_of_train_and_man) + " *" + str(time_taken_to_cross_the_man))
        print("Length of train = " + str(round(length_of_train, 2)))


def calculating_time_taken_to_cross(length_of_train, total_speed_of_train_and_man, speed_condition):
    if speed_condition == "kmph":
        time_taken_to_cross_the_man = length_of_train / (total_speed_of_train_and_man * 5 / 18)
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross = " + str(length_of_train) + " / (" + str(total_speed_of_train_and_man) + "*5/18)")
        print("Time taken to cross = " + str(round(time_taken_to_cross_the_man, 2)) + " secs")
    elif speed_condition == "metres":
        time_taken_to_cross_the_man = length_of_train / (total_speed_of_train_and_man)
        print("Length of train = " + str(length_of_train))
        print("Time taken to cross = " + str(length_of_train) + " / " + str(total_speed_of_train_and_man))
        print("Time taken to cross = " + str(round(time_taken_to_cross_the_man, 2)) + " secs")


def calculating_speed_of_train(time_taken_to_cross_the_man, length_of_train, speed_of_man, speed_condition,given_direction, given_situation):
    if given_direction == "opposite":
        if speed_condition == "kmph":
            speed_of_train = (length_of_train / time_taken_to_cross_the_man) - (speed_of_man * 5 / 18)
            print("Speed of " + given_situation + " = " + str(speed_of_man))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of train = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") - (" + str(speed_of_man) + "*5/18)")
            print("Speed of train = " + str(round(speed_of_train, 2)) + " kmph")

        elif speed_condition == "metres":
            speed_of_train = (length_of_train / time_taken_to_cross_the_man) - (speed_of_man)
            print("Speed of " + given_situation + " = " + str(speed_of_man))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of train = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") - " + str(speed_of_man))
            print("Speed of train = " + str(round(speed_of_train, 2)) + " m/s")
    elif given_direction == "same direction":
        if speed_condition == "kmph":
            speed_of_train = (length_of_train / time_taken_to_cross_the_man) + (speed_of_man * 5 / 18)
            print("Speed of " + given_situation + " = " + str(speed_of_man))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of train = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") + (" + str(speed_of_man) + "*5/18)")
            print("Speed of train = " + str(round(speed_of_train, 2)) + " kmph")
        elif speed_condition == "metres":
            speed_of_train = (length_of_train / time_taken_to_cross_the_man) + (speed_of_man)
            print("Speed of " + given_situation + " = " + str(speed_of_man))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of train = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") + " + str(speed_of_man))
            print("Speed of train = " + str(round(speed_of_train, 2)) + " m/s")


def calculating_speed_of_man(time_taken_to_cross_the_man, length_of_train, speed_of_train, speed_condition,given_direction, given_situation):
    if given_direction == "opposite":
        if speed_condition == "kmph":
            speed_of_man = (length_of_train / time_taken_to_cross_the_man) - (speed_of_train * 5 / 18)
            print("Speed of train = " + str(speed_of_train))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of " + given_situation + "  = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") - (" + str(speed_of_train) + "*5/18)")
            print("Speed of " + given_situation + "  = " + str(round(speed_of_man, 2)) + " kmph")

        elif speed_condition == "metres":
            speed_of_man = (length_of_train / time_taken_to_cross_the_man) - (speed_of_train)
            print("Speed of train = " + str(speed_of_train))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of " + given_situation + "  = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") - " + str(speed_of_train))
            print("Speed of " + given_situation + "  = " + str(round(speed_of_man, 2)) + " m/s")
    elif given_direction == "same direction":
        if speed_condition == "kmph":
            speed_of_man = (length_of_train / time_taken_to_cross_the_man) + (speed_of_train * 5 / 18)
            print("Speed of train = " + str(speed_of_train))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of " + given_situation + "  = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") + (" + str(speed_of_train) + "*5/18)")
            print("Speed of " + given_situation + "  = " + str(round(speed_of_man, 2)) + " kmph")

        elif speed_condition == "metres":
            speed_of_man = (length_of_train / time_taken_to_cross_the_man) + (speed_of_train)
            print("Speed of train = " + str(speed_of_train))
            print("Length of train = " + str(length_of_train))
            print("Time taken to cross " + given_situation + " = " + str(time_taken_to_cross_the_man))
            print("Speed of " + given_situation + "  = (" + str(length_of_train) + " / " + str(time_taken_to_cross_the_man) + ") + " + str(speed_of_train))
            print("Speed of " + given_situation + "  = " + str(round(speed_of_man, 2)) + " m/s")
def calculating_speeds(speeds_of_man_and_train, given_direction):
    if given_direction == "opposite":
        total_speed_of_train_and_man = speeds_of_man_and_train[0] + speeds_of_man_and_train[1]
        print("Speed of train = " + str(speeds_of_man_and_train[0]))
        print("speeds of man = " + str(speeds_of_man_and_train[1]))
    elif given_direction == "same direction":
        if speeds_of_man_and_train[0] > speeds_of_man_and_train[1]:
            total_speed_of_train_and_man = speeds_of_man_and_train[0] - speeds_of_man_and_train[1]
            print("Speed of train = " + str(speeds_of_man_and_train[0]))
            print("speeds of man = " + str(speeds_of_man_and_train[1]))
        else:
            total_speed_of_train_and_man = speeds_of_man_and_train[1] - speeds_of_man_and_train[0]
            print("Speed of train = " + str(speeds_of_man_and_train[0]))
            print("speeds of man = " + str(speeds_of_man_and_train[1]))
    return total_speed_of_train_and_man

given_situation = input("Enter the input like 'moving man':").lower()
need_to_find = input("Enter the input what need to find:").lower()
given_direction = input("Enter the direction:").lower()
speed_condition = input("Enter the measurement of speed in kmph or metres :").lower()
if given_situation == "moving man" or given_situation == "jogger":
    if need_to_find == "length of train":
        speeds_of_train_and_man = list(map(float, input("Enter the Speeds of train and man:").split()))
        time_taken_to_cross_the_man = float(input("Enter time taken to cross the man:"))
        total_speed_of_train_and_man = calculating_speeds(speeds_of_train_and_man, given_direction)
        calculating_length_of_train(total_speed_of_train_and_man, time_taken_to_cross_the_man, speed_condition)
    elif need_to_find == "time taken to cross":
        speeds_of_train_and_man = list(map(float, input("Enter the Speeds of train and man:").split()))
        total_speed_of_train_and_man = calculating_speeds(speeds_of_train_and_man, given_direction)
        length_of_train = float(input("Enter the length of train:"))
        calculating_time_taken_to_cross(length_of_train, total_speed_of_train_and_man, speed_condition)
    elif need_to_find == "speed of train":
        time_taken_to_cross_the_man = float(input("Enter time taken to cross the man:"))
        length_of_train = float(input("Enter the length of train:"))
        speed_of_man = float(input("Enter the speed of the man:"))
        calculating_speed_of_train(time_taken_to_cross_the_man, length_of_train, speed_of_man, speed_condition,given_direction, given_situation)
    elif need_to_find == "speed of man":
        time_taken_to_cross_the_man = float(input("Enter time taken to cross the man:"))
        length_of_train = float(input("Enter the length of train:"))
        speed_of_train = float(input("Enter the speed of the train:"))
        calculating_speed_of_man(time_taken_to_cross_the_man, length_of_train, speed_of_train, speed_condition,given_direction, given_situation)