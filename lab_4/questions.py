from words_data import words  # 1000 word list
import random



# QUESTION 1

print("Enter two numbers between 0 and 1000 that second is greater than first.................")

while True:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if (number2 > number1) and (0 < number1 < 1000) and (0 < number2 < 1000):
        print("Numbers are valid. Here is the slice of the list.......")
        break
    else:
        print("Numbers entered are not valid. Please check and enter again")


for data in words[number1:number2]:
    print(data)

    

# QUESTION 2

print("Enter a user number between 3 and 7........................")
while True:
    user_number = int(input("Enter the number: "))
    if 3 < user_number < 7:
        break
    else:
        print("Enter a valid number")

password = ""
for i in range(user_number):
    password += words[random.randint(1, 999)]

password = password[::-1]
print(f"Password: {password}")




# QUESTION 3

shorter = set()
longer = set()
password_count = 0

print("Enter user numbers between 3 and 7 to create passwords....................")
while True:
    if password_count == 8:
        break

    password = ""
    user_number = int(input("Enter number: "))

    if 3 < user_number < 7:
        password_count += 1
        for i in range(user_number):
            password += words[random.randint(1, 999)]
        password = password[::-1]

        if user_number < 5:
            shorter.add(password)
        else:
            longer.add(password)

    else:
        print("Enter a valid number")


all_password = shorter.union(longer)

for password in all_password:
    print(password)




# QUESTION 4

my_dictionary = {}

# a
for i in range(1,31):
    my_dictionary[i] = i * (i-1)

print(my_dictionary)

# b
for key in my_dictionary:
    print(f"{key} : {my_dictionary[key]}")

# c
sum = 0
for value in my_dictionary.values():
    sum += value

print(f"Sum of the keys:  {sum}")

# d

delete_key = int(input("Enter a key value to delete: "))

if delete_key in my_dictionary.keys():
    my_dictionary.pop(delete_key)

else:
    print("Key number you entered is not in dictionary")


# QUESTION 5

divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {}
united_we_stand.update(divided)
united_we_stand.update(we_fall)

print("{:<10} {:<10}".format("Name", "Age"))
for key in united_we_stand.keys():
    print("{:<10} {:<10}".format(key, united_we_stand[key]))
    
# b
united_we_stand.pop("Nat")
for key in united_we_stand.keys():
    print("{:<10} {:<10}".format(key, united_we_stand[key]))

# c
sorted_list = sorted(united_we_stand.keys())
tmpDic = {}
for keys in sorted_list:
    tmpDic[keys] = united_we_stand[keys]

united_we_stand = tmpDic
for key in united_we_stand.keys():
    print("{:<10} {:<10}".format(key, united_we_stand[key]))

# d
print(f"Max Value: {max(united_we_stand.values())}")
print(f"Min Value: {min(united_we_stand.values())}")
