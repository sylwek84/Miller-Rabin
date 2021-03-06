def zlozonosc(a, d, n, s): #sprawdzanie złożoności podanej liczby
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True

def pierwszosc(n, precyzja_dla_duzej_n = 16): #test pierwszosci liczby
    if n in znane_liczby_pierwsze or n in (0, 1):
        return True
    if any((n % p) == 0 for p in znane_liczby_pierwsze):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    if n < 3825123056546413051:
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23))
    if n < pow(2, 64):
        return not any(zlozonosc(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))

    return not any(zlozonosc(a, d, n, s) for a in znane_liczby_pierwsze[:precyzja_dla_duzej_n])

znane_liczby_pierwsze = [2, 3]
znane_liczby_pierwsze += [x for x in range(5, 1000, 2) if pierwszosc(x)]

print("\nSkrypt do sprawdzania pierwszości liczby przy wykorzystaniu testu Millera-Rabina")
print("Opracowanie: Kamila Kurowska, Marcin Brzeziński, Sylwester Brożyna, Tomasz Mielczarek\n")
print("WSPol w Szczytnie, II rok Informatyki\n")
liczba = int(input("Podaj liczbę dla której chcesz przeprowadzić test pierwszości Millera-Rabina: \n"))

if pierwszosc(liczba):
    print("Liczba", liczba, "jest liczbą pierwszą!")
else:
    print("Liczba", liczba, "niestety nie jest liczbą pierwszą!")

