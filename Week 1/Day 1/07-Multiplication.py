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

def multiplication(x, y):
    carry = 0
    if x[0] == "-" and y[0] == "-":
        x = x.strip("-")
        y = y.strip("-")

    for i in range(len(y) - len(x)):
        x = "0" + x
    for j in range(len(x) - len(y)):
        y = "0" + y

    lis = [[] for i in range(len(y))]

    for i in range(1, len(x) + 1):
        if i >= 2:
            for z in range(i - 1):
                disp = 0
                lis[i - 1].append(disp)
        for j in range(1, len(y) + 1):
            ans = int(y[-i]) * int(x[-j]) + carry
            if ans >= 10:
                ans = str(ans)
                lis[i - 1].append(int(ans[1]))
                carry = int(ans[0])
            else:
                lis[i - 1].append(ans)
                carry = 0
            lis[i - 1][::-1]
        if carry != 0:
            lis[i - 1].append(carry)
            carry = 0
    for r in range(len(lis)):
        lis[r] = lis[r][::-1]

    summ = 0
    liss = []
    for i in range(len(lis)):
        nstr = ""
        for j in lis[i]:
            nstr += str(j)
        liss.append(nstr)
    if len(liss) > 2:
        while len(liss) > 2:
            summ = summ + summation(liss[0], liss[1])
            liss.remove(liss[0])
            liss.remove(liss[0])
    if len(liss) == 2:
        summ = summ + summation(liss[0], liss[1])
    else:
        summ = summ + int(liss[0])

    return summ


if x[0] == "-" and y[0] == "-":
    print(int(multiplication(x, y)))
elif x[0] == "-" or y[0] == "-":
    x = x.strip("-")
    y = y.strip("-")
    result = multiplication(x, y)
    print(int("-" + str(result)))
else:
    print(int(multiplication(x, y)))
    
