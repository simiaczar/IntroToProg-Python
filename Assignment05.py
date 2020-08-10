# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Carl Caba, 08.10.20 ,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open('ToDoList.txt', 'r')
for row in objFile:
    task, value = row.split(',')
    dicRow = {'TASK': task, 'PRIORITY': value}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print('Your Current Data is: ')
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strName = str(input('What is the task?: '))
        strValue = str(input('Enter a priority for the task [Low to High]: '))
        dicRow = {'TASK': strName, 'PRIORITY': strValue}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strItem = input('What task did you complete?: ')
        for row in lstTable:
            if row['TASK'].lower() == strItem.lower():
                lstTable.remove(row)
                print(strItem, 'has been successfully removed')
            else:
                print('Sorry, but', strItem, " couldn't be found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['TASK'] + ',' + row['PRIORITY'] + "\n")
        objFile.close()
        print('The data has been successfully saved!')
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        input('Press enter to exit the program')
        break  # and Exit the program

