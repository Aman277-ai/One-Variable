def calculations(spaceRemovedStr : str):
    var = variable(spaceRemovedStr)
    leftSide = spaceRemovedStr[:spaceRemovedStr.find('=')]
    rightSide = spaceRemovedStr[spaceRemovedStr.find('=') + 1]

    numOfVar : str = ""
    leftSideTemp = leftSide[:leftSide.find(var) + 1 : -1]
    
    print(numOfVar)

    if numOfVar != '':
        leftSide = leftSide.replace(var, "")

    else:
        if leftSide[leftSide.find(var) + 1 : leftSide.find(var) + 2] == '*':
            leftSide = leftSide.replace(var, '1')
        
        elif leftSide[leftSide.find(var) - 1 : leftSide.find(var)] == '/':
            leftSide = leftSide.replace(var, '1')

        elif leftSide[leftSide.find(var) + 1 : leftSide.find(var) + 2] == '/':
            leftSide = leftSide.replace(var, '1')

        else:
            leftSide = leftSide.replace(var, '0')

    print(leftSide)

def variable(spaceRemovedStr : str):
    var : str = ""
    for x in spaceRemovedStr:
        if x >= 'a' and x <= 'z':
            var += x
        else:
            continue
    return var