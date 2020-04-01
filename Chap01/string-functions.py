
class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'the number of bunnies is {self._n}'

x = bunny(47)
print(x)