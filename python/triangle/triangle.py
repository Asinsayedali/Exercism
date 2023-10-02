def equilateral(sides):
    if all(side > 0 for side in sides) and len(set(sides)) == 1:
        return True
    else:
        return False





def isosceles(sides):
    for i in range(len(sides)-2):
        if sides[i] == sides[i+1] or sides[i+1] == sides[i+2] or sides[i] == sides[i+2]:
            if sides.count(1) == 2:
                return False
            return True
    return False


def scalene(sides):
    # Check if the sides violate the triangle inequality theorem
    if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1]:
        return False

    # Check if all sides are different
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    else:
        return False
