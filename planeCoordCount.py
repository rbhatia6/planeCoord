import someLibrary

def planeResultsCoord(coord1, coord2, coordSet):
    numLeft = numRight = 0
    for coord in coordSet:
        # 1 if the point is on left
        # 2 if the point is on right
        x = someLibrtary.getPlaneCoord(coord1, coord2, coordSet)
        numLeft += 1 if x == 1 else numRight += 1
    return (numLeft, numRight)


# coordSet = [(x1,y1), (x2,y2), ….]
def coordMain(coordSet):
    outList = []
    for x, y in coordSet:
        outTuple = planeResultsCoord(x, y, coordSet)
        if outTuple[0] != outTuple[1]:
            pass
        else:
            outList.append(outTuple)
    return outList
