cheeses = {
    23.55: "roquefort",
    34.50: "stilton",
    25.44: "brie",
    21.55: "gouda",
    25.22: "edam",
    28.34: "parmezan",
    24.21: "mozzarella",
    55.77: "czech sheep milk cheese"
}
print("Lista serów z cenami w PLN : ", cheeses)

print("===============================")

cheese1 = "roquefort"
price_cheese1 = 23.55

cheese2 = "stilton"
price_cheese2 = 34.50

cheese3 = "brie"
price_cheese3 = 25.44

cheese4 = "gouda"
price_cheese4 = 21.55

cheese5 = "edam"
price_cheese5 = 25.22

cheese6 = "parmezan"
price_cheese6 = 28.34

cheese7 = "mozzarella"
price_cheese7 = 24.21

cheese8 = "czech sheep milk cheese"
price_cheese8 =  55.77

list_of_cheeses = f"Lista serow: 1. {cheese1}, cena {price_cheese1} PLN, 2. {cheese2}, cena {price_cheese2} PLN, 3. {cheese3}, cena {price_cheese3} PLN, 4. {cheese4}, cena {price_cheese4} PLN, 5. {cheese5}, cena {price_cheese5} PLN, 6. {cheese6}, cena {price_cheese6} PLN, 7. {cheese7}, cena {price_cheese7} PLN, 8. {cheese8}, cena {price_cheese8} PLN"
print(list_of_cheeses)

print("===============================")

cheese1 = "roquefort"
price_cheese1 = 23.55

cheese2 = "stilton"
price_cheese2 = 34.50

cheese3 = "brie"
price_cheese3 = 25.44

cheese4 = "gouda"
price_cheese4 = 21.55

cheese5 = "edam"
price_cheese5 = 25.22

cheese6 = "parmezan"
price_cheese6 = 28.34

cheese7 = "mozzarella"
price_cheese7 = 24.21

cheese8 = "czech sheep milk cheese"
price_cheese8 =  55.77

list_of_cheeses1 = f"1. {cheese1}, cena: {price_cheese1} PLN"
list_of_cheeses2 = f"2. {cheese2}, cena: {price_cheese2} PLN"
list_of_cheeses3 = f"3. {cheese3}, cena: {price_cheese3} PLN"
list_of_cheeses4 = f"4. {cheese4}, cena: {price_cheese4} PLN"
list_of_cheeses5 = f"5. {cheese5}, cena: {price_cheese5} PLN"
list_of_cheeses6 = f"6. {cheese6}, cena: {price_cheese6} PLN"
list_of_cheeses7 = f"7. {cheese7}, cena: {price_cheese7} PLN"
list_of_cheeses8 = f"8. {cheese8}, cena: {price_cheese8} PLN"
print("lista serow z cenami:")
print(list_of_cheeses1)
print(list_of_cheeses2)
print(list_of_cheeses3)
print(list_of_cheeses4)
print(list_of_cheeses5)
print(list_of_cheeses6)
print(list_of_cheeses7)
print(list_of_cheeses8)

# ===============
print("=" * 25)
print("raport 2\n")

cheese1 = "roquefort"
rem_amount_kg1 = 2.00
price_cheese1 = 23.55
price_rem_amount1 = rem_amount_kg1 * price_cheese1

cheese2 = "stilton"
rem_amount_kg2 = 1.00
price_cheese2 = 34.50
price_rem_amount2 = rem_amount_kg2 * price_cheese2

cheese3 = "brie"
rem_amount_kg3 = 1.00
price_cheese3 = 25.44
price_rem_amount3 = rem_amount_kg3 * price_cheese3

cheese4 = "gouda"
rem_amount_kg4 = 1.00
price_cheese4 = 21.55
price_rem_amount4 = rem_amount_kg4 * price_cheese4

cheese5 = "edam"
rem_amount_kg5 = 1.00
price_cheese5 = 25.22
price_rem_amount5 = rem_amount_kg5 * price_cheese5

cheese6 = "parmezan"
rem_amount_kg6 = 3.50
price_cheese6 = 28.34
price_rem_amount6 = rem_amount_kg6 * price_cheese6

cheese7 = "mozzarella"
rem_amount_kg7 = 0.13
price_cheese7 = 24.21
price_rem_amount7 = round(rem_amount_kg7 * price_cheese7, 2)

cheese8 = "czech sheep \n  milk cheese"
rem_amount_kg8 = 0.22
price_cheese8 =  55.77
price_rem_amount8 = round(rem_amount_kg8 * price_cheese8, 2)

dessert = "mint"
rem_amount_mint = 0.20
price_dessert = 20.00

price_sum = round(price_rem_amount1 + price_rem_amount2 + price_rem_amount3 + price_rem_amount4 + price_rem_amount5 + price_rem_amount6 + price_rem_amount7 + price_rem_amount8 + price_dessert, 2)
# ===========================

print("Raport z zakupów")

szer = 44
print("-" * szer)
print("|     Produkt    | masa w kg |  Cena PLN  |")
print("*" * szer)
print(f"| {cheese1:14} | {rem_amount_kg1:8}  | {price_rem_amount1:10} |")

print(f"| {cheese2:14} | {rem_amount_kg2:8}  | {price_rem_amount2:10} |")

print(f"| {cheese3:14} | {rem_amount_kg3:8}  | {price_rem_amount3:10} |")

print(f"| {cheese4:14} | {rem_amount_kg4:8}  | {price_rem_amount4:10} |")

print(f"| {cheese5:14} | {rem_amount_kg5:8}  | {price_rem_amount5:10} |")

print(f"| {cheese6:14} | {rem_amount_kg6:8}  | {price_rem_amount6:10} |")

print(f"| {cheese7:14} | {rem_amount_kg7:8}  | {price_rem_amount7:10} |")

print(f"| {cheese8:14}    | {rem_amount_kg8:8}  | {price_rem_amount8:10} |")

print(f"| {dessert:14} | {rem_amount_mint:8}  | {price_dessert:10} |")

print("-" * szer)

print("Suma zł:", price_sum)