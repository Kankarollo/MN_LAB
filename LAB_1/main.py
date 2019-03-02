import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
   skrypt_jeden()
   skrypt_dwa()



def skrypt_jeden():
    x = 0.5
    for i in range(10):
        wynik = rozwiniecie_poprawne(i + 1, x)
        print(wynik)
        roznica_wzgledne_bewzgledne(wynik)

def skrypt_dwa():
    x = np.arange(0.0, 1.0, 0.01)

    wartosc1 = [rozwiniecie_poprawne(1, xi) for xi in x]
    wartosc3 = [rozwiniecie_poprawne(3, xi) for xi in x]
    wartosc10 = [rozwiniecie_poprawne(10, xi) for xi in x]

    wartosc1 = np.asarray(wartosc1)
    wartosc3 = np.asarray(wartosc3)
    wartosc10 = np.asarray(wartosc10)

    plt.plot(x, wartosc1, 'r', x, wartosc3, 'b', x,wartosc10, 'g')
    red_patch = mpatches.Patch(color='red', label='n = 1')
    blue_patch= mpatches.Patch(color='blue', label='n = 3')
    green_patch = mpatches.Patch(color='green', label='n = 10')
    plt.legend(handles=[red_patch, blue_patch, green_patch])
    plt.show()

def rozwiniecie_poprawne(n,x):
    indexy = np.arange(n)
    potega = indexy*2 + 1
    licznik = np.abs(indexy*2-1)
    licznik = np.cumprod(licznik)
    mianownik1 = np.arange(1,2*n,2)
    mianownik2 = np.arange(0,2*n,2)
    mianownik2[0] = 1
    mianownik = np.cumprod(mianownik2)*mianownik1

    tablica_wynikow = (np.power(x,potega)*licznik)/mianownik

    arc_sin = np.sum(tablica_wynikow)
    arc_cos = (math.pi / 2) - arc_sin

    return math.degrees(arc_cos)



def roznica_wzgledne_bewzgledne(liczba):
    wartosc_bewzgledna = math.fabs(liczba - 60.0)
    wartosc_wzgledna = (wartosc_bewzgledna / 60.0) * 100.0
    print("Wartosc bewzgledna: ", wartosc_bewzgledna, "Wartosc wzgledna: ", wartosc_wzgledna, "%")


def test():
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    print(np.multiply(x,y))
    print(np.convolve(x,y))


if __name__ == '__main__':
    main()
    # test()
    # rozwiniecie_poprawne(5)