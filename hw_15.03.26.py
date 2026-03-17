#1 question

#Write a function that groups words by number of letters
#The key should be the length of the word, and the value should be a list of all words with that length
'''
:param words: list of words
:return: dict { <length>: [list of words with that length] }

'''

fruit_words = ["apple","banana","kiwi","grape","melon","pear"]

def group_words_by_length(fruit_words: list) -> dict:
    dictionary_words = {}

    for word in fruit_words:
        length = len(word)

        if length not in dictionary_words:
            dictionary_words[length] = [word]

        else:
            dictionary_words[length].append(word)


    return dictionary_words

print(group_words_by_length(fruit_words))
print("-" * 20)

#2 question

#Write a function that calculates the average grade of all students
'''
    :param grades: {<name>: <grade>}
    :return: average grade of all students
    
'''

grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

def get_average_grade(grades: dict) -> float:
    students_amount = 0
    total_grade = 0

    for name, grade in grades.items():
        total_grade += grade
        students_amount += 1

    average_grade = total_grade / students_amount
    return average_grade

print(get_average_grade(grades))
print("-" * 20)

#3 question

'''
    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
'''

numbers = [4, -2, 0, 7, -5, 3]

def group_numbers(numbers: list) -> dict:
    dictionary = {
        "positive": [],
        "negative": [],
        "zero": [],
    }
    for num in numbers:
        if num > 0:
            dictionary["positive"].append(num)
        elif num < 0:
            dictionary["negative"].append(num)
        else:
            dictionary["zero"].append(num)

    return dictionary

print(group_numbers(numbers))
print("-" * 20)