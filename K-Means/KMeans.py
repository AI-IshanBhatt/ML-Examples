import numpy as np
from pprint import pprint


def has_not_converged(points):
    for point in points:
        if point.prev != point.curr:
            return 1
    return 0


def get_mean_centroid(points, i):
    x_axis = round(np.mean([point.x for point in points]))
    y_axis = round(np.mean([point.y for point in points]))
    pprint("THE NEW CENTROID {} {} for centroid {}".format(x_axis, y_axis, i))
    return Centroid(x_axis,y_axis,[])
"""
About doing multiprocessing-
1) Re location of centroids can be done using multip processing (1 process per cluster)
2) Divide points by CPU counts and 1 process for one set of points to set previous and current centroids.
"""

def get_minimum_euclidian(centroids, point):
    # pprint(centroids) This one is as expected
    point_np = np.array(point.to_array())
    min_id = 0
    min_dist = 9999
    for idx, centroid in enumerate(centroids):
        centroid = np.array(centroid.to_array())
        distance = np.linalg.norm(centroid - point_np, 2)
        if distance < min_dist:
            min_id = idx
            min_dist = distance
    centroids[min_id].near_points.append(point)
    return centroids[min_id]


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def to_array(self):
        return list((self.x, self.y))

    def __str__(self):
        return "{} {}".format(self.x, self.y)

    def __repr__(self):
        return "{} {}".format(self.x, self.y)


class DataPoint(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.prev = None
        self.curr = None

    def __str__(self):
        return "{} {} -> {} {}".format(self.x, self.y, self.prev, self.curr)

    def __repr__(self):
        return "{} {} -> {} {}".format(self.x, self.y, self.prev, self.curr)


class Centroid(Point):
    def __init__(self,x, y, near_points):
        super().__init__(x, y)
        self.near_points = near_points

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

c1 = Centroid(50, 50, [])
c2 = Centroid(100, 100, [])
c3 = Centroid(150, 150, [])

centroids = [c1,c2,c3]
new_centroids = []
data_points = [list(map(int,x.strip().split(","))) for x in open("training.csv")]
points = [DataPoint(*point) for point in data_points]

# Initial Centroind assignments
for point in points:
    point.curr = get_minimum_euclidian(centroids,point)

while 1:
    if has_not_converged(points):
        for i in range(0,len(centroids)):
            centroids[i] = get_mean_centroid(centroids[i].near_points, i)

        for point in points:
            point.prev = point.curr
            point.curr = get_minimum_euclidian(centroids, point)
    else:
        break

print("------------------------------------------------------------------------------")

for c in centroids:
    print(c.near_points)


