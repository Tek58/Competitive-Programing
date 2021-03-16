'''
Question -> https://www.hackerrank.com/contests/a2sv-contest-8/challenges/gridland-metro/problem
@author -> Taklemariam Alazar
'''
def gridlandMetro(n, m, k, track):
    visited = {}
    count = 0
    for i in range(k):
        tr = track[i]
        if tr[0] not in visited: 
            visited[tr[0]] = (tr[1],tr[2])
            count += (tr[2] - tr[1])+1
        else:
            prev = visited[tr[0]]
            if tr[1] > prev[1] or tr[2] < prev[0]:
                count += (tr[2] - tr[1])+1
            else:
                newTr1 = min(prev[0],tr[1])
                newTr2 = max(prev[1],tr[2])
                count -= ((prev[1] - prev[0])+1)
                count += (newTr2 - newTr1)+1
                visited[tr[0]] = (newTr1,newTr2)
                
    return (n*m) - count