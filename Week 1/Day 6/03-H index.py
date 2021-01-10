'''
Question -> https://leetcode.com/problems/h-index/
@Author : Taklemariam Alazar
'''
def hIndex(citations):
    citations = sorted(citations)
    citations = citations[::-1]
    count = 0
    for i in range(1,len(citations)+ 1):
        if citations[i-1] >= i:
            count += 1
    return count 