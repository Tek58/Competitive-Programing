'''
Question -> https://leetcode.com/problems/product-of-array-except-self/
@author -> Taklemariam Alazar
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        for i in range(len(nums)-1):
            prefix.append((prefix[i] * nums[i]))
            postfix.append((postfix[i] * nums[len(nums)-1-i]))
        
        postfix.reverse()
        return [prefix[x]*postfix[x] for x in range(len(postfix))]

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        container = []
        total_product = 1
        exists = False
        for i in nums:
            if i != 0:
                total_product *= i
            else:
                exists += 1
                
        for i in nums:
            if i == 0 and exists == 1:
                container.append(total_product)
            else:
                if exists:
                    container.append(0)
                else:
                    container.append(total_product//i)
        
        return container
'''