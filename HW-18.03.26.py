#gets a list of numbs
#gets a n-th choice for decreasing order of the list
# later try to fix the out of range problem for n-th (non existent list position)

import random

def three_digit():

    '''
    this gets a input and checks if it is a number
    and if its between my limit of 3 digits, it returns it
    loops until get right input
    '''

    while True:
        numbers = input(f"Input a number of 3 digits:")

        if numbers.isdigit() and int(numbers) >= 100:
            return int(numbers)
        print(f"Invalid input. Try again.")

def descent_orderer(unique_list: list) -> list:
    '''

    this gets a list of unique numbers and sort them in descending order

    '''
    unique_list.sort(reverse=True)
    return unique_list


while True:
    user_number = three_digit()
    print (f"number chosen is: {user_number}")

    input_shuffle_list = [random.randint(0, user_number)\
                      for n in range(30)]
    print (f"Your generated random list (30 numbers can include duplicates):\n {input_shuffle_list}")

    unique_list = list(set(input_shuffle_list))   # here i take out duplicates

    sorted_unique_list = descent_orderer(unique_list)
    print(f"This is the sorted list (without duplicates):\n {sorted_unique_list}")

    while True:
        n = int(input("Enter a number for n ( n will be the position of that number in descending order):  "))
        print (f" The number in {n}-th biggest position is: {sorted_unique_list[n - 1]} ")

        n_return = input("Want to continue checking positions yes/no?:").lower()
        if n_return != "yes":
            break

    print("Goodbye than!")


