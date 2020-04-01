def main():
    kitten('meoww', 'grr', 'purr')

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow')

if __name__ == "__main__": main()
    