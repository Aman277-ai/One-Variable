def calculations(spaceRemovedStr : str):
    
    var = variable(spaceRemovedStr)
    leftSide = spaceRemovedStr[:spaceRemovedStr.find('=')]
    rightSide = spaceRemovedStr[spaceRemovedStr.find('=') + 1 : len(spaceRemovedStr)]
    
    leftSideTemp = leftSide[0 : leftSide.find(var) + 1]
    leftSideTemp = leftSideTemp[ : : -1]
    operatorOfVar : str = ""
    
    for x in leftSideTemp:
        if x == '+':
            operatorOfVar = '+'
            break

        elif x == '-':
            operatorOfVar = '-'
            break

        elif x == '*':
            operatorOfVar = '*'
            break

        elif x == '/':
            operatorOfVar = '/'
            break
    
    numOfVar : str = leftSideTemp[leftSideTemp.find(var) + 1 : leftSideTemp.find(operatorOfVar)]
    if leftSideTemp.find(operatorOfVar) == 0:
        numOfVar = leftSideTemp[leftSideTemp.find(var) + 1]
    
    answer : float = None
    if operatorOfVar == '+' or operatorOfVar == '-':
        if numOfVar == "":
            leftSide = leftSide.replace(var, "0")
            answer = (eval(rightSide) - eval(leftSide))
            if eval(leftSide) == 0:
                answer = answer * -1
        else:
            leftSide = leftSide.replace(var, "")
            answer = (eval(rightSide) - eval(leftSide))
            if eval(leftSide) == 0:
                answer = answer * -1

    else:
        if numOfVar == "":
            leftSide = leftSide.replace(var, "1")
            answer = (eval(rightSide) / eval(leftSide))
        else:
            leftSide = leftSide.replace(var, "")
            answer = (eval(rightSide) / eval(leftSide)) 
    return answer,operatorOfVar

def variable(spaceRemovedStr : str):
    var : str = ""
    for x in spaceRemovedStr:
        if x >= 'a' and x <= 'z':
            var += x
        else:
            continue
    print("Value of " + var + " is equal to:")
    return var