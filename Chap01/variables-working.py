#Python doesn't have private variables

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'donald'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rrr'

#getter setter. If t we set t
    def type(self, t = None):
        if t: self._type = t
        return self._type

#getter setter. If t we set n
    def name(self, n = None):
        if n: self._name = n
        return self._name

#getter setter. If t we set s
    def sound(self, s = None):
        if s: self._sound = s
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(
        o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a0.name)

if __name__ == "__main__":
    main()
