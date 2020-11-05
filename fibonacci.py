class Fibonacci:

    
    def __init__(self, max):                      
        self.max = max
    
    def iter(self):
        a = 0
        b = 1
        result = [a]
        while a < self.max:
            a, b = b, a + b
            result.append(a)
        return result

