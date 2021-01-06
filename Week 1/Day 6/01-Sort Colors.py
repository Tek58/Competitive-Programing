def sortColors(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[index] = 0
            index += 1
        if nums[i] == 1:
            pass
        if nums[i] == 2:
            nums[index - 1] = 2
            index -= 1 

    return nums


        

print(sortColors([[2,0,2,1,1,0]]))