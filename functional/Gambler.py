from Utility import *


class Gambler:
    utility = Utility()
    stake = int(input("Please enter a stake : "))
    goal = int(input("Please enter a goal : "))
    number_of_times = int(input("Please enter a number_of_times : "))
    utility.game(stake,goal,number_of_times)
