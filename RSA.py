from datetime import datetime as dt


def trasforma_binario(n):
    return bin(n)[2:]


def rsa1(b, e, modulo):
    """b è la base
    e è l'esponente
    mod è il modulo per il resto
    #return b**e%m"""

    risultato = 1
    esponente_binario = trasforma_binario(e)

    for c in esponente_binario[::-1]:
        bit_esponente = int(c)
        if bit_esponente == 1:
            risultato = risultato * b
        b = b * b % modulo
    return risultato % modulo


if __name__ == '__main__':
    base = int(input('base: '))
    esponente = int(input('esponente: '))
    mod = int(input('modulo: '))
    t0 = dt.now()
    print(rsa1(base, esponente, mod))
    t1 = dt.now()
    print('tempo: ', t1 - t0)
    print(base ** esponente % mod)
    t2 = dt.now()
    print('tempo: ', t2 - t1)
