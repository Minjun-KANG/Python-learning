def multiples():
    num_mult = int(input("Enter num : "))
    for i in range(1, num_mult+1):
        x=float(input("Enter num :"))
        print(i, i*x)
    return i * x

multiples()
print()
def multiples2():
    num_mult = int(input("Enter num : "))
    for i in range(1, num_mult+1):
        x=float(input("Enter num :"))
        print(i, i*x)
        return i * x
multiples2()
#return 하고 끝나서 한번밖에 출력이 안댐.
