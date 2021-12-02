"""
Triangulation tool for minecraft

A Client-Side CLI tool written in python.

Author: Qumolama.d(Lama3L9R)
"""
from math import sqrt, isclose

class Coordinate:
    x: float = 0
    z: float = 0

    def __init__(self, x=0, z=0):
        self.x = x
        self.z = z

    def distance(self, to: Coordinate) -> float:
        return sqrt((self.x - to.x)**2, (self.z - to.z)**2)

    def is_equals(self, obj: Coordinate) -> bool:
        return isclose(self.x, obj.x) and isclose(self.y, obj.y)

class ViewedCoordinate(Coordinate):
    yaw: float = 0

    def __init__(self, x=0, z=0, yaw=0):
        if yaw > 180 or yaw < -179.9:
            raise ValueError("Yaw out of range! The range of yaw should be (-179.9, 180]")
        self.yaw = yaw
    
    def is_equals(self, obj: Coordinate) -> bool:
        if isinstance(obj, ViewedCoordinate):
            return super().is_equals(obj) and isclose(self.yaw, obj.yaw)
        else:
            return super().is_equals(obj)

def triangulation(coord_1: ViewedCoordinate, coord_2: ViewedCoordinate):
    if coord_1.is_equals(coord_2):
        raise ValueError("Two coordinates are too close")
    left: ViewedCoordinate
    right: ViewedCoordinate

    if coord_1.x > coord_2.x:
        left = coord_2
        right = coord_1
    else:
        left = coord_1
        right = coord_2
    
    