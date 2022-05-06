import random


# Napravi metodu koja prima 2 broja i ispituje koji je veći.
# Napravi metodu koja prima broj i string i ispituje jeli dužina stringa veća ili nije od broja
# Napravi metodu koja prima 2 broja i sadržava 1 liniju koda koja vrati dali je broj 1 veći od broja 2 za ispitivanje
# primjeni isti princip i u metodi 2
# Napravi metodu koja prima 2 liste brojeva i stvara treću listu koja je rezultat zbroja brojeva na istim pozicijama u listama
def metoda1(num1, num2):
    if num1 > num2:
        return (num1)
    return (num2)


def metoda2(limit, word):
    return limit > len(word)


def dali_je_br1_veci_od_br2(num1, num2):
    return num1 > num2


def metoda4(list1, list2):
    result = []

    if dali_je_br1_veci_od_br2(len(list1), len(list2)):
        veca = list1
        manja = list2
    else:
        veca = list2
        manja = list1

    index = 0
    for broj_u_vecoj in veca:
        if dali_je_br1_veci_od_br2(index, len(manja)-1):
            result.append(broj_u_vecoj)
        else:
            sum = broj_u_vecoj + manja[index]
            result.append(sum)
        index += 1
    return(result)

print(dali_je_br1_veci_od_br2(3, 4))

A = input("upisi broj 1: ")
B = input("upisi broj 2: ")
print(f'Veći broj je {metoda1(A, B)}')

limit = int(input("Upiši limit jeben ti mrtvog oca: "))
word = input("UPIŠI RIČ MRTVOG TI ISUSA JEBEN: ")
print(f'RIČ JE MANJA: {metoda2(limit, word)}')

C = input("upisi broj 1: ")
D = input("upisi broj 2: ")
print(f'Broj 1 je veći:  {dali_je_br1_veci_od_br2(C, D)}')

prva_lista = [1, 2, 5, 7, 3, 8, 3, 1, 543, 7676]
druga_lista = [12, 32, 15, 47, 53, 68, 2]

print(metoda4(prva_lista, druga_lista))
