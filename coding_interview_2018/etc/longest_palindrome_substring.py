"""
f("a") = "a"
f("aa") = "aa"
f("aba") = "aba"
f("abba") = "abba"
f("abcdc") = "cdc"
"""


def find_pal(left, right, input):
    if right >= len(input):
        return ""
    if input[left] != input[right]:
        return ""
    while left >= 0 and right < len(input) and input[left] == input[right]:
        left -= 1
        right += 1

    return input[left+1:right]


def longest_palindrome(input):
    if len(input) <= 1:
        return input
    max_odd = ""
    max_even = ""
    for idx in range(len(input)):
        max_odd = max(max_odd, find_pal(idx, idx, input))
        max_even = max(max_even, find_pal(idx, idx+1, input))
    return max(max_odd, max_even)

print( longest_palindrome("") )
print( longest_palindrome("a") )
print( longest_palindrome("aa") )
print( longest_palindrome("aba") )
print( longest_palindrome("abcdc") )
