"""
S,S,S,F,F,F,F,F,F,F
"""


def binary_search(input, l, r):
    if len(input) < 1:
        return -1

    while l < r:
        mid = (l + r) // 2
        if input[mid] == "F":
            r = mid
        else:
            l = mid + 1

    return l if input[l] == "F" else -1


input = ["S", "S", "S", "F", "F", "F", "F", "F", "F", "F"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

input = ["F", "F", "F"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

input = ["S", "S", "S"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

input = ["S"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

input = []
idx = binary_search(input, 0 , len(input)-1)
print(idx)