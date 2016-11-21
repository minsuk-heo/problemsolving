"""
N = 10000000000
M = 10011
i = 2
j = 6
output : 10001001100
"""

def printBinary(num):
    b_num = bin(num)    #b_num: 0bXXX
    print(b_num[2:])    #don't display b0

def getMask(i,j,max_int):
    # 11100000000
    left = max_int << (j+1)
    # 00000000011
    right = (1 << i) - 1
    # 11100000011
    return left | right

def UpdateBits(m,n,i,j):
    max_int = 2 ** 32 - 1
    # mask = 11100000011
    mask = getMask(i,j,max_int)
    # n_cleared = 10000000000
    n_cleared = n & mask
    # m_shifted = 1001100
    m_shifted = m << i
    # return 10001001100
    return n_cleared | m_shifted

# 19 = 10011
m = 19
# 1024 = 10000000000
n = 1024
i = 2
j = 6

result = UpdateBits(m,n,i,j)
printBinary(result)
