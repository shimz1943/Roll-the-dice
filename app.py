import random


def logika():
    if obrana[0] >= napad[0] and obrana[1] >= napad[1]:

        print("Obrana dobija oba")

    elif napad[0] > obrana[0] and napad[1] > obrana[1]:
        print("Napad dobija oba")

    else:
        print("Oba nose po 1")


napad = [str(random.randint(1, 6)), str(random.randint(1, 6))]
obrana = [str(random.randint(1, 6)), str(random.randint(1, 6))]

napad.sort(reverse=True)
obrana.sort(reverse=True)

print("Napad: " + napad[0] + " " + napad[1])
print("Obrana: " + obrana[0] + " " + obrana[1])
print("--------------")
logika()




