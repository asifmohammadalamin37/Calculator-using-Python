def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

while 1:

    print("\nSelect an operation:\n\n1 for Add\n2 for Subtract\n3 for Multiply\n4 for Divide\n5 for Modulus\n0 for Exit\n")
    try:
        x = int(input("Enter choice (1/2/3/4/5/0): "))
    except ValueError:
        print("\nYour input is not valid. Please enter a valid integer number.")
        continue
    
    if x==0:
        break
    elif x<0 or x>5:
        print ("\nChoose an integer from 0 to 5.")
        continue
    else:
        try:
            y = float(input("\nInput first number: "))
            z = float(input("Input second number: "))
        except ValueError:
            print("\nYour input is not valid. Please enter a valid number.")
            continue
        
        if y.is_integer():
            y = int(y)
        if z.is_integer():
            z = int(z)
    
    if x==1:
        r = round(add(y,z),2)
        if r.is_integer():
            r = int(r)
        print(f"\nAddition: {y} + {z} = {r}\n")

    elif x==2:
        r = round(sub(y,z),2)
        if r.is_integer():
            r = int(r)
        print(f"\nSubtraction: {y} - {z} = {r}\n")

    elif x==3:
        r = round(mul(y,z),2)
        if r.is_integer():
            r = int(r)
        print(f"\nMultiplication: {y} * {z} = {r}\n")

    elif x==4:
        try:
            r = round(div(y,z),2)
        except ZeroDivisionError:
            print("\nSecond number can not be zero. Try again.")
            continue
        if r.is_integer():
            r = int(r)
        print(f"\nDivision: {y} / {z} = {r}\n")

    elif x==5:
        try:
            r = round(mod(y,z),2)
        except ZeroDivisionError:
            print("\nSecond number can not be zero. Try again.")
            continue
        if r.is_integer():
            r = int(r)
        print(f"\nModulus: {y} % {z} = {r}\n")