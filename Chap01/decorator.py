# A Decorator is a special function that returns a wrapper function - WTF?
# Meta Programming

def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

@f1
def f3():
    print('this is f3')

f3()