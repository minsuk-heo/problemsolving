# Returns the length of the longest palindromic subsequence

def longest_palindrome_subsequence(str):
    n = len(str)

    # Create a table to store results of subproblems
    matrix = []
    for i in range(n):
        matrix.append([0]*n)

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        matrix[i][i] = 1

    # window is length of substring
    for window in range(2, n + 1):
        for i in range(n - window + 1):
            j = i + window - 1
            if str[i] == str[j] and window == 2:
                matrix[i][j] = 2
            elif str[i] == str[j]:
                matrix[i][j] = matrix[i + 1][j - 1] + 2
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i + 1][j]);

    return matrix[0][n - 1]

print(longest_palindrome_subsequence("a"))
print(longest_palindrome_subsequence("abba"))
print(longest_palindrome_subsequence("efet"))
print(longest_palindrome_subsequence("abcdcba"))
print(longest_palindrome_subsequence("abcddcba"))
print(longest_palindrome_subsequence("awbcdedcba"))