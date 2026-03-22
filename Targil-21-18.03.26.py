########## 1 ############
'''
input number from the user --  88949
user_input_list = [88949]
'''

user_input = input("Input a few numbers:")
print(f" This is your input:{user_input}")


# this formula gives me back a list plus takes out the spaces between the str if add .split(input)
user_input_list_int = [int(n) for n in user_input]
user_input_list = list(user_input) # still a list of str

print(f" the user input as list of int is: {user_input_list_int}")
print(f" the user input as list of str is {user_input_list}")

''''
print the number in REVERSE -- 94988
'''

user_input_list_int.reverse()
print(f" This is the reversed list:{user_input_list_int}")
#print(f" the reverse of {user_input} is: {user_input[::-1]}") # slicing vers for when str

#reverse_list = "".join(user_input_list) # joins the list back to being a str
#print(f" This is the reversed list: {reverse_list}")

'''
print the biggest digit -- 9
'''
biggest = max(user_input_list_int)
print(f" This is the biggest digit: {biggest}")

'''
print how many times the biggest digit appears? -- 2
'''
counter = user_input_list_int.count(biggest)
print(f" The biggest number -> {biggest}, appears {counter} times")

'''
print the min digit -- 4 
'''
shortest = min(user_input_list_int)
print(f" This is the shortest digit: {shortest}")


'''
print the sum of digits -- 38 
'''
total = sum(user_input_list_int)
print(f" the sum of all digits is: {total}")

'''
print the avg of digits -- 8+8+9+4+9 / 5
'''

average = total/len(user_input_list_int)
print(f" The average for digits input is: {average:.2f}")

print("*"*25)

########## 2 ############
'''
write a function that gets a list of numbers and returns if the list is sorted or not
'''


def is_sorted(numbers: list) -> bool:
    return numbers == sorted(numbers)

user_numbers = input("Input serial of spaced numbers:")
numbers = [int(n) for n in user_numbers.split()]

print(f" the {numbers} sorting is {is_sorted(numbers)}")
print("-"*20)

def is_sorted_2(numbers: list) -> bool:
    for n in range(len(numbers) - 1):
        if numbers[n] > numbers[n + 1]:
            return False
    return True

user_numbers = input("Input serial of spaced numbers:")
numbers = [int(n) for n in user_numbers.split()]

print(f" the {numbers} sorting is {is_sorted_2(numbers)}")
print("-"*20)

'''
write a function that gets a list of numbers (with duplication), n-th biggest and returns it
i.e. [88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , 4 --> will return 95 (because it is the 4-th biggest after 100, 99, 97, 95)
'''

def biggest_in_list(numbers: list, n: int) -> list:
