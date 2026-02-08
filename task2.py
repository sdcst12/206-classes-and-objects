import os

def showInstructions():
    os.system("clear||cls")
    print("- Quadratic Equation Calculator - ")
    print("You will enter a quadratic in standard form")
    print("          ax² + bx + c")
    print("I will ask you for the coefficients")
    print("I will then tell you several things about the quadratic")
    print("I hope you are ready, this poop is about to get real!\n")

def getCoeffs():
    vars = ['a','b','c']
    for i in range(3):
        while True:
            try:
                coeff = int(input(f"Enter coefficient {vars[i]} >"))
                vars[i] = coeff 
                break
            except:
                print("invalid! It must be an integer. Try again")
            
    return vars[0],vars[1],vars[2]   

def getVertex(a,b,c):
    x = -(b)/(2*a)
    y = a*x**2 + b*x + c
    return (x,y)

def getVertexForm(a,vertex):
    x = vertex[0]
    y = vertex[1]
    if x < 0:
        bracket = f"(x + {-1*x})"
    else:
        bracket = f"(x - {x})"
    if y < 0:
        constant = f"- {-1*y}"
    else:
        constant = f" + {y}"
    return f"{a}{bracket}² {constant}"

def getYInt(a,b,c):
    return c

def getDiscriminant(a,b,c):
    return b**2 - 4*a*c

def getXInt(a,b,c):
    disc = getDiscriminant(a,b,c)
    roots = []
    if disc >= 0:
        r1 = round((-(b) + disc**(0.5))/(2*a),3)
        r2 = round((-(b) - disc**(0.5))/(2*a),3)
        roots.append(r1)
        roots.append(r2)
    else:
        roots.append('non real')
        roots.append('non real')
    return roots

if __name__ == "__main__":
    #show instructions
    showInstructions()
    #ask user for coefficients
    a,b,c = getCoeffs()
    vertex = getVertex(a,b,c)
    print(vertex)
    vertexForm = getVertexForm(a,vertex)
    print(vertexForm)
    yint = getYInt(a,b,c)
    print(yint)
    xint = getXInt(a,b,c)
    print(xint)
    #determine vertex form of parabola
    #determine directino of opening
    #determine y-intercept
    #determine x-intercepts (if they exist)