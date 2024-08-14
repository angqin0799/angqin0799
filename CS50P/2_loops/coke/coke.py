# Constants
COKE_COST = 50
VALID_COINS = [5, 10, 25]

def main():
    amount_due = COKE_COST

    while True:
        print("Amount Due:", amount_due)
        amount_inserted = int(input("Insert Coin: "))

        # if not true cent, amount due will persist
        # valid coins continue
        if not verify_coin(amount_inserted):
            print("Amount Due:", amount_due)
            continue

        amount_due -= amount_inserted
        if amount_due > 0:
            amount_due = amount_due
        elif amount_due < 0:
            change_owed = abs(amount_due)
            print("Change Owed:", change_owed)
            break
        else:
            print("Change Owed: 0")
            break





def verify_coin(cent):
    ''' verify inserted coins '''
    return cent in VALID_COINS


main()




