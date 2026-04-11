# need to find euclidian distance between two points in 2D space

# (2,3) , (10,8)

# heres the formula
# sqrt((p1-q1)^2 + (p2-q2)^2)
def euclidian_distance(p1, p2):

    diff1 = p1[0] - p2[0]
    diff2 = p1[1] - p2[1]
    sum = diff1**2 + diff2**2
    sqrt = sum** 0.5 # i forgor- sqrt- to the 0.5 power

    return sqrt

p1 = [2,3]
p2 = [10,8]

print(euclidian_distance(p1,p2))
