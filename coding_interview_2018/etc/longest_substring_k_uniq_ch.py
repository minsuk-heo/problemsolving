"""
abaydae = 5
abcade = 6
"""


def longest_substring(str, k):
    log = {}
    cur = ""
    largest = 0

    for i in range(len(str)):
        if not str[i] in log:
            log[str[i]] = 1
            cur += str[i]
        else:
            if log[str[i]] == k:
                largest = max(largest, len(cur))
                start = cur.find(str[i])
                cur = cur[start+1:] + str[i]
            else:
                log[str[i]] += 1
                cur += str[i]
    return max(largest, len(cur))

str ="aaaaaaa"
print( longest_substring(str,2) )

str ="abaa"
print( longest_substring(str,1) )