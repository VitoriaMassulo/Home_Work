# try to use this patern in the code
#while True:
#   try: x = int(input())
#   break
#   except ValueError:
#print('try again')
'''
WHILE LOOP (main game)
│
├── ask for bet
├── spin()
├── check winner
└── update wallet

'''

import random

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
wallet_money = 50

print("=== SLOT MACHINE === \n")


while True:
    choice = input("Press Enter to spin or press Q to quit: ")
    if choice == "q":
        print("Thank you for playing! 😄")
        break

    index_random = [random.randint(0, 4) for r in range(3)]
    result = [symbols[index] for index in index_random]

    try:
        bet_amount = int(input(f"You have {wallet_money}$.\n Enter your bet amount: "))
    except ValueError:
        print("please enter a whole number!")
        continue

    if bet_amount >= 1 and bet_amount <= wallet_money:
        print(f"{result[0]} {result[1]} {result[2]}")

        if index_random[0] == index_random[1] == index_random[2]:
            winnings = bet_amount * rate[index_random[0]] * 777
            print(f"🎉 3 of a kind! You win {winnings}$")
        elif index_random.count(index_random[0]) == 2 or\
             index_random.count(index_random[1]) == 2:
            match_rate = max(index_random, key = index_random.count)
            winnings = bet_amount * rate[match_rate]
            print(f"🎉 2 of a kind! You win {winnings}$")
        else:
            winnings = -bet_amount
            print(f"😢 All different! You lose {bet_amount}$")

        wallet_money += winnings

        if wallet_money <= 0:
            print("💸 You ran out of money! Game over.")
            break

    else:
        print(f"Invalid bet amount!")







