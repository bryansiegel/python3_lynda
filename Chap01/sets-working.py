#A set does not allow duplicate elements

def main():
    a = set('We need a bigger boat')
    b = set('Sorry you cannot do that')
    # print_set(a)
    # print_set(b)

    #check member that's in set a but not set b
    print_set(a - b)
    #check member that's in both
    print_set(a & b)
    #check either member
    print_set(a | b)
    #forgot what this one was
    print_set(a ^ b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == "__main__": main()
