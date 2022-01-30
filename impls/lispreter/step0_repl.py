def read(x):
    return x

def eval(x):
    return x

def _print(x):
    print(x)

def rep(x):
    _print(eval(read(x)))
    


if __name__ == '__main__':
    while True:
        inp = input("user> ")
        rep(inp)
            