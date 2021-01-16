def reverse(self, x: int) -> int:
        if x == 0 :
            return 0
        elif x < 0:
            x = str(x).strip("-")
            for i in range(len(x)):
                if x[-1] == "0":
                    x =x.strip("0")
                    if len(x) == 1 and int(x[0]) == 0:
                        return 0
            answer = "-" + str(x[::-1])
            if int(answer) < (-2**31):
                return 0
            return answer
        x = str(x)
        for i in range(len(x)):
            if x[-1] == "0":
                x =x.strip("0")
                if len(x) == 1 and int(x[0]) == 0:
                    return 0
        answer = x[::-1]
        if int(answer) > (2**31)-1:
            return 0
        return answer