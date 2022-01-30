from printer import pr_str
from reader import read_str
import getopt
import sys


def read(x):
    return read_str(x)


def eval(x):
    return x


def _print(x):
    print(pr_str(x))


def rep(x):
    _print(eval(read(x)))


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'd')
    isDebug = True if '-d' in [x[0] for x in opts] else False

    if isDebug:
        inp = '(+ 1 2)'
        rep(inp)

    else:
        while True:
            inp = input("user> ")
            rep(inp)
