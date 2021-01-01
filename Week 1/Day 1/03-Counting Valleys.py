def countingValleys(n,ar):
    count = 0
    x = 0
    for i in range(n):
        if ar[i] == "U":
            x += 1
        if ar[i] == "D":
            x -= 1
        if x == 0 and ar[i] == "U":
            count += 1
    return count
print(countingValleys(10,"DDUUUUDDDU"))
