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
    result = []
    for i in range(len(both_nums)):
        if both_nums[i] != 0:
            if  both_nums[i] == 1:
                if i < Min:
                    result.append(Min - i)
                result.append(Min + i)
    print(both_nums)
    
print(frequencySort([5,9,8,8,2,-6,9,-6,4,-1,-2]))