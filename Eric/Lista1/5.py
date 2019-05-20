"""Sum of the even numbers of the fibonacci sequence"""


# yields the even-valued numbers of the fibonacci sequence
def fib(biggest):
    f, s = 0, 1
    while s < biggest:
        f, s = s, f + s
        if s % 2 == 0:
            yield s


def main():
    print(sum(fib(4000000)))


if __name__ == "__main__":
    main()
