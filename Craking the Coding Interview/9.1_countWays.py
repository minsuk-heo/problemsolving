def countWays(n):
    if(n < 0):
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)


print(countWays(3))
