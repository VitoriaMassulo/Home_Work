user_input = input("Input a number between 1 and 9: ")
user_choice = int(user_input)



for n in range(1, user_choice + 1):
    lines = ""
    for u in range(1, n + 1):
        lines += str(u)
    print(lines)

for n in range(user_choice - 1, 0, -1):
    lines = ""
    for u in range(1, n + 1):
        lines += str(u)
    print(lines)

print("-" * 20)

#  BONUS

cochavit = []

for i in range(1, user_choice + 1):
    star_lines = ""
    for s in range(user_choice - i):
        star_lines = star_lines + " "

    for t in range( 2*i - 1):
        star_lines = star_lines + "*"

    chochavit.append(star_lines)

for row in cochavit:
    print(row)