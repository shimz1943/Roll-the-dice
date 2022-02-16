covik_ima_dimike = False

counter = 0
while counter < 5:
    robi_pila_na_mob = input("Da li pilaš čovika pozivima svako 10 minuti? (d/n) or (da/ne): ")
    if robi_pila_na_mob.lower() == "d" or robi_pila_na_mob.lower()=="da":
        covik_ima_dimike = True
        break
    elif robi_pila_na_mob.lower() == "n" or robi_pila_na_mob.lower()=="ne":
        if counter == 4:
            print("robi kme kme nema za pušit")
            break
        print("sinko jesi li ti bolestan daj ga zovi")
        counter = counter + 1

    else:
        print("ne razumim, aj ponovo")

while covik_ima_dimike:

    kolicina = int(input("E lega imam. Koliko ti triba? (upiši koliko grama ti triba): "))
    gram_price = 0

    if kolicina < 25:
        gram_price = 30


    elif 25 <= kolicina < 50:
        gram_price = 15


    elif 50 <= kolicina < 100:
        gram_price = 10


    elif kolicina >= 100:
        gram_price = 5

    total = kolicina * gram_price
    print(f"{kolicina}g ce te izac {total}kn")
    break
