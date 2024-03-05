def euclide_esteso_funzionante(a, b):
    a, b = abs(a), abs(b)
    #sono quattro liste
    q = [None]
    r = [a, b]
    x = [1, 0]
    y = [0, 1]
    flag = False
    q.append(a//b)
    #il '-' in una lista la legge al contrario
    while(r[-1] != 0):
        q.append(r[-2]//r[-1])
        r.append(r[-2]-q[-1]*r[-1])
        x.append(x[-2] - q[-1] * x[-1])
        y.append(y[-2] - q[-1] * y[-1])
    if(r[-2] == 1):
        flag = True
    return flag, x[-2], y[-2]


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
        chiave_privata = int(input("Inserisci il primo numero: "))
        p = int(input("Inserisci un numero primo: "))
        q = int(input("ancora un altro: "))
        phi = (p - 1) * (q - 1)
        #a -> chiave privata, x -> chiave pubblica
        flag, x, y = euclide_esteso_funzionante(chiave_privata, phi)
        if(flag):
            print(x, y)
            print(f"{chiave_privata}*{x}+{phi}*{y} = {chiave_privata*x+phi*y}")
        else:
            print("flag = false")
