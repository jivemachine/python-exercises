

# For the following exercises, 
# read about and use the itertools module from the standard library to help you solve the problem.

# 1 How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

print(list(itertools.product("ABC", "123")))

9 lol

# 2 How many different ways can you combine two of the letters from "abcd"?

print(list(itertools.product("ABCD", repeat = 2))

16



#Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:
candy = json.load(open("profiles.json"))
#Total number of users
len(candy)
#Number of active users
active = [can["isActive"] for can in candy]
active = [can["isActive"] for can in candy if can["isActive"] == True]
len(active)
9
#Number of inactive users
notactive = [can["isActive"] for can in candy if can["isActive"] == False]
len(notactive)

10
#Grand total of balances for all users
balance = [can["balance"] for can in candy] # creating list of only the balances
balance = [b.lstrip("$") for b in balance] # removing dollar signs
balance = newbalance = [bal.replace(",","") for bal in balance] # removed commas

money_showers = []                         # placeholder
for item in newbalance:
    money_showers.append(float(item))      #converting to a FLOAT

sum(money_showers)

$52,667.02
#Average balance per user

mean_money = statistics.mean(money_showers) 

2771.95

#User with the lowest balance
user = [can["name"] for can in candy] # creating list of users
user_low = {money_showers[i]:user[i] for i in range(len(user))} # new dictionary of users and their money
min(user_low) = 1214.1       # lowest balance
user_low.get(1214.1) = "Avery Flynn"     # getting the name
Answer:


#User with the highest balance
max(user_low) = 3919.64    # max balance
user_low.get(3919.64)      # getting the name from the balance

answers:
Fay Hammond

#Most common favorite fruit
fruit = [can["favoriteFruit"] for can in candy] # list of all fruit
mode_fruit = statistics.mode(fruit)   # mode of fruit

#Least most common favorite fruit
min(fruit) = 'apple'

#Total number of unread messages for all users

messages = [can["greeting"] for can in candy]   # getting messages 
word_list = [item for item in messages for item in item.split(" ")]  # converting messages into GIANT LIST OF WORDS

# Grabbing numbers from list of strings
from itertools import groupby
number_list = [int(''.join(i)) for is_digit, i in groupby(word_list, str.isdigit) if is_digit] 

sum(number_list)

210

