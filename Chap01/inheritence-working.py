
class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

#getter setter. If t we set t / since no default we need to handle exceptions
    def type(self, t=None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return none

#getter setter. If t we set n / since no default we need to handle exceptions
    def name(self, n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return none

#getter setter. If t we set s / since no default we need to handle exceptions
    def sound(self, s=None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return none
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type'] #remove parent class kwargs and replace with inherited class kwargs
        super().__init__(**kwargs) #super allways calls the parent class


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type'] #remove parent class kwargs and replace with inherited class kwargs
        super().__init__(**kwargs) #super() allways calls the parent class

# def print_animal(o):
#     if not isinstance(o, Animal):
#         raise TypeError('print_animal(): requires an Animal')
#     print('The {} is named "{}" and says "{}".'.format(
#         o.type(), o.name(), o.sound()))


def main():
    a0 = Kitten( name='fluffy', sound='rwar')
    a1 = Duck( name='donald', sound='quack')
    print(a0)
    print(a1)


if __name__ == "__main__":
    main()
