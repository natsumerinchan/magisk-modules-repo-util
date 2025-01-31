
class Print:
    @classmethod
    def header(cls, string):
        print("\033[01;36m", end="")
        for x in range(0, len(string) + 6):
            print("=", end="")
        print("\n== %s ==" % string)
        for x in range(0, len(string) + 6):
            print("=", end="")
        print("\n\033[0m", end="")

    @classmethod
    def value(cls, tag, msg, *, end: str = "\n"):
        print("\033[01;34m== {0}\033[0m".format(tag), end="")
        print("\033[01;32m -> \033[0m", end="")
        print("\033[01;31m{0}\033[0m".format(msg), end=end)

