print("-> Time has to be given only in seconds")
given_situation = input("Enter the Input Of Type Like : Two Trains, Bridge, Man, Pole:").lower()
need_to_find = input("Enter the Input What Need to Find:").lower()
# Finding Time For Two Trains To Cross Each Other
if given_situation == "two trains" and need_to_find == "time":
    lengths_and_speeds_of_two_trains = list(map(float, input("Enter The Length and Speeds Of Trains:").split()))
    speed_condition = input("Enter the Speed in kmph or metres:").lower()
    length_of_trains_condition = input("Enter the distance given in km or metres:").lower()
    given_direction = input("Enter the direction:").lower()
    if given_direction == "opposite":
        if speed_condition == "kmph" and length_of_trains_condition == "km":
            speed_of_train_A = lengths_and_speeds_of_two_trains[1]
            calculated_speed_of_train_A_in_meters = speed_of_train_A * (5 / 18)
            speed_of_train_B = lengths_and_speeds_of_two_trains[3]
            calculated_speed_of_train_B_in_meters = speed_of_train_B * (5 / 18)
            total_speed_of_two_trains = calculated_speed_of_train_B_in_meters + calculated_speed_of_train_A_in_meters
            length_of_train_A = lengths_and_speeds_of_two_trains[0] * 1000
            length_of_train_B = lengths_and_speeds_of_two_trains[2] * 1000
            total_length_of_two_trains = length_of_train_B + length_of_train_A
            total_time_taken_to_cross_each_other = total_length_of_two_trains / total_speed_of_two_trains
            print("Length Of Train A = " + str(length_of_train_A) + "\n" + "Length Of Train B = " + str(
                length_of_train_B) + "\n" + "Total Length Of Two Trains = Length Of Train A + Length Of Train B" + "\n" + "Total Length Of Two Trains = " + str(
                total_length_of_two_trains))
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Total Speeds Of Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speeds Of Trains = " + str(
                total_speed_of_two_trains))
            print("Time Taken To Cross Each Other = " + str(total_length_of_two_trains) + "/" + str(
                total_speed_of_two_trains))
            if total_time_taken_to_cross_each_other > 60:
                print("Total Time Taken To Cross Each Other = " + str(
                    round(total_time_taken_to_cross_each_other // 60)) + " Min " + str(
                    round(total_time_taken_to_cross_each_other % 60)) + " secs")
            else:
                print("Time Taken To Cross Each Other = " + str(round(total_time_taken_to_cross_each_other, 1)))
        elif speed_condition == "kmph" and length_of_trains_condition == "metres":
            speed_of_train_A = lengths_and_speeds_of_two_trains[1]
            calculated_speed_of_train_A_in_meters = speed_of_train_A * (5 / 18)
            speed_of_train_B = lengths_and_speeds_of_two_trains[3]
            calculated_speed_of_train_B_in_meters = speed_of_train_B * (5 / 18)
            total_speed_of_two_trains = calculated_speed_of_train_B_in_meters + calculated_speed_of_train_A_in_meters
            length_of_train_A = lengths_and_speeds_of_two_trains[0]
            length_of_train_B = lengths_and_speeds_of_two_trains[2]
            total_length_of_two_trains = length_of_train_B + length_of_train_A
            total_time_taken_to_cross_each_other = total_length_of_two_trains / total_speed_of_two_trains
            print("Length Of Train A = " + str(length_of_train_A) + "\n" + "Length Of Train B = " + str(
                length_of_train_B) + "\n" + "Total Length Of Two Trains = Length Of Train A + Length Of Train B" + "\n" + "Total Length Of Two Trains = " + str(
                total_length_of_two_trains))
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Total Speeds Of Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speeds Of Trains = " + str(
                total_speed_of_two_trains))
            print("Time Taken To Cross Each Other = " + str(total_length_of_two_trains) + "/" + str(
                total_speed_of_two_trains))
            if total_time_taken_to_cross_each_other > 60:
                print("Total Time Taken To Cross Each Other = " + str(
                    round(total_time_taken_to_cross_each_other // 60)) + " Min " + str(
                    round(total_time_taken_to_cross_each_other % 60)) + " secs")
            else:
                print("Time Taken To Cross Each Other = " + str(round(total_time_taken_to_cross_each_other, 1)))
    elif given_direction == "same direction":

        if speed_condition == "kmph" and length_of_trains_condition == "km":
            speed_of_train_A = lengths_and_speeds_of_two_trains[1]
            calculated_speed_of_train_A_in_meters = speed_of_train_A * (5 / 18)
            speed_of_train_B = lengths_and_speeds_of_two_trains[3]
            calculated_speed_of_train_B_in_meters = speed_of_train_B * (5 / 18)
            length_of_train_A = lengths_and_speeds_of_two_trains[0] * 1000
            length_of_train_B = lengths_and_speeds_of_two_trains[2] * 1000
            if calculated_speed_of_train_B_in_meters > calculated_speed_of_train_A_in_meters:
                total_speed_of_two_trains = calculated_speed_of_train_B_in_meters - calculated_speed_of_train_A_in_meters
            else:
                total_speed_of_two_trains = calculated_speed_of_train_A_in_meters - calculated_speed_of_train_B_in_meters
            length_of_train_A = lengths_and_speeds_of_two_trains[0] * 1000
            length_of_train_B = lengths_and_speeds_of_two_trains[2] * 1000
            total_length_of_two_trains = length_of_train_B + length_of_train_A
            total_time_taken_to_cross_each_other = total_length_of_two_trains / total_speed_of_two_trains
            print("Length Of Train A = " + str(length_of_train_A) + "\n" + "Length Of Train B = " + str(
                length_of_train_B) + "\n" + "Total Length Of Two Trains = Length Of Train A + Length Of Train B" + "\n" + "Total Length Of Two Trains = " + str(
                total_length_of_two_trains))
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Total Speeds Of Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speeds Of Trains = " + str(
                total_speed_of_two_trains))
            print("Time Taken To Cross Each Other = " + str(total_length_of_two_trains) + "/" + str(
                total_speed_of_two_trains))
            if total_time_taken_to_cross_each_other > 60:
                print("Total Time Taken To Cross Each Other = " + str(
                    round(total_time_taken_to_cross_each_other // 60)) + " Min " + str(
                    round(total_time_taken_to_cross_each_other % 60)) + " secs")
            else:
                print("Time Taken To Cross Each Other = " + str(round(total_time_taken_to_cross_each_other, 1)))
        elif speed_condition == "kmph" and length_of_trains_condition == "metres":
            speed_of_train_A = lengths_and_speeds_of_two_trains[1]
            calculated_speed_of_train_A_in_meters = speed_of_train_A * (5 / 18)
            speed_of_train_B = lengths_and_speeds_of_two_trains[3]
            calculated_speed_of_train_B_in_meters = speed_of_train_B * (5 / 18)
            length_of_train_A = lengths_and_speeds_of_two_trains[0]
            length_of_train_B = lengths_and_speeds_of_two_trains[2]
            if calculated_speed_of_train_B_in_meters > calculated_speed_of_train_A_in_meters:
                total_speed_of_two_trains = calculated_speed_of_train_B_in_meters - calculated_speed_of_train_A_in_meters
            else:
                total_speed_of_two_trains = calculated_speed_of_train_A_in_meters - calculated_speed_of_train_B_in_meters
            length_of_train_B = lengths_and_speeds_of_two_trains[2]
            total_length_of_two_trains = length_of_train_B + length_of_train_A
            total_time_taken_to_cross_each_other = total_length_of_two_trains / total_speed_of_two_trains

            print("Length Of Train A = " + str(length_of_train_A) + "\n" + "Length Of Train B = " + str(
                length_of_train_B) + "\n" + "Total Length Of Two Trains = Length Of Train A + Length Of Train B" + "\n" + "Total Length Of Two Trains = " + str(
                total_length_of_two_trains))
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Total Speeds Of Trains = (Speed Of Train A - Speed Of Train B)*(5/18 )" + "\n" + "Total Speeds Of Trains = " + str(
                total_speed_of_two_trains))
            print("Time Taken To Cross Each Other = " + str(total_length_of_two_trains) + "/" + str(
                total_speed_of_two_trains))
            if total_time_taken_to_cross_each_other > 60:
                print("Total Time Taken To Cross Each Other = " + str(
                    round(total_time_taken_to_cross_each_other // 60)) + " Min " + str(
                    round(total_time_taken_to_cross_each_other % 60)) + " secs")
            else:
                print("Time Taken To Cross Each Other = " + str(round(total_time_taken_to_cross_each_other, 1)))
# Finding Speeds For Two trains and For one sinlge train
elif given_situation == "two trains" and need_to_find == "speed of two trains":
    lengths_of_two_trains = list(map(float, input("Enter the lengths of two trains:").split()))
    time_taken_to_cross = float(input("Enter the time to cross each other:"))
    need_the_speed_in = input("Enter the measurment in which you need the speed value:")
    given_direction = input("Enter the direction:")
    if need_the_speed_in == "kmph":
        length_of_train_A = lengths_of_two_trains[0]
        length_of_train_B = lengths_of_two_trains[1]
        total_length_of_two_trains = length_of_train_A + length_of_train_B
        total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross * (18 / 5)
        speed_of_each_train = total_speed_of_two_trains / 2
        print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(length_of_train_B))
        print("Time Taken To Cross Each Other = " + str(time_taken_to_cross))
        print(
            "Total Length Of Two Trains = Length Of Train-A + Length Of Train-B " + "\n" + "Total Length Of Two Trains = " + str(
                length_of_train_A) + " + " + str(length_of_train_B))
        print(
            "Total Speed Of Two Trains = Total Length Of Two Trains/Time Taken To Cross Each Other*(18/5)" + "\n" + "Total Speed Of Two Train = " + str(
                round(total_speed_of_two_trains, 2)))
        print("Speed Of Each Train = " + str(round(speed_of_each_train, 2)))
    elif need_the_speed_in == "metres":
        length_of_train_A = lengths_of_two_trains[0]
        length_of_train_B = lengths_of_two_trains[1]
        total_length_of_two_trains = length_of_train_A + length_of_train_B
        total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
        speed_of_each_train = total_speed_of_two_trains / 2
        print(round(speed_of_each_train, 2))

