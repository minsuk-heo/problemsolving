"""
[1,2,3,4,5] k=4, return 3
[1,2,3,4,5] k=6, return -1
[4,5,1,2,3] k=4, return 0
"""

def find_pivot(arr,l, r):
    if len(arr) < 1:
        return -1
    if arr[l] < arr[r]:
        return -1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid-1]:
            return mid -1
        else:
            if arr[mid] > arr[l]:
                l = mid
            else:
                r = mid - 1
    return l


def find_k(arr, pivot, k):
    if arr[pivot] == k :
        return pivot

    if pivot == -1:
        #binary search on arr
        l, r = 0, len(arr)-1
    elif pivot == 0:
        l, r = pivot+1, len(arr)-1
    else:
        #binary search considering pivot
        if k >= arr[0] and k < arr[pivot]:
            l, r = 0, pivot-1
        else:
            l, r = pivot+1, len(arr)-1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == k:
            return mid
        else:
            if arr[mid] < k:
                l = mid + 1
            else:
                r = mid - 1

    return l if arr[l] == k else -1


arr = [5,1,2,3,4]
pivot = find_pivot(arr, 0 ,len(arr)-1)
#print(pivot)
#print(find_k(arr, pivot, 4))


arr = [4,5,1,2,3]
pivot = find_pivot(arr, 0 ,len(arr)-1)
#print(pivot)
#print(find_k(arr, pivot, 4))


arr = [3,4,5,1,2]
pivot = find_pivot(arr, 0 ,len(arr)-1)
#print(pivot)
#print(find_k(arr, pivot, 4))

arr = [2,3,4,5,1]
pivot = find_pivot(arr, 0 ,len(arr)-1)
#print(pivot)
#print(find_k(arr, pivot, 4))

arr = [1,2,3,4,5]
pivot = find_pivot(arr, 0 ,len(arr)-1)
#print(pivot)
#print(find_k(arr, pivot, 4))

arr = [1,2,3,4,5]
pivot = find_pivot(arr, 0 ,len(arr)-1)
print(pivot)
print(find_k(arr, pivot, 40))