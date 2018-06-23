def quick_sort(input, start, end):
    if start >= end:
        return

    pivot = end
    window = start
    i = start
    while i < pivot:
        if input[i] < input[pivot]:
            input[window], input[i] = input[i], input[window]
            window += 1
        i += 1
    input[window], input[pivot] = input[pivot], input[window]
    pivot = window
    quick_sort(input, start, pivot-1)
    quick_sort(input, pivot+1, end)

input = [4,9,1,2,8,3]
quick_sort(input, 0 ,len(input)-1)
print(input)