import random
son = random.randint(1, 100)
taxmin = int(input("1 dan 100 gacha bo'lgan sonni kiriting: "))
if taxmin == son:
    print("To'g'ri")
else:
    print("Noto'g'ri, men o'ylagan son:", son)