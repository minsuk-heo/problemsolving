"""
f([-2,-1,4,1]) = 5
f([-2,-1,4,1,-3,1]) = 5
"""

def largest_sum_subarray(arr):
    l_sum = arr[0]
    cur = arr[0]
    for i in range(1, len(arr)):
        if cur > 0:
            cur = cur + arr[i]
        else:
            cur = arr[i]

        l_sum = max(l_sum, cur)

    return l_sum


print( largest_sum_subarray( [-2,-1] ) )
print( largest_sum_subarray( [-2,-1,4,1] ) )
print( largest_sum_subarray( [-2,-1,4,1,-3,1] ) )
print( largest_sum_subarray( [-2,-1,4,1,-1,3] ) )