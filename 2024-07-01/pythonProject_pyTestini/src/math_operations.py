class MathOperations:
    def factorial(self, n):
        if n == 0:
            return 1
        elif n < 0:
            raise ValueError("Negetive numbers do not have a factorial.")
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