elif given_situation == "two trains" and need_to_find == "speed of one train":
    lengths_of_two_trains = list(map(float, input("Enter the lengths of two trains:").split()))
    time_taken_to_cross = float(input("Enter the time taken to cross eac other:"))
    speed_of_one_train = float(input("Enter the speed of one train:"))
    speed_of_one_train_given_in = input("Enter the measurment of speed of given train:").lower()
    need_the_speed_in = input("Enter the measurment of speed of another train in kmph or metres:").lower()
    given_direction = input("Enter the direction:").lower()
    if given_direction == "opposite":
        length_of_train_A = lengths_of_two_trains[0]
        length_of_train_B = lengths_of_two_trains[1]
        total_length_of_two_trains = length_of_train_A + length_of_train_B
        if speed_of_one_train_given_in == "kmph" and need_the_speed_in == "kmph":
            total_speed_of_two_trains = (total_length_of_two_trains / time_taken_to_cross) * (18 / 5)
            speed_of_another_train = total_speed_of_two_trains - speed_of_one_train
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) *(18/5)   ->(To convert into kmph we use 18/5)" + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")*(18/5)")
            print(
                "Speed Of Another Train = Total Speed Of Two trains - Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " - " + str(speed_of_one_train))
            print("Speed Of Another Train = " + str(round(speed_of_another_train, 1)) + " kmph")
        elif speed_of_one_train_given_in == "metres" and need_the_speed_in == "kmph":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = (total_speed_of_two_trains - speed_of_one_train) * (18 / 5)
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) " + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")")
            print(
                "Speed Of Another Train = Total Speed Of Two trains - Speed of One train *(18/5) " + "\n" + "Speed Of Another Train = (" + str(
                    total_speed_of_two_trains) + " - " + str(
                    speed_of_one_train) + ")*(18/5)   ->(To convert into kmph we use 18/5)")
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " kmph")
        elif speed_of_one_train_given_in == "kmph" and need_the_speed_in == "metres":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = total_speed_of_two_trains - (speed_of_one_train * (18 / 5))
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) *(18/5)   ->(To convert into kmph we use 18/5)" + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")")
            print(
                "Speed Of Another Train = Total Speed Of Two trains - Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " - (" + str(speed_of_one_train) + "*18/5")
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " metres")
        elif speed_of_one_train_given_in == "metres" and need_the_speed_in == "metres":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = (total_speed_of_two_trains - speed_of_one_train)
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) " + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")")
            print(
                "Speed Of Another Train = Total Speed Of Two trains - Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " - " + str(speed_of_one_train))
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " metres")
    elif given_direction == "same direction":
        length_of_train_A = lengths_of_two_trains[0]
        length_of_train_B = lengths_of_two_trains[1]
        total_length_of_two_trains = length_of_train_A + length_of_train_B
        if speed_of_one_train_given_in == "kmph" and need_the_speed_in == "kmph":
            total_speed_of_two_trains = (total_length_of_two_trains / time_taken_to_cross) * (18 / 5)
            speed_of_another_train = total_speed_of_two_trains + speed_of_one_train
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) *(18/5)   ->(To convert into kmph we use 18/5)" + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(
                    time_taken_to_cross) + ")*(18/5)   ->(To convert into kmph we use 18/5)")
            print(
                "Speed Of Another Train = Total Speed Of Two trains + Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " + " + str(speed_of_one_train))
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " kmph")
        elif speed_of_one_train_given_in == "metres" and need_the_speed_in == "kmph":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = (total_speed_of_two_trains + speed_of_one_train) * (18 / 5)
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other) " + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")")
            print(
                "Speed Of Another Train = Total Speed Of Two trains + Speed of One train" + "\n" + "Speed Of Another Train = (" + str(
                    total_speed_of_two_trains) + " + " + str(
                    speed_of_one_train) + ")*(18/5)   ->(To convert into kmph we use 18/5)")
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " kmph")
        elif speed_of_one_train_given_in == "kmph" and need_the_speed_in == "metres":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = total_speed_of_two_trains + (speed_of_one_train * (18 / 5))
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other)    ->(To convert into kmph we use 18/5)" + "\n" + "Total Speed Of Two trains = (" + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross) + ")*(18/5)")
            print(
                "Speed Of Another Train = Total Speed Of Two trains + Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " + (" + str(
                    speed_of_one_train) + "*(18/5))   ->(To convert into kmph we use 18/5)")
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " metres")
        elif speed_of_one_train_given_in == "metres" and need_the_speed_in == "metres":
            total_speed_of_two_trains = total_length_of_two_trains / time_taken_to_cross
            speed_of_another_train = (total_speed_of_two_trains + speed_of_one_train)
            print("Length Of Train-A = " + str(length_of_train_A) + "\n" + "Length Of Train-B = " + str(
                length_of_train_B) + "\n" + "Total Length of two trains = " + str(total_length_of_two_trains))
            print("Time Taken To Cross Each other = " + str(time_taken_to_cross))
            print(
                "Total Speed Of Two trains = (Total Length of two trains/Time Taken To Cross Each other)  " + "\n" + "Total Speed Of Two trains = " + str(
                    total_length_of_two_trains) + "/" + str(time_taken_to_cross))
            print(
                "Speed Of Another Train = Total Speed Of Two trains + Speed of One train" + "\n" + "Speed Of Another Train = " + str(
                    total_speed_of_two_trains) + " + " + str(speed_of_one_train))
            print("Speed Of Another Train " + str(round(speed_of_another_train, 1)) + " metres")
