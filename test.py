def insertion_sort(cisla, n):
    i = 1
    while i < n:
        klic = cisla[i]
        pozice = i
        j = i - 1

        while j >= 0:
            if cisla[j] > klic:
                cisla[j + 1] = cisla[j]
                pozice = j
            else:
                break
            j = j - 1

        cisla[pozice] = klic
        i = i + 1

    return cisla


cisla = input("Zadejte čísla oddělená mezerou: ").split()

n = len(cisla)

print("Před:", cisla)
print("Po:", insertion_sort(cisla, n))