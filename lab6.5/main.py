# QUESTION 1

def common_converter(list1, list2):
    new_list = set(list1).intersection(list2)
    return new_list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 6, 7, 8]
print("COMMON ELEMENTS: ", common_converter(list1, list2))


# QUESTION 2

def palindromes(str_list):
    pal_list = []
    for word in str_list:
        if word == word[::-1]:
            pal_list.append(word)
    return pal_list

words = ["deed", "hello", "kaan", "noon", "peep", "deliver", "hang"]
print("PALINDROME LIST: ", palindromes(words))


# QUESTION 3

def sieve_of_eratoshenes(number_list):
    list.sort(number_list)

    for number in number_list:
        if number == 1:
            continue

        for delete_n in number_list:
            if (delete_n >= number**2) and (delete_n%number == 0):
                number_list.remove(delete_n)

    return number_list


number_list = []
for i in range(1, 50):
    number_list.append(i)
print(sieve_of_eratoshenes(number_list))


# QUESTION 4

def anagrams(word, word_list):
    anagram_list = []
    word_l = list(word)
    list.sort(word_l)
    word_l = [*set(word_l)]


    for x in word_list:
        x_list = list(x)
        list.sort(x_list)
        x_list = [*set(x_list)]
        if x_list == word_l:
            anagram_list.append(x)

    return anagram_list


word_listt = ["enlists", "google", "inlets", "banana"]
print("ANAGRAM: ", anagrams("listen", word_listt))
