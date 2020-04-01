# import os


def main():
    infile = open('Chap01/lines.txt', 'rt')
    outfile = open('Chap01/lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

    # print(os.getcwd())


if __name__ == "__main__":
    main()
