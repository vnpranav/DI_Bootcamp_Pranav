def addOperator(x,y):
    try:
        sum = x+ y
        return sum
    except:
        print("wrong operand(s)")
        return None

def divideOperator(x,y):
    try:
        div = x / y
        return div
    except:
        print("error has occured")
        return None