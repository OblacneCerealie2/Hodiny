stlpce = int(input("stlpce?: "))
rady = int(input("Rady?: "))
symbol = input("Daj symbol")


for i in range(stlpce):
    for x in range(rady):
        print(symbol, end = " ")
    print()