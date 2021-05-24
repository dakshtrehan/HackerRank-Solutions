class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum({i for i in range(1, n+1) if n % i == 0})
