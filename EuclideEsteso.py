def euclide_esteso(a,b):
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y1

def euclide(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

if __name__ == '__main__':
    # funzioane euclide
    # a = int(input("Inserisci il primo numero: "))
    # b = int(input("Inserisci il primo numero: "))
    # if a > b:
    #     print(euclide(a, b))
    # else:
    #     print(euclide(b, a))

    # funzione euclide esteso
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il primo numero: "))
    if a > b:
        print(euclide_esteso(a, b))
    else:
        print(euclide_esteso(b, a))
