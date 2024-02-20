def euclide_esteso(a, b):
    a, b = abs(a), abs(b)
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def euclide(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


if __name__ == '__main__':
    sc = int(input("1. Euclide\n"
                   "2. Euclide esteso\n"))
    if sc == 1:
        # funzione euclide
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il primo numero: "))
        if a > b:
            print(euclide(a, b))
        else:
            print(euclide(b, a))
    elif sc == 2:
        # funzione euclide esteso
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il primo numero: "))
        if a > b:
            print(euclide_esteso(a, b))
        else:
            print(euclide_esteso(b, a))
