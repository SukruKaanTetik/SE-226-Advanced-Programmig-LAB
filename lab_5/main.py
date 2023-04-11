from word_data import words
import random

# QUESTION 1
def passGen(user_no):
    if not 3 < user_no < 7:
        print("Enter a valid value")

    else:
        password = ""
        for i in range(user_no):
            password += words[random.randint(1, 999)]

        password = password[::-1]
        return password


# QUESTION 2
def rep_with_upper(word):
    letter = random.choice(word)
    word_list = list(word)
    new_word = ""

    for i in range(len(word_list)):
        if word_list[i] == letter:
            word_list[i] = letter.upper()

    word = new_word.join(word_list)
    return word


def swap_letters(word):
    word_list = list(word)
    n_letters = len(word_list)
    new_word = ""

    word_list[0], word_list[n_letters-2] = word_list[n_letters-2], word_list[0]
    word_list[1], word_list[n_letters-1] = word_list[n_letters-1], word_list[1]

    new_word = new_word.join(word_list)
    return new_word


# QUESTION 3
def search_letter(letter, word):
    if letter in word:
        return True
    return False

# EXECUTION
user_number = 0
while (user_number < 3) or (user_number > 7):
    print("Enter a user number between 3 and 7........................")
    user_number = int(input("Enter the number: "))
    
random_password = passGen(user_number)
final_password = swap_letters(rep_with_upper(random_password))

print(f"First Password: {random_password}")
print(f"Final Password: {final_password}")


print(search_letter("k", final_password))
