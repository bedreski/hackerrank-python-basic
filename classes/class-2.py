# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true

from math import acos, degrees

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# The subtraction between two vectors is done coordinate by coordinate:
# A - B = (Ax - Bx, Ay - By, Az - Bz)
# The __sub__ special method allows Python to interpret the operator - between two objects of our class.
# This way, we can write AB = B - A instead of call a subtraction method explicitly. 
    def __sub__(self, no):
        return Point(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

# The dot product between two vector is:
# A * B = AxBx + AyBy + AzBz
    def dot(self, no):
        return (
            self.x * no.x +
            self.y * no.y +
            self.z * no.z
        )

    # Calculate the cross product, returning a new vector perpendicular to the two vectors used in the operation.
    def cross(self, no):
        return Point(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    

if __name__ == '__main__':
    A = Point(*map(float, input().split()))
    B = Point(*map(float, input().split()))
    C = Point(*map(float, input().split()))
    D = Point(*map(float, input().split()))

    AB = B - A
    BC = C - B
    CD = D - C

    X = AB.cross(BC)
    Y = BC.cross(CD)

    if Y > 0:
        cos_angle = X.dot(Y) / (X.absolute() * Y.absolute())
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle = degrees(acos(cos_angle))
        print(f"{angle:.2f}")