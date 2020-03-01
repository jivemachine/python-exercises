# 1 Read the contents of your last exercise file into a variable.
with open('4.6_import_exercises.py') as ie:
    import_exercises = ie.read()

#Print out every line in the file
print(import_exercises)

line = import_exercises.split('\n')

with open('4.6_import_exercises.py') as ie:
    import_exerises = ie.readlines()

#Print out every line in the file, but add a line numbers
with open('4.6_import_exercises.py') as ie:

for line_number, enumerate(import_exercise):

for line_number, line in enumerate(import_exercises):
    if (line_number, line):
        print(line)    



with open(filename, "r") as openfile:
    with open(filename2, "w") as out_file:
        for j, line in enumerate(openfile):
            out_file.write('{0:<5}{1}'.format(j+1, line))

    


for j, line in enumerate(import_exercise):
            out_file.write('{0:<5}{1}'.format(j+1, line))


count = 1
for lines in import_exercises:
    print str(count) + lines
    count += 1


count = 1
for lines in import_exercises:
    print(lines)
    count += 1



newFile = open('4.6_import_exercises.py', 'w')
count = 1

for line in readfile:
    newFile.write (str(count)+'\t'+line)
    count+=1
newFile.close()   

for line in enumerate(import_exercises):
    print line

for count, line in enumerate(import_exercises):
    print(count, line)

# 2 Write some python code to create a grocery list.

grocery_list = ["mayonnaise", "pancakes", "sugar plums"]

#Create a variable named grocery_list. It should be a list, 
# and the elements in the list should be a least 
# 3 things that you need to buy from the grocery store.

#Create a function named make_grocery_list. 
# When run, this function should write the contents of the grocery_list 
# variable to a file named my_grocery_list.txt.

with open('myfile.txt', 'w') as f:
    f.write(file_contents)




def make_grocery_list(add_list):
    with open('my_grocery_list.txt', 'w') as f:
        for add_list in f:
            f.write('%s\n' % add_list)
            

def make_grocery_list(add_list):
    for item in add_list:

newgrocerylist = open(my_grocery_list.txt, 'w')
yourResult = [line.split(',') for line in newgrocerylist.readlines()]        

def make_grocery_list(add_list):
    allLines = []
    for file in add_list:
        f = open(file,'r')



def readFile(allFiles):
    with open ('"my_grocery_list.txt', mode='wt', encoding='utf-8') as fileOutput:
        for file in allFiles:
            with open(file) as reader:
                for line in reader:
                    fileOutput.write(line)        

f = open('my_grocery_list', 'r')
wordlist = f.read()
f.close()


###### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ THIS IS THE ANSWER  THAT I HAVE SLAVED FOR

def make_grocery_list(add_list):
    item = [list for list in add_list]
    with open("my_grocery_list.txt", "w") as f:
        f.write(str(grocery_list))




#Create a function named show_grocery_list. 
# When run, it should read the items from the text file and 
# show each item on the grocery list.

def show_grocery_list(x):
    with open() as f:
        file_contents = f.read()
    print(file_contents)
#Create a function named buy_item. 
# It should accept the name of an item on the grocery list, 
# and remove that item from the list.