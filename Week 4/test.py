def encode(word):
    left = 0
    right = 0
    count = 0
    container = []
    while right < len(word):
        if word[left] == word[right]:
            count += 1
            right += 1
        else:
            container.append((word[left], count))
            count = 0
            left = right
    container.append((word[left], count))
    result = ""
    for i in range(len(container)):
        result += str(container[i][1]) + "" + container[i][0]
    
    print(result)

encode("aabaccccdddrgjhf")