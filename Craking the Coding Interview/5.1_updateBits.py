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
    left = max_int << (j+1)
    right = (1 << i) - 1
    return left | right

def UpdateBits(m,n,i,j):
    max_int = 2 ** 32 - 1
    mask = getMask(i,j,max_int)
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted

m = 19
n = 2048
i = 2
j = 6

result = UpdateBits(m,n,i,j)
printBinary(result)
