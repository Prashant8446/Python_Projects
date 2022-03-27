# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import math
from random_number_generator import random_number_class
from guessTheNumber import guessNumber



def mainDriver():

    randomNumberobj = random_number_class().randomNumber()

    guessNumberobj = guessNumber()
    guessNumberobj.guessTheNumber(randomNumberobj)


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainDriver()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
