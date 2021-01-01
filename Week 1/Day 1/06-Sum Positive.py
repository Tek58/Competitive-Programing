def summation(x, y):
    carry = 0
    lis = []


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
    result = ""
    for i in lis:
        result += str(i)
    return result
print(summation("216546541","4565465454"))
