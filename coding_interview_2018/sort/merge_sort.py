def merge_sort(input, start, end):
    if start == end:
        return

    mid = (start + end) // 2
    merge_sort(input, start, mid)
    merge_sort(input, mid+1, end)
    left = input[start: mid+1]
    right = input[mid+1: end+1]

    i,j,k = 0,0,start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            input[k] = left[i]
            i += 1
        else:
            input[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        input[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        input[k] = right[j]
        j += 1
        k += 1


input = [4,9,1,2,8,3]
merge_sort(input, 0 ,len(input)-1)
print(input)