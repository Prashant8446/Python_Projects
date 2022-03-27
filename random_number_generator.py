import random
class random_number_class:

    def __init__(self):
        print("in init: random")

    def randomNumber(self):


        self.Lower_Bound = int(input("Enter lower bound: "))
        self.Upper_Bound = int(input("Enter Upper bound: "))

        self.random_Number_is = random.randint(self.Lower_Bound, self.Upper_Bound)
        # print("random_Number_is: ", randomNumber.random_Number_is)

        return self.random_Number_is, self.Lower_Bound,self.Upper_Bound

