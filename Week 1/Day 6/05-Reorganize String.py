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
  if len(A) == 1:
    return A[0]
  A = sorted(A)
  server1 = []
  server2 = []
  
  server1.append(A.pop())
  server2.append(A.pop())
  
  value1 = Sum(server1)
  value2 = Sum(server2)
    
  for i in range(len(A)):
    if value1 > value2 and len(A)!= 0:
      server2.append(A.pop())
      value2 = Sum(server2)
    elif value1 <= value2 and len(A)!= 0:
      server1.append(A.pop())
      value1 = Sum(server1)
  return abs(value1 - value2)

def solution1(A):
    Max = A[0]
    count = 1
    for i in range(len(A)):
        if A[i] > Max:
            Max = A[i]
            count += 1
    return count