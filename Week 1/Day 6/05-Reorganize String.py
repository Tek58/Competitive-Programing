# '''
# Question -> https://leetcode.com/problems/reorganize-string/
# @Author : Taklemariam Alazar
# '''
# def reorganizeString(S):
#     if len(S) == 1 or len(S) == 0:
#         return ' " " '

#     storage  = [0]*26
#     for i in S:
#         storage[(ord(i)-97)] += 1

#     S = sorted(S)
#     letters = []
#     non_zero = []
#     count = 0
#     for i in storage:
#         if i != 0:
#             count += 1
#             non_zero.append(i)

#     for i in range(count):
#         letters.append((S[:(non_zero[i])]))
#         S = S[(non_zero[i]):] 
#         if len(S) == 1:
#             letters.append(S)
#             break

#     reorganized = ''
#     print(non_zero)
#     print(letters)
#     i = 0
#     for i in range(len(non_zero)-1):
#         x = letters[i]
#         y = letters
#         while i == 0:
#             if len(letters[i]) != 0 and len(letters[i+1]) != 0:
#                 let1 = letters[j].pop()
#                 let2 = letters[i+1].pop()
#                 reorganized = reorganized + let1 + let2
 
#     return 
# print(reorganizeString("abaaczadrrcr"))

def solution(A):
    new_A = sorted(A)
    new_A = new_A[::-1]
    count = 0
    print(A)
    print(new_A)
    for i in range(len(A)-1):
        if A.index(new_A[i]) > A.index(new_A[i+1]):
            count += 1
            print(count, A.index(new_A[i]), A.index(new_A[i+1]))
    return count
print(solution([5,3,2,4,6,1,9,2,11,5]))