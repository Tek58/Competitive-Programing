'''
Question -> https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
@Author : Taklemariam Alazar
'''
def markAndToys(prices, k):
    sorted_arr = sorted(prices)
    sum_of_toys = 0
    count = 0
    for i in range(len(sorted_arr)):
        sum_of_toys += sorted_arr[i]
        if sum_of_toys <= k:
            count += 1
        else:
            break
    return count

print(markAndToys([1,12,5,111,200,1000,10], 50))


