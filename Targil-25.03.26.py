'''
1
Write a function average_score(scores: list[int]) -> float:
  that receives a list of exactly three integers (0–100)
  and returns the average as a float

Example: average_score([80, 90, 70]) → 80.0

if got list not with 3 numbers then -> return None
Or:
  raise ValueError("Expected exactly three scores")
'''

scores = []

def average_score(scores: list[int]) -> float:
    if len(scores) != 3:
        raise ValueError("Expected exactly three scores")

    return sum(scores)/len(scores)
try:
    scores = [80, 90, 70, 100]
    print(average_score(scores))
except ValueError as e:
    print(f"Error: {e}")



print(average_score([80, 90, 70]))
print("-"*20)

'''
2
def star_odd(word: str) -> bool:
  pass

You are given a string 
Print "yes" if every element at an odd index (1, 3, 5, …, 23) equals "*"
Otherwise print "no"

 0123
  1 3
"1*2*"

'''

def star_odd(word: str) -> bool:
    valid_odds = True
    for index in range(1, len(word), 2):
        if index % 2 == 0:
            if word[index] != "*":
                valid_odds = False
                break
        return valid_odds

result = star_odd("1*2*3*4*5*6*7")

if result == True:
    print("yes")
elif result == False:
    print("no")

print("-"*20)


def star_odd2(word: str) -> bool:
    return all(index == "*" for index in word[1::2])

user_input = "1*2*3*4*5*6*7"

if star_odd2(user_input):
    print("yes")
else:
    print("no")


print("-"*20)
'''
3
Write a function that generates random integers between 0 and 10 (inclusive) 
until the  sum becomes greater than 42
The program must print how many numbers were generated
(print the random generated numbers [for debug])

def count_draws_until_sum_exceeds(limit: int = 42) -> int:
  pass

8 10 8 4 6 7 1 
43

return: 7
'''
import random

def count_draws_until_sum_exceeds(limit: int = 42) -> int:
    the_sum = 0
    g_numbers = []

    while the_sum <= limit:
        number = random.randint(0, 10)
        g_numbers.append(number)
        the_sum += number

    print(f"Numbers generated: {g_numbers}")
    print(f"The sum is: {the_sum}")
    return len(g_numbers)

tt_draw = count_draws_until_sum_exceeds(42)
print(f"there were {tt_draw} numbers generated to reach limit")
print("-"*20)


def count_draws_until_sum_exceeds2(limit: int = 42) -> int:
    total_sum = 0
    count = 0

    # 1. Start the loop
    while total_sum <= limit:
        # 2. Generate a random number from 0 to 10
        # 'randint' is inclusive, meaning it can pick 0 or 10
        new_number = random.randint(0, 10)

        # 3. [Debug] Print the number we just got
        print("Generated:", new_number)

        # 4. Add the number to our running total
        total_sum = total_sum + new_number
        print(f"The sum is: {total_sum}")

        # 5. Increment our counter
        count = count + 1

    # 6. Once the loop finishes, print the final result
    print("Final count of numbers generated is:", count)

    return count


tt_draw2 = count_draws_until_sum_exceeds2(42)
print(f"{tt_draw2}")
print("-"*20)

'''
4
Repeatedly prompt the user for a fraction of the form X/Y where:

X is a non-negative integer
Y is a positive integer
X <= Y
When valid, compute the percentage round(100 * X / Y) and output:

E if the percentage is 5% or less
F if the percentage is 95% or more
otherwise output NN% (e.g., 75.59%)
If input is invalid (not integers, Y == 0, or X > Y), 
prompt again
(Catching ValueError / ZeroDivisionError is acceptable)

def fuel_status() -> str:
  pass 
'''
def fuel_status() -> str:
    while True:
        try:
            x_fraction = int(input("Enter fraction of form (X): "))
            y_fraction = int(input("Enter fraction of form (Y): "))

            if y_fraction == 0:
                print("Error: Y cant be zero")
                continue
            if x_fraction < 0 or x_fraction > y_fraction:
                print("Error: X must be between 0 and Y.")
                continue

            percentage = round(100 * x_fraction / y_fraction)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except ValueError:
            print("Error: Enter whole numbers only.")
            continue

fraction = fuel_status()
print(fraction)
print("-"*20)

'''
5
Input: one variable name in camelCase (assume valid camelCase)
Output: the same name converted to snake_case
Example: preferredFirstName → preferred_first_name

def camel_to_snake(name: str) -> str:
  pass
'''
def camel_to_snake(name: str) -> str:
    snake_result = ""
    for letter in name:
        if letter.isupper():
            snake_result = snake_result + "_" + letter.lower()
        else:
            snake_result = snake_result + letter


    if snake_result.startswith("_"):
        snake_result = snake_result[1:]
    return snake_result

user_input = input("Enter a camelCase string to convert to snake_case: ")
print(camel_to_snake(user_input))