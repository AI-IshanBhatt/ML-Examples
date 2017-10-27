import numpy as np
from pprint import pprint

def get_minimum_euclidian(centroids, point):
    point = np.array(point.to_array())
    min_id = 0
    min_dist = 0
    for idx,centroid in enumerate(centroids):
        centroid = np.array(centroid.to_array())
        distance = np.linalg.norm(centroid - point, 2)
        if distance < min_dist:
            min_id = idx
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

    de

class Centroid(Point):
    def __init__(self,x, y, near_points):
        super().__init__(x, y)
        self.near_points = near_points


c1 = Centroid(25, 25, [])
c2 = Centroid(75, 75, [])


data_points = [list(map(int,x.strip().split(","))) for x in open("training.csv")]
points = [DataPoint(*point) for point in data_points]

pprint(points)
#Initial Centroind assignments
# for point in points:
#     point.curr = get_minimum_euclidian([c1,c2], point)

