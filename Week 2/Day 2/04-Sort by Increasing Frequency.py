def frequencySort(nums):
    Max = max(nums)
    Min = min(nums)
    nums_negative = []
    nums_positive = []

    if Min < 0:
        nums_negative = [0]*(Min*-1)
    nums_positive = [0]*(Max + 1)
    for i in range(len(nums)):
        if nums[i] >= 0:
            nums_positive[nums[i]] += 1
        elif nums[i] < 0:
            nums_negative[nums[i]] += 1
   
    both_nums = nums_negative + nums_positive
    max_both = max(both_nums)
    result = []
    for i in range(1,max_both + 1):
        for j in range(len(both_nums)-1,0,-1):
            if both_nums[j] != 0:
                if  both_nums[j] == i:
                    print(both_nums[j])
                    for i in range(i):
                        if j < (-1 * Min):
                            result.append(both_nums[j - Min])
                        result.append(both_nums[j - Max])
    print(result)
    
print(frequencySort([5,9,8,8,2,-6,9,-6,4,-1,-2]))