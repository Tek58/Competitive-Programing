def fib(self, n: int) -> int:
    if n <= 1:
        return n
    else:
        return (self.fib((n-2)) + self.fib((n-1)))
