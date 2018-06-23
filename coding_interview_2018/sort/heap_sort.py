def heap_sort(input):
    p = (len(input) // 2) - 1
    #heapify
    while p >= 0:
        siftdown(input, p, len(input)-1)
        p -= 1

    out = len(input) - 1
    while out > 0:
        input[0], input[out] = input[out], input[0]
        out -= 1
        siftdown(input, 0, out)

def siftdown(arr, p, last):
    left = 2*p+1
    right = 2*p+2
    if left > last:
        return
    if right > last or arr[left] > arr[right]:
        max_node = left
    else:
        max_node = right

    if arr[max_node] > arr[p]:
        arr[max_node], arr[p] = arr[p], arr[max_node]
        siftdown(arr, max_node, last)


input = [4,3,1,5,7,9]
heap_sort(input)
print(input)