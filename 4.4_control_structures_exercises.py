

# 1
#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
it_is_monday = False
if it is monday:
    print("Today is indeed Monday...") 
else:
    print("Monday is not today.")  

the_day_of_the_week = input("What is the day: ")
if the_day_of_the_week in ["Monday", "monday"]:
    print("The day of the week is indeed monday!")
else:
    print("The day of the week is NOT MONDAY!")  
#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = "Thursday"
if day_of_the_week in ["Saturday" or  "Sunday"]: 
    print("It is the weekend!")
else:
    print("It is a weekday.")

weekend_input_day = input("What day is it!?!?!")
if weekend_input_day in ["Saturday", "saturday", "Sunday", "sunday"]:
    print("ITS THEVWEEKEND!!!")
else:
    print("Go to bed and go to work!")
#create variables and make up values for

#the number of hours worked in one week
hours_per_week = 55
#the hourly rate
hourly_rate = 50
#how much the week's paycheck will be
paycheck = hours_per_week * hourly_rate
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
overtime = (hourly_rate * 1.5) * (overtime_hours_worked)

(REAL ANSWER)
overtime = ((hours_per_week % 40) * (1.5 * hourly_rate) + ((40 % hours_per_week) * hourly_rate)





# 2 
#Loop Basics

#While

#Create an integer variable i with a value of 5.
i = 5
#Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    i =+ 1
#Each loop iteration, output the current value of i, then increment i by one.
#Your output should look like this:


5
6
7
8
9
10
11
12
13
14
15

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i <= 1_000_000:
    print(i)
    i = i * i

 2
 4
 16
 256
 65536
#Write a loop that uses print to create the output shown below.
i = 100
while i <= 5:
    print(i)
    i -= 5


100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5



# B

#For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
number_enter = int(input("Give us a number: "))
for number in range(1,11):
    print(number_enter, "X",number,"=", number_enter * 10)
#For example, if the user enters 7, your program should output:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

#Create a for loop that uses print to create the output shown below.
for number in range(1,10):
    print(str(number) * number)
1
22
333
4444
55555
666666
7777777
88888888
999999999


# C

#break and continue

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
gimmie_number = int(input("Give us an odd number between 1 and 50"))


for n in range(1,51): 
    if n % 2 == 0: 
        continue
    print("Here is an odd number: {}".format(n)) 
    if n == gimmie_number: 
        break 
    print("Yikes! Skipping number: {}".format(gimmie_number)) 
#Your output should look like this:

Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49

#The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)


#Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# 3 Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.


#Write a program that prints the numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i + 1
#For multiples of three print "Fizz" instead of the number
 while i <= 100:
     print(i) 
     i += 1 
     if (i % 3 == 0):
         print("Fizz")
     if (i % 5 == 0):
         print("Buzz")
     if (i % 3 == 0 and i % 5 == 0):
         print("FizzBuzz")

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    if num % 3 == 0:
        print("Fizz")
        continue
    if num % 5 == 0:
        print("Buzz")
        continue
    print(num)        
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

# 4 Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
#Example Output
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125

Bonus: Research python's format string specifiers to align the table

# 5 Convert given number grades into letter grades
#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

#A : 100 - 88
#B : 87 - 80
#C : 79 - 67
#D : 66 - 60
#F : 59 - 0

# BONUS 
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# 6 Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

# 6 Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
