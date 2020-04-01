#list comprehension

def main():
    seq = range(11)
    #take the first list and multiply by 2
    seq2 = [x * 2 for x in seq]
    seq3 = [x for x in seq if x % 3 != 0]
    print_list(seq)
    print_list(seq2)
    print_list(seq3)

def print_list(o):
    for x in o: print(x, end = '')
    print()

if __name__ == "__main__": main()
