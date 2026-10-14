a= int(input("Birinchi son: "))
b= int(input("Ikkinchi son: "))
amal = input("Amallar, (+, -, *, /,): ")
if amal == "+":
    print(a+b)
elif amal == "-":
    print(a-b)
elif amal == "*":
    print(a*b)
elif amal == "/":
    print(a/b)
else:
    print("Noto'g'ri amal")