def matrix(w,h):
    return [ [0 for x in range(w)] for y in range(h) ]

m1 = matrix(3,4)
print(m1)
m1[0][0] = 1
m1[0][1] = 2
m1[0][2] = 3
m1[1][0] = 4
m1[1][1] = 5
m1[1][2] = 6
print(m1)
