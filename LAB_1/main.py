import numpy as np
import math
import matplotlib.pyplot as plt


def main():
    x = 0.5
    for i in range(10):
        wynik = rozwiniecie(i + 1, x)
        print(wynik)
        roznica_wzgledne_bewzgledne(wynik)

    wartosc1 = []
    wartosc3 = []
    wartosc10 = []
    for i in range(100):
        wartosc1.append(rozwiniecie(1, i))
        wartosc3.append(rozwiniecie(3, i))
        wartosc10.append(rozwiniecie(10, i))

    wartosc1 = np.asarray(wartosc1)
    wartosc3 = np.asarray(wartosc3)
    wartosc10 = np.asarray(wartosc10)

    i = list(range(100))
    plt.plot(i, wartosc1)
    plt.hold
    plt.plot(i, wartosc3)
    plt.hold
    plt.plot(i, wartosc10)
    plt.show()


def rozwiniecie(n, x):
    licznik = np.array([x, (x ** 3) / (2 * 3), (3 * x ** 5) / (2 * 4 * 5), (15 * x ** 7) / (2 * 4 * 6 * 7),
                        (3 * 5 * 7 * x ** 9) / (2 * 4 * 6 * 8 * 9),
                        (1 * 3 * 5 * 7 * 9 * 11 * x ** 13) / (2 * 4 * 6 * 8 * 10 * 11),
                        (1 * 3 * 5 * 7 * 9 * 11 * 13 * x ** 15) / (2 * 4 * 6 * 8 * 10 * 12 * 13),
                        (1 * 3 * 5 * 7 * 9 * 11 * 13 * 15 * x ** 17) / (2 * 4 * 6 * 8 * 10 * 12 * 14 * 15),
                        (1 * 3 * 5 * 7 * 9 * 11 * 13 * 15 * 17 * x ** 19) / (2 * 4 * 6 * 8 * 10 * 12 * 14 * 16 * 17),
                        (1 * 3 * 5 * 7 * 9 * 11 * 13 * 15 * 17 * 19 * x ** 21) / (
                                    2 * 4 * 6 * 8 * 10 * 12 * 14 * 16 * 18 * 19)])
    arc_sin = np.sum(licznik[:n])
    arc_cos = (math.pi / 2) - arc_sin

    return math.degrees(arc_cos)


def roznica_wzgledne_bewzgledne(liczba):
    wartosc_bewzgledna = np.double(math.fabs(liczba - 60.0))
    wartosc_wzgledna = np.double(wartosc_bewzgledna / 60.0) * 100.0
    print("Wartosc bewzgledna: ", wartosc_bewzgledna, "Wartosc wzgledna: ", wartosc_wzgledna, "%")
    # print('Wartosc bewzgledna: %d Wartosc wzgledna: %s  ' % (wartosc_bewzgledna, wartosc_wzgledna))


def test():
    test = np.array([1, 2, 3, 4, 5])
    print(np.sum(test[:3]))
    print(math.degrees(math.pi))


if __name__ == '__main__':
    main()
    # test()