

coke_price = int(50)

while coke_price > 0:
    amount_msg = print("Amount Due: " + str(coke_price))
    insert_coin = int(input("Insert Coin: "))

    match insert_coin:
        case 5|10|25:
            coke_price = coke_price - insert_coin
        case _:
            coke_price = coke_price

print("Change Owed: " + str(coke_price * -1))




















