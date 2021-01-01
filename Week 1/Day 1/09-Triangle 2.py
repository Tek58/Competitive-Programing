def triangle2(num):
    for i in range(num):
        print(" " * (num-i), end="")

        print("*"*(2*i - 1), end="")
        print()
triangle2(num)
