from random_number_generator import random_number_class
import math

class guessNumber:


    def guessTheNumber(self,randomNumber):

        chances = round(math.log(randomNumber[2] - randomNumber[1] + 1, 2))
        print("chances", chances)

        count = 0

        while count < chances:
            count += 1
            guessed_number = int(input("Enter your guess "))
            print("you entered ", guessed_number, "for chance ", count)
            chances_remaining = chances - count

            if (guessed_number == randomNumber[0]):
                print("congrats you have guessed correct number in ", count, " chance")
                break
            elif (guessed_number > randomNumber[0]):
                print("Wrong: The guessed number is too large")
                print("chances remaining", chances_remaining)
            else:
                print("Wrong: guessed number is too small")
                print("chances remaining", chances_remaining)

        if (count >= chances):
            print("Your chances to guess the number are finished,/nBetter luck next time")