# Finding Lengths Of Two Trains and Also For One Train
elif given_situation == "two trains" and need_to_find == "length of two trains":
    speed_of_two_trains = list(map(float, input("Enter the speeds of two trains:").split()))
    time_taken_to_cross = float(input("Enter the time taken to cross each other:"))
    speed_condition = input("Enter the speed measurment in kmph or metres:").lower()
    given_direction = input("Enter the direction:").lower()
    speed_of_train_A = speed_of_two_trains[0]
    speed_of_train_B = speed_of_two_trains[1]
    if given_direction == "opposite":
        if speed_condition == "kmph":
            total_speed_of_two_trains = (speed_of_train_A + speed_of_train_B) * 5 / 18
            lengths_of_two_trains = total_speed_of_two_trains * time_taken_to_cross
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Time Taken To Cross Each Other = " + str(
                time_taken_to_cross) + "\n" + "Total Speed Of Two Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speed Of Two Trains = " + (
                              str(speed_of_train_A) + "  + " + str(speed_of_train_B)) + "")
            print(
                "Length Of Two Trains = Total Speed Of Two Trains * Time Taken To Cross Each Other " + "\n" + "Length Of Two Trains = " + str(
                    round(total_speed_of_two_trains, 2)) + " * " + str(
                    time_taken_to_cross) + "\n" + "Length Of Two Trains = " + str(
                    round(lengths_of_two_trains, 2)) + "\n" + "Length Of One Train = " + str(
                    round(lengths_of_two_trains / 2, 2)))
        elif speed_condition == "metres":
            total_speed_of_two_trains = (speed_of_train_A + speed_of_train_B)
            lengths_of_two_trains = total_speed_of_two_trains * time_taken_to_cross
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Time Taken To Cross Each Other = " + str(
                time_taken_to_cross) + "\n" + "Total Speed Of Two Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speed Of Two Trains = " + (
                              str(speed_of_train_A) + "  + " + str(speed_of_train_B)))
            print(
                "Length Of Two Trains = Total Speed Of Two Trains * Time Taken To Cross Each Other " + "\n" + "Length Of Two Trains = " + str(
                    round(total_speed_of_two_trains, 2)) + " * " + str(
                    time_taken_to_cross) + "\n" + "Length Of Two Trains = " + str(
                    round(lengths_of_two_trains, 2)) + "\n" + "Length Of One Train = " + str(
                    round(lengths_of_two_trains / 2, 2)))
    if given_direction == "same direction":
        if speed_condition == "kmph":
            if speed_of_train_A > speed_of_train_B:
                total_speed_of_two_trains = (speed_of_train_A - speed_of_train_B) * 5 / 18
            else:
                total_speed_of_two_trains = (speed_of_train_B - speed_of_train_A) * 5 / 18
            lengths_of_two_trains = total_speed_of_two_trains * time_taken_to_cross
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Time Taken To Cross Each Other = " + str(
                time_taken_to_cross) + "\n" + "Total Speed Of Two Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speed Of Two Trains = " + (
                              str(speed_of_train_A) + "  + " + str(speed_of_train_B)))
            print(
                "Length Of Two Trains = Total Speed Of Two Trains * Time Taken To Cross Each Other " + "\n" + "Length Of Two Trains = " + str(
                    round(total_speed_of_two_trains, 2)) + " * " + str(
                    time_taken_to_cross) + "\n" + "Length Of Two Trains = " + str(
                    round(lengths_of_two_trains, 2)) + "\n" + "Length Of One Train = " + str(
                    round(lengths_of_two_trains / 2, 2)))
        elif speed_condition == "metres":
            if speed_of_train_A > speed_of_train_B:
                total_speed_of_two_trains = (speed_of_train_A - speed_of_train_B)
            else:
                total_speed_of_two_trains = (speed_of_train_B - speed_of_train_A)
            lengths_of_two_trains = total_speed_of_two_trains * time_taken_to_cross
            print("Speed Of Train A = " + str(speed_of_train_A) + "\n" + "Speed Of Train B = " + str(
                speed_of_train_B) + "\n" + "Time Taken To Cross Each Other = " + str(
                time_taken_to_cross) + "\n" + "Total Speed Of Two Trains = Speed Of Train A + Speed Of Train B" + "\n" + "Total Speed Of Two Trains = " + (
                              str(speed_of_train_A) + "  + " + str(speed_of_train_B)))
            print(
                "Length Of Two Trains = Total Speed Of Two Trains * Time Taken To Cross Each Other " + "\n" + "Length Of Two Trains = " + str(
                    round(total_speed_of_two_trains, 2)) + " * " + str(
                    time_taken_to_cross) + "\n" + "Length Of Two Trains = " + str(
                    round(lengths_of_two_trains, 2)) + "\n" + "Length Of One Train = " + str(
                    round(lengths_of_two_trains / 2, 2)))
# Finding Time For Crossing A bridge Or A Platform Or A Tunnel
elif (given_situation == "tunnel" or given_situation == "bridge" or given_situation == "platform"):
    if need_to_find == "speed":
        lengths_of_train_and_bridge = list(
            map(float, input("Enter the lengths of train and given tunnel or bridge or platform:").split()))
        time_taken_to_cross = float(input("Enter the time taken to cross:"))
        speed_condition = input("Enter the speed measurement of which you needed in kmph or metres:")
        length_of_train = lengths_of_train_and_bridge[0]
        length_of_the_bridge = lengths_of_train_and_bridge[1]
        total_length_of_train_and_bridge = length_of_train + length_of_the_bridge
        if speed_condition == "kmph":
            speed_of_the_train = (total_length_of_train_and_bridge / time_taken_to_cross) * (18 / 5)
            print("Time Taken To Cross The " + given_situation + " = " + str(
                time_taken_to_cross) + " secs" + "\n" + "Length Of Train = " + str(
                length_of_train) + "\n" + "Length Of The " + given_situation + " = " + str(length_of_the_bridge))
            print("Total length = " + str(total_length_of_train_and_bridge))
            print("Speed Of The Train = (" + str(total_length_of_train_and_bridge) + "/" + str(
                time_taken_to_cross) + ")*18/5" + "\n" + "Speed Of The Train = " + str(
                round(speed_of_the_train, 2)) + "kmph")
        elif speed_condition == "metres":
            speed_of_the_train = (total_length_of_train_and_bridge / time_taken_to_cross)
            print("Time Taken To Cross The " + given_situation + " = " + str(
                time_taken_to_cross) + " secs" + "\n" + "Length Of Train = " + str(
                length_of_train) + "\n" + "Length Of The " + given_situation + " = " + str(length_of_the_bridge))
            print("Total length = " + str(total_length_of_train_and_bridge))
            print("Speed Of The Train = " + str(round(speed_of_the_train, 2)) + "m/s")
        else:
            print("Please enter valid input")
    elif need_to_find == "time":
        lengths_of_train_and_bridge = list(map(float, input("Enter the lengths of train and bridge:").split()))
        speed_of_the_train = float(input("Enter the speed of train:"))
        speed_condition = input("Enter the measurement of speed in kmph or metres:")
        length_of_train = lengths_of_train_and_bridge[0]
        length_of_the_bridge = lengths_of_train_and_bridge[1]
        total_length_of_train_and_bridge = length_of_train + length_of_the_bridge
        if speed_condition == "kmph":
            time_taken_to_cross = total_length_of_train_and_bridge / (speed_of_the_train * 5 / 18)
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Length Of The Train = " + str(
                length_of_train) + "\n" + "Length Of The " + given_situation + " = " + str(length_of_the_bridge))
            print("Total Length = " + str(total_length_of_train_and_bridge))
            print("Time Taken To Cross " + given_situation + " = " + str(total_length_of_train_and_bridge) + "/(" + (
                str(speed_of_the_train)) + ")*5/18")
            print("Time Taken To Cross " + given_situation + " = " + str(round(time_taken_to_cross, 2)))
        elif speed_condition == "metres":
            time_taken_to_cross = total_length_of_train_and_bridge / (speed_of_the_train)
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Length Of The Train = " + str(
                length_of_train) + "\n" + "Length Of The " + given_situation + " = " + str(length_of_the_bridge))
            print("Total Length = " + str(total_length_of_train_and_bridge))
            print("Time Taken To Cross " + given_situation + " = " + str(total_length_of_train_and_bridge) + "/" + (
                str(speed_of_the_train)))
            print("Time Taken To Cross " + given_situation + " = " + str(round(time_taken_to_cross, 2)))
        else:
            print("Please enter valid input")
    elif need_to_find == "equal lengths":
        time_taken_to_cross = float(input("Enter the time taken to cross:"))
        speed_of_the_train = float(input("Enter the speed of the train:"))
        speed_condition = input("Enter the measurement of speed in kmph or metres:")
        if speed_condition == "kmph":
            total_length_of_train_and_bridge = time_taken_to_cross * speed_of_the_train * 5 / 18
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross))
            print("Total Length = (Speed Of the Train*5/18) * Time Taken To Cross" + "\n" + "Total Length = " + str(
                round(total_length_of_train_and_bridge, 2)))
            print("Length Of " + given_situation + " = " + str(round(total_length_of_train_and_bridge / 2, 2)))
        elif speed_condition == "metres":
            total_length_of_train_and_bridge = time_taken_to_cross * speed_of_the_train
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross))
            print("Total Length = Speed Of the Train * Time Taken To Cross" + "\n" + "Total Length = " + str(
                round(total_length_of_train_and_bridge, 2)))
            print("Length Of " + given_situation + " = " + str(round(total_length_of_train_and_bridge / 2, 2)))
        else:
            print("Please enter valid input")
    elif need_to_find == "length of train":
        speed_of_the_train = float(input("Enter the speed of the train:"))
        time_taken_to_cross = float(input("Enter the time taken to cross:"))
        length_of_the_bridge = float(input("Enter the length of the bridge or tunnel or platform:"))
        speed_condition = input("Enter the measurement of speed in kmph o metres:")
        if speed_condition == "kmph":
            length_of_train = (time_taken_to_cross * speed_of_the_train * 5 / 18) - length_of_the_bridge
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross) + "\n" + "Length Of the " + given_situation + " = " + str(length_of_the_bridge))
            print(
                "Length Of the Train = ((Speed Of the Train*5/18) * Time Taken To Cross) - Length Of The " + given_situation + "\n" + "Length of the Train = " + str(
                    round(length_of_train, 2)))
        elif speed_condition == "metres":
            length_of_train = (time_taken_to_cross * speed_of_the_train) - length_of_the_bridge
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross) + "\n" + "Length Of the " + given_situation + " = " + str(length_of_the_bridge))
            print(
                "Length Of the Train = ((Speed Of the Train) * Time Taken To Cross) - Length Of The " + given_situation + "\n" + "Length of the Train = " + str(
                    round(length_of_train, 2)))
        else:
            print("Please enter valid input")
    elif need_to_find == "length of bridge":
        speed_of_the_train = float(input("Enter the speed of the train:"))
        time_taken_to_cross = float(input("Enter the time to cross the tunnel or bridge or platform:"))
        length_of_the_train = float(input("Enter the length of the train:"))
        speed_condition = input("Enter the speed measurment in kmph or metres:")
        if speed_condition == "kmph":
            length_of_bridge = (time_taken_to_cross * (speed_of_the_train * 5 / 18)) - length_of_the_train
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross) + "\n" + "Length Of the " + given_situation + " = " + str(length_of_the_train))
            print(
                "Length Of the " + given_situation + " = ((Speed Of the Train*5/18) * Time Taken To Cross) - Length Of The Train" + "\n" + "Length of the " + given_situation + " = ((Speed Of the Train) * Time Taken To Cross) - Length Of The Train  " + "\n" + "Length of The " + given_situation + " = " + str(
                    round(length_of_bridge, 2)))
        elif speed_condition == "metres":
            length_of_the_bridge = (time_taken_to_cross * speed_of_the_train) - length_of_the_train
            print("Speed Of the Train = " + str(speed_of_the_train) + "\n" + "Time Taken To Cross = " + str(
                time_taken_to_cross) + "\n" + "Length Of the " + given_situation + " = " + str(length_of_the_train))
            print(
                "Length Of the " + given_situation + " = ((Speed Of the Train) * Time Taken To Cross) - Length Of The Train" + "\n" + "Length of the " + given_situation + " = ((Speed Of the Train) * Time Taken To Cross) - Length Of The Train  " + "\n" + "Length of The " + given_situation + " = " + str(
                    round(length_of_the_bridge, 2)))
        else:
            print("Please enter valid input")
    else:
        print("Please enter valid input")
else:
    print("Please enter  valid input")
