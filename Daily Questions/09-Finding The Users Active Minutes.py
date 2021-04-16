'''
Question -> https://leetcode.com/problems/finding-the-users-active-minutes/
'''
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        container_min = defaultdict(set)
        container_UAM = defaultdict(int)
        result = [0]*k
        for log in logs:
            container_min[log[0]].add(log[1])

        for i in container_min:
            count = len(container_min[i])
            container_UAM[count] += 1

        for count in container_UAM:
            result[count-1] = container_UAM[count]

        return result
