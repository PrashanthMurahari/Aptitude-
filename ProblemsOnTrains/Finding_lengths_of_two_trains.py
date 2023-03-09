def calculating_lengths_of_two_trains(total_speed_of_two_trains, time_taken_to_cross, speed_condition):


    if speed_condition == "kmph":
        lengths_of_two_trains=((total_speed_of_two_trains * 5/18) * time_taken_to_cross)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_cross))
        print("Lengths of two trains = (" + str(total_speed_of_two_trains) + " * 5/18) * " + str(time_taken_to_cross))
        print("Lengths of two trains = " + str(round(lengths_of_two_trains,2)))
        print("Length of each train = " + str(round(lengths_of_two_trains/2,2)))

    elif speed_condition == "metres":
        lengths_of_two_trains = ((total_speed_of_two_trains) * time_taken_to_cross)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_cross))
        print("Lengths of two trains = " + str(total_speed_of_two_trains) + " * " + str(time_taken_to_cross))
        print("Lengths of two trains = " + str(round(lengths_of_two_trains,2)))
        print("Length of each train = " + str(round(lengths_of_two_trains/2,2)))

def calculating_length_of_one_train(total_speed_of_two_trains, time_taken_to_cross, length_of_one_train, speed_condition):


    if speed_condition == "kmph":
        lengths_of_another_train = (((total_speed_of_two_trains * 5/18) * time_taken_to_cross) - length_of_one_train)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_cross))
        print("Length of one train = " + str(length_of_one_train))
        print("Length of another train = ((" + str(total_speed_of_two_trains) + " * 5/18) * " + str(time_taken_to_cross) + ") - "+str(length_of_one_train))
        print("Length of another train = " + str(lengths_of_another_train))

    elif speed_condition == "metres":
        lengths_of_another_train = (((total_speed_of_two_trains) * time_taken_to_cross) - length_of_one_train)
        print("Total speed of two trains = " + str(total_speed_of_two_trains))
        print("Time taken to cross each other = " + str(time_taken_to_cross))
        print("Length of one train = " + str(length_of_one_train))
        print("Length of another train = (" + str(total_speed_of_two_trains) + " * " + str(time_taken_to_cross) + ") - "+str(length_of_one_train))
        print("Length of another train = " + str(lengths_of_another_train))


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


need_to_find = input("Enter what need to find ? :").lower()
if  need_to_find == "length of two trains":
    speed_of_two_trains = list(map(float,input("Enter the speeds of two trains:").split()))
    time_taken_to_cross = float(input("Enter the time taken to cross:"))
    speed_condition = input("Enter the speed measurement given in kmph or metres:").lower()
    total_speed_of_two_trains = main(speed_of_two_trains)
    calculating_lengths_of_two_trains(total_speed_of_two_trains, time_taken_to_cross,speed_condition)

elif  need_to_find == "length of one train":
    speed_of_two_trains = list(map(float,input("Enter the speeds of two trains:").split()))
    time_taken_to_cross = float(input("Enter the time taken to cross:"))
    length_of_one_train = float(input("Enter the length of the train:"))
    speed_condition = input("Enter the speed measurement given in kmph or metres:").lower()
    total_speed_of_two_trains = main(speed_of_two_trains)
    calculating_length_of_one_train(total_speed_of_two_trains, time_taken_to_cross, length_of_one_train,speed_condition)
