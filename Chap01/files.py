# import os


def main():
    # f = open('lines.txt')
    f = open('lines.txt', 'r')
    for line in f:
        print(line.rstrip())

    # print(os.getcwd())


if __name__ == "__main__":
    main()
