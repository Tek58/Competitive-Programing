'''
Question -> https://www.hackerrank.com/contests/a2sv-contest-2/challenges/fraudulent-activity-notifications/problem
@Author -> 
'''
def activityNotifications(expenditure, d):
    noti = 0
    new_exp = expenditure
    for i in range( d, len(expenditure)):
        data = sorted(new_exp[:d])
        if len(data) % 2 == 0:
            median = (data[(len(data)//2)] + data[(len(data)//2) - 1])/2
        else:
            median = data[len(data)//2]
        if expenditure[i] >= median*2:
            noti += 1
            
        new_exp = new_exp[1:]
    return noti
