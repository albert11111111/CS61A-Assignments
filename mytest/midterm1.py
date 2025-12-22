def delay(arg):
    print("a")
    def g():
        return arg
    return g


def h(g):
    return g
def g():
    return 1 