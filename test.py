
def point_position(p0, p1, p2):
    print(p0, p1, p2)
    return (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
    


print(point_position([3,2],[1,5],[1,5]))