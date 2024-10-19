class Fibonacci:
    def __init__(self) -> None:
        # Dictionary to store the already computed Fibonacci values
        self.__memo = {0: 0, 1: 1}

    
    def fib(self, number):
        #checking if the value is already computed
        if number in self.__memo:
            return self.__memo[number]
        
        # making use of memoization to compute fib value recursively
        self.__memo[number] = self.fib(number - 1) + self.fib(number - 2)
        return self.__memo[number]
    
    def get_series(self, number):
        # make use of nth number to generate the fib series
        series = [self.fib(i) for i in range(number + 1)]
        return series
    
    
if __name__ == "__main__":
    fibonacci = Fibonacci()

    try:
        number = int(input('Enter the fibonacii number to compute: '))
        if number < 0:
            raise ValueError("please enter a non-negative number.")
        
        print(f'The {number}th Fibonacci number is: {fibonacci.fib(number)}')
        print(f'The Fibonacci series up to {number} is: {fibonacci.get_series(number)}') 
    except ValueError as Er:
        print(Er)  