def calculating_time_taken_to_cross(speed_of_the_train, total_length_of_train_and_bridge, speed_condition):
    if speed_condition == "kmph":

        time_taken_to_cross = total_length_of_train_and_bridge / (speed_of_the_train * 5 / 18)
        if time_taken_to_cross<60:

            print("Length of train and bridge = " + str(total_length_of_train_and_bridge))
            print("Speed of train = " + str(speed_of_the_train))
            print("Time taken to cross = " + str(total_length_of_train_and_bridge) + " / (" + str(speed_of_the_train) + " *5/18)")
            print("Time taken to cross = " + str(round(time_taken_to_cross, 2)) + " secs")
        else:
            print("Length of train and bridge = " + str(total_length_of_train_and_bridge))
            print("Speed of train = " + str(speed_of_the_train))
            print("Time taken to cross = " + str(total_length_of_train_and_bridge) + " / (" + str(speed_of_the_train) + " *5/18)")
            print("Time taken to cross = "+str(round(time_taken_to_cross//60))+" min "+str(round(time_taken_to_cross%60))+" secs")
    elif speed_condition == "metres":
        time_taken_to_cross = total_length_of_train_and_bridge / (speed_of_the_train)
        print("Length of train and bridge = " + str(total_length_of_train_and_bridge))
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(total_length_of_train_and_bridge) + " / " + str(speed_of_the_train))
        print("Time taken to cross = " + str(round(time_taken_to_cross, 2)) + " secs")


def calculating_speed_of_train(total_length_of_train_and_bridge, speed_condition, time_taken_to_cross):
    if speed_condition == "kmph":
        speed_of_the_train = (total_length_of_train_and_bridge / time_taken_to_cross) * 18 / 5
        print("Length of train and bridge = " + str(total_length_of_train_and_bridge))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Speed of train = " + str(total_length_of_train_and_bridge) + " / (" + str(time_taken_to_cross) + " *18/5)")
        print("Speed of train = " + str(round(speed_of_the_train, 2)) + " kmph")
    elif speed_condition == "metres":
        speed_of_the_train = (total_length_of_train_and_bridge / time_taken_to_cross)
        print("Length of train and bridge = " + str(total_length_of_train_and_bridge))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Speed of train = " + str(total_length_of_train_and_bridge) + " / " + str(time_taken_to_cross))
        print("Speed of train = " + str(round(speed_of_the_train, 2)) + " m/s")


def calculating_lengths_of_train_and_bridge(speed_of_the_train, time_taken_to_cross, speed_condition):
    if speed_condition == "kmph":
        lengths_of_train_and_bridge = (speed_of_the_train * 5 / 18) * time_taken_to_cross
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Lengths of train and bridge = (" + str(speed_of_the_train) + "*5/18) * " + str(time_taken_to_cross))
        print("Lengths of train and bridge = " + str(round(lengths_of_train_and_bridge, 2)))
        print("Length of train or bridge = " + str(round(lengths_of_train_and_bridge / 2, 2)))
    elif speed_condition == "metres":
        lengths_of_train_and_bridge = (speed_of_the_train) * time_taken_to_cross
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Lengths of train and bridge = " + str(speed_of_the_train) + " * " + str(time_taken_to_cross))
        print("Lengths of train and bridge = " + str(round(lengths_of_train_and_bridge, 2)))
        print("Length of train or bridge = " + str(round(lengths_of_train_and_bridge / 2, 2)))


def calculating_length_of_train(speed_of_the_train, time_taken_to_cross, length_of_bridge, speed_condition):
    if speed_condition == "kmph":
        length_of_train = ((speed_of_the_train * 5 / 18) * time_taken_to_cross) - length_of_bridge
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Length of bridge = " + str(length_of_bridge))
        print("Length of train = (" + str(speed_of_the_train) + "*5/18) * " + str(time_taken_to_cross) + " - " + str(length_of_bridge))
        print("Length of train = " + str(round(length_of_train, 2)))

    elif speed_condition == "metres":
        lengths_of_train_and_bridge = (speed_of_the_train) * time_taken_to_cross - length_of_bridge
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Length of bridge = " + str(length_of_bridge))
        print("Length of train = " + str(speed_of_the_train) + " * " + str(time_taken_to_cross) + " - " + str(length_of_bridge))
        print("Length of train = " + str(round(lengths_of_train_and_bridge, 2)))


def calculating_length_of_bridge(speed_of_the_train, time_taken_to_cross, length_of_train, speed_condition):
    if speed_condition == "kmph":
        length_of_bridge = ((speed_of_the_train * 5 / 18) * time_taken_to_cross) - length_of_train
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Length of train = " + str(length_of_train))
        print("Length of bridge = (" + str(speed_of_the_train) + "*5/18) * " + str(time_taken_to_cross) + " - " + str(length_of_train))
        print("Length of bridge = " + str(round(length_of_bridge, 2)))

    elif speed_condition == "metres":
        length_of_bridge = (speed_of_the_train) * time_taken_to_cross - length_of_train
        print("Speed of train = " + str(speed_of_the_train))
        print("Time taken to cross = " + str(time_taken_to_cross))
        print("Length of train = " + str(length_of_train))
        print("Length of bridge = " + str(speed_of_the_train) + " * " + str(time_taken_to_cross) + " - " + str(length_of_train))
        print("Length of bridge = " + str(round(length_of_bridge, 2)))


need_to_find = input("Enter the input what need to find:").lower()
speed_condition = input("Enter the measurement of speed in kmph or metres:").lower()


if need_to_find == "time" or need_to_find == "speed":
    lengths_of_train_and_bridge = list(map(float, input("Enter the lengths of train and the bridge:").split()))
    total_length_of_train_and_bridge = lengths_of_train_and_bridge[0] + lengths_of_train_and_bridge[1]
    if need_to_find == "time":
        speed_of_the_train = float(input("Enter the Speed of train:"))
        calculating_time_taken_to_cross(speed_of_the_train, total_length_of_train_and_bridge, speed_condition)
    elif need_to_find == "speed":
        time_taken_to_cross = float(input("Enter the time taken to cross :"))
        calculating_speed_of_train(total_length_of_train_and_bridge, speed_condition, time_taken_to_cross)

elif need_to_find == "lengths of train and bridge" or need_to_find == "length of train" or need_to_find == "length of bridge":
    time_taken_to_cross = float(input("Enter the time taken to cross :"))
    speed_of_the_train = float(input("Enter the Speed of train:"))
    if need_to_find == "lengths of train and bridge":
        calculating_lengths_of_train_and_bridge(speed_of_the_train, time_taken_to_cross, speed_condition)
    elif need_to_find == "length of train":
        length_of_bridge = float(input("Enter the length of the bridge:"))
        calculating_length_of_train(speed_of_the_train, time_taken_to_cross, length_of_bridge, speed_condition)
    elif need_to_find == "length of bridge":
        length_of_train = float(input("Enter the length of the train:"))
        calculating_length_of_bridge(speed_of_the_train, time_taken_to_cross, length_of_train, speed_condition)