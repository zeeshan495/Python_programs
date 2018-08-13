from Utility import *


class Gambler:

    utility = Utility()
    print("Please enter a number_of_times : ")
    number_of_times = utility.input_int_data()
    if number_of_times <= 0:
        print("check the input")
    else:
        loss = 0
        wins = 0
        x = 1
        # for x in range(1, number_of_times + 1):
        while x <= number_of_times :
            print("Please enter a stake : ")
            stake = utility.input_int_data()
            print("Please enter a goal : ")
            goal = utility.input_int_data()
            if (stake <= 0) or (goal <= 0) :
                print("please check the input")
            elif goal== stake or goal < stake:
                print("you already reached goal")
            else:
                amount = stake
                while (amount > 0) and (amount < goal):
                    rand_num = random.random()
                    if (rand_num > 0.5):
                        amount = amount + 1
                    else:
                        amount = amount - 1
                if (amount == goal):
                    wins = wins + 1
                    print("win")
                else:
                    loss = loss + 1
                    print("loss")
                x +=1

        print("total number of wins " + str(wins))
        print("percentage of win " + str((100.0 * wins) / number_of_times))
        print("percentage of loss " + str((100.0 * loss) / number_of_times))