def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(len(game))
    print_list(game)

def print_list(o):
    for i in o: print(i)
    print()

if __name__ == "__main__": main()
