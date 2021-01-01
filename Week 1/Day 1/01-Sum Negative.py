x = input("Enter your first num: ")
y = input("Enter your second num: ")

def summation(x, y):
    carry = 0
    lis = []

    x = x.strip("-")
    y = y.strip("-")

    for i in range(len(x) - len(y)):
        y = "0" + y

    for i in range(len(y) - len(x)):
        x = "0" + x

    for i in range(1, len(x) + 1):
        ans = int(x[-i]) + int(y[-i]) + carry
        if ans >= 10:
            ans = str(ans)
            lis.append(int(ans[1]))
            carry = int(ans[0])
        else:
            lis.append(ans)
            carry = 0
    if carry != 0:
        lis.append(carry)
        carry = 0

    lis = lis[::-1]
    # return "".join(lis)
    result = ""
    for i in lis:
        result += str(i)
    return int(result)

if x[0] == "-" and y[0] == "-":
    result = summation(x, y)
    print("-" + str(result))


elif x[0] == "-" or y[0] == "-":
    x = x.strip("-")
    y = y.strip("-")
    if len(x) > len(y):
        maximum = x
        minimum = y
    if len(x) < len(y):
        maximum = y
        minimum = x
    if len(x) == len(y):
        if x[0] > y[0]:
            maximum = x
            minimum = y
        else:
            maximum = y
            minimum = x
    lis = []
    for i in range(len(x) - len(y)):
        y = "0" + y

    for i in range(len(y) - len(x)):
        x = "0" + x

    for i in range(1, len(x) + 1):
        if int(x[-i]) < int(y[-i]):
            ans = int("1"+x[-i]) - int(y[-i])
            # x[-i-1] = int(x[-i]) - 1
            lis.append(ans)
        else:
            ans = int(x[-i]) - int(y[-i])
            lis.append(ans)

    lis = lis[::-1]
    result = ""
    for i in lis:
        result += str(i)

    print(result)

