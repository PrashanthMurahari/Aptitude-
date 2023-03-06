def calculating_speed_of_another_train(total_length_of_two_trains, time_taken_to_each_other, speed_of_one_train):
    speed_condition = input("Enter the Speed measurement in kmph or metres:").lower()
    given_direction = input("Enter the direction:").lower()
    if given_direction == "opposite":

        if speed_condition == "kmph":
            speed_of_another_train = (total_length_of_two_trains / time_taken_to_each_other) * 18 / 5 - speed_of_one_train
            print("Length of two trains = " + str(total_length_of_two_trains))
            print("Time taken to cross each other = " + str(time_taken_to_each_other))
            print("Speed of another train = (" + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other) + ")*18/5 - " + str(speed_of_one_train))
            print("Speed of another train = " + str(round(speed_of_another_train, 2)) + " kmph")

        elif speed_condition == "metres":
            speed_of_another_train = (total_length_of_two_trains / time_taken_to_each_other) - speed_of_one_train
            print("Length of two trains = " + str(total_length_of_two_trains))
            print("Time taken to cross each other = " + str(time_taken_to_each_other))
            print("Speed of another train = " + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other) + " - " + str(speed_of_one_train))
            print("Speed of another train = " + str(round(speed_of_another_train, 2)) + " m/s")

    elif given_direction == "same direction":

        if speed_condition == "kmph":
            speed_of_another_train = (total_length_of_two_trains / time_taken_to_each_other) * 18 / 5 + speed_of_one_train
            print("Length of two trains = " + str(total_length_of_two_trains))
            print("Time taken to cross each other = " + str(time_taken_to_each_other))
            print("Speed of another train = (" + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other) + ")*18/5 - " + str(speed_of_one_train))
            print("Speed of another train = " + str(round(speed_of_another_train, 2)) + " kmph")

        elif speed_condition == "metres":
            speed_of_another_train = (total_length_of_two_trains / time_taken_to_each_other) + speed_of_one_train
            print("Length of two trains = " + str(total_length_of_two_trains))
            print("Time taken to cross each other = " + str(time_taken_to_each_other))
            print("Speed of another train = " + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other) + " - " + str(speed_of_one_train))
            print("Speed of another train = " + str(round(speed_of_another_train, 2)) + " m/s")


def calculating_equal_speeds_of_two_trains(total_length_of_two_trains, time_taken_to_each_other):
    need_speed_in = input("Enter the measurement of speed needed in kmph or metres: ").lower()

    if need_speed_in == "kmph":
        speed_of_two_trains = (total_length_of_two_trains / time_taken_to_each_other) * 18 / 5
        print("Length of two trains = " + str(total_length_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_each_other))
        print("Equal speeds of two trains = (" + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other) + ") *18/5")
        print("Equal speeds of two trains = " + str(round(speed_of_two_trains, 2)) + " kmph")
        print("Speed of each train = " + str(round(speed_of_two_trains / 2, 2)) + " kmph")

    elif need_speed_in == "metres":
        speed_of_two_trains = (total_length_of_two_trains / time_taken_to_each_other)
        print("Length of two trains = " + str(total_length_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_each_other))
        print("Equal speeds of two trains = " + str(total_length_of_two_trains) + " / " + str(time_taken_to_each_other))
        print("Equal speeds of two trains = " + str(round(speed_of_two_trains, 2)) + " m/s")
        print("Speed of each train = " + str(round(speed_of_two_trains / 2, 2)) + " m/s")


def calculating_time_to_cross_each_other(total_speed_of_two_trains, total_length_of_two_trains):
    speed_condition = input("Enter the measurement of speed in kmph or metres:").lower()

    if speed_condition == "kmph":
        time_taken_to_each_other = total_length_of_two_trains / (total_speed_of_two_trains * 5 / 18)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Length of two trains = " + str(total_length_of_two_trains))
        print("Time taken to cross each other = " + str(total_length_of_two_trains) + " / (" + str(total_speed_of_two_trains) + "*5/18)")
        print("Time taken to cross each other = " + str(round(time_taken_to_each_other, 2)) + " secs")

    elif speed_condition == "metres":
        time_taken_to_each_other = total_length_of_two_trains / (total_speed_of_two_trains)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Length of two trains = " + str(total_length_of_two_trains))
        print("Time taken to cross each other = " + str(total_length_of_two_trains) + " / " + str(total_speed_of_two_trains))
        print("Time taken to cross each other = " + str(round(time_taken_to_each_other, 2)) + " secs")


def main(speed_of_two_trains):
    speed_of_train_A = speed_of_two_trains[0]
    speed_of_train_B = speed_of_two_trains[1]
    given_direction = input("Enter the direction:").lower()

    if given_direction == "opposite":
        total_speed_of_two_trains = speed_of_train_A + speed_of_train_B
        print("Speed of train A = " + str(speed_of_train_A))
        print("Speed of train B = " + str(speed_of_train_B))


    elif given_direction == "same direction":
        if speed_of_train_A > speed_of_train_B:
            total_speed_of_two_trains = speed_of_train_A - speed_of_train_B
            print("Speed of train A = " + str(speed_of_train_A))
            print("Speed of train B = " + str(speed_of_train_B))

        else:
            total_speed_of_two_trains = speed_of_train_B - speed_of_train_A
            print("Speed of train A = " + str(speed_of_train_A))
            print("Speed of train B = " + str(speed_of_train_B))
    return total_speed_of_two_trains


given_situation = input("Enter the input like tow trains:").lower()
need_to_find = input("Enter the input what need to find:").lower()
length_of_two_trains = list(map(float, input("Enter the lengths of two trains:").split()))
total_length_of_two_trains = length_of_two_trains[0] + length_of_two_trains[1]

if given_situation == "two trains" and need_to_find == "time":
    speed_of_two_trains = list(map(float, input("Enter the speeds of two trains:").split()))
    total_speed_of_two_trains = main(speed_of_two_trains)
    calculating_time_to_cross_each_other(total_speed_of_two_trains, total_length_of_two_trains)

elif given_situation == "two trains" and need_to_find == "equal speed of two trains":
    time_taken_to_each_other = float(input("Enter the time taken to cross each other:"))
    calculating_equal_speeds_of_two_trains(total_length_of_two_trains, time_taken_to_each_other)

elif given_situation == "two trains" and need_to_find == "speed of one train":
    speed_of_one_train = float(input("Enter the speed of one train:"))
    time_taken_to_each_other = float(input("Enter the time taken to cross each other:"))
    calculating_speed_of_another_train(total_length_of_two_trains, time_taken_to_each_other, speed_of_one_train)