milkman_has_milk = False

counter = 0
while counter < 5:
    you_annoy_with_calls = input("Are you shameless enough to get the milkan to answer to your calls? (y/yes/n/no): ")
    if you_annoy_with_calls.lower() == "y" or you_annoy_with_calls.lower()== "yes":
        milkman_has_milk = True
        break
    elif you_annoy_with_calls.lower() == "n" or you_annoy_with_calls.lower()== "no":
        if counter == 4:
            print("Anxiety got all over you. No milk, no party. :(")
            break
        print("C'mon man call him. Coffee without milk is no g00d bruh.")
        counter = counter + 1

    else:
        print("Don't understand your input. Please repeat.")

while milkman_has_milk:

    quantity_milk = int(input("""
Sorry man I was busy. My stocks are full so don't worry. 
How much milk do you need? (write the number for amount of milk in liters): """))
    milk_price = 0

    if quantity_milk < 25:
        milk_price = 8


    elif 25 <= quantity_milk < 50:
        milk_price = 6


    elif 50 <= quantity_milk < 100:
        milk_price = 4


    elif quantity_milk >= 100:
        milk_price = 2

    total = quantity_milk * milk_price
    print(f"{quantity_milk}l of milk will total you of {total}kn")
    break
