def draw(n,symbol="*"):
    for i in range(1, n+1):
        print(symbol, end="")
    print()
    

def proc(*params):
    for var in params:
        print("var",var)