import numpy as np
class nb():

    def __init__(self,number):
        if type(number) != type(0):
            print "Initlize with a number"
            return None
        if number <= 0 :
            print "Should bigger than 0"
        else:
            self.number = number

    def divisor(self):
        """
        return the divisor of the number.
        return type: list
        """
        result = [1]
        sqrt_root = int(np.sqrt(self.number))+1
        for i in xrange(2, sqrt_root):
            if self.number%i == 0:
                result.append(self.number/i)
                result.append(i)
        return list(set(result))

    def div_sum(self):
        tmp = self.divisor()
        return sum(tmp)

