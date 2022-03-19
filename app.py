## Import Libraries
import mysql.connector
import pandas as pd
from operations import operations
from locations import locations as loc
from companies import companies as co
from salaries import salaries as sal
from userJobInfo import userJobInfo as usjo

## Make Connection to SQL
## Input Your Own User and PW
connection = mysql.connector.connect(
    host = "35.193.110.141",
    user = "jeremy",
    password = "password1",
    database = "finalproject"
)

cursor = connection.cursor()

## Import Data - Make Sure Path is Your Own
#geographies = operations.importData("c:/Users/jerem/Documents/CPSC_Courses/CPSC_408/final_project/Data/Geography.csv")
#companies = operations.importData("c:/Users/jerem/Documents/CPSC_Courses/CPSC_408/final_project/Data/Companies.csv")
#salaries = operations.importData("c:/Users/jerem/Documents/CPSC_Courses/CPSC_408/final_project/Data/Salaries.csv")

#print(companies.head())

#geographies = geographies.where((pd.notnull(geographies)), None)
#companies = companies.where((pd.notnull(companies)), None)
#salaries = salaries.where((pd.notnull(salaries)), None)


#### INSERT ENTITIES INTO MYSQL
## Insert Geography Data
# geo_table = []
# for idx, row in geographies.iterrows():
#
#     cityid = row['cityid']
#     cityName = row['cityName']
#     stateProvince = row ['stateProvince']
#     country = row ['country']
#
#     geo_table.append((cityid,cityName,stateProvince,country))
#
# for i in geo_table:
#     cursor.execute('''INSERT INTO geographies VALUES (%s,%s,%s,%s)''', i)
#
# print("Geography Data Inserted")

# Insert Company Data
#companies_table = []
#print("Inserting Company Data")

#for idx,row in companies.iterrows():
    #companyid = row['companyid']
    #companyName = row['companyName']

    #companies_table.append((companyid, companyName))

#for i in companies_table:
    #cursor.execute('''INSERT INTO companies VALUES (%s,%s)''', i)

#print("Company Data Inserted")
#connection.commit()

## Insert Salary Data

#def insertSalary():

#    salaries_table = []
#    print("Inserting Salary Data")
#
#    for idx,row in salaries.iterrows():
#        salaryid = int(row['salaryID'])
#        yearsAtCompany = int(row['yearsatcompany'])
#        yearlyComp = int(row['totalyearlycompensation'])
#        baseSalary = int(row['basesalary'])
#        stockGrant = int(row['stockgrantvalue'])
#        bonus = int(row['bonus'])
#
#        salaries_table.append((salaryid, yearsAtCompany, yearlyComp, baseSalary, stockGrant, bonus))
#
#    count = 0
#    for i in salaries_table:
#        count += 1
#        cursor.execute('''INSERT INTO salaries VALUES (%s,%s,%s,%s,%s,%s)''', i)
#        print(count, "row inserted")
#
#    print("Salary Data Inserted")
#    connection.commit()



def searchByCompany():
    query = '''
    SELECT DISTINCT companyName
    FROM companies;

    '''
    #list all company names
    cursor.execute(checkDelete(query))
    companies = cursor.fetchall()

    choices = {}
    for i in range(len(companies)):
        print(str(i) + '. ' + str(companies[i]).strip(''' ,()'" '''))
        choices[i] = companies[i]

    index = helper.get_choice(choices.keys())

    #index is the number which user selects -- return company info/ salaries within company

def searchSalaryByField():
    query = '''
    SELECT DISTINCT title
    FROM users
    '''

def searchByLocation():
    choice = input('''Do you want to search by:

    1. Country
    2. State
    3. City
    ''')

    #query = '''
    #SELECT %s

    #'''
    if choice == "1":
        loc.searchByCountry(cursor)
        mainmenu()
    elif choice == "2":
        loc.searchByState(cursor)
        mainmenu()
    elif choice == "3":
        loc.searchByCity(cursor)
        mainmenu()
    else:
        print("Incorrect Option")
        searchByLocation()

## 12/3 - Query Functions to Extract Geographic Info Based On User Choice
## 12/4 - Added in queries to print the average salary by location
##        and then prompts the user to select a location and print all salaries



## 12/3 - Improved the Front End of Applicaiton
## Connected Some of Menus and Functions Together
## Also Added Some Error Functionality, app won't break if user enters incorrect option on main menu
def mainmenu():

    user_choice = input('''
    Welcome to the Database. Please Select an Option Below:
    Select the Corresponding Number.

    1. Search
    2. Update User Information
    3. Delete
    4. Rollback
    5. Create New User
    6. Exit the Application
    ''')

    if user_choice == "1":
        optionsMenu2()
    elif user_choice == "2":
        optionsMenu3()
    elif user_choice == "3":
        username = input("Enter the username of the record you would like to delete" + '\n')
        operations.flagRecord(username, cursor, connection)
        print("User deleted!")
        mainmenu()
    elif user_choice == "4":
        print("Test")
    elif user_choice == "5":
        username = input("Enter Username: " + '\n')
        dob = input("Enter date of birth: " + '\n')
        age = input("Enter age: " + '\n')
        fullName = input("Enter full name: " + '\n')
        jobTitle = input("Enter job title: " + '\n')
        yearsExp = input("Enter years of experience: " + '\n')
        joblvl = input("Enter job level: " + '\n')
        createNewUser(username,dob,age,fullName,jobTitle,yearsExp,joblvl)

    elif user_choice == "6":
        print("Exiting Application...")
    else:
        print("Incorrect Input.")
        mainmenu()

def optionsMenu1():

    choice = input('''
    Would you like to:
    1. Choose a record
    2. Go Back to Main menu
    3. Export

    ''')

    if choice == 1:
        optionsMenu2()
    elif choice == 2:
        mainmenu()
    elif choice == 3:
        exportCSV()

def optionsMenu2():

    user_choice = input('''
    Do you want to look at:
    1. Salary information
    2. Company information
    3. User + Job Information
    4. Job Location

    ''')

    if user_choice == "1":
        sal.searchBySalaries(cursor)
        mainmenu()
    elif user_choice == "2":
        co.getCompanyInfo(cursor)
        mainmenu()
    elif user_choice == "3":
        usjo.searchByUser(cursor)
        mainmenu()
    elif user_choice == "4":
        searchByLocation()

def optionsMenu3():
    username = input('''
    Enter the username for the account you'd like to update

    ''')

    query = "SELECT userID FROM users WHERE username = '" + str(username) + "';"


    cursor.execute(query)
    userID = cursor.fetchone()

    userInfo = getUserInfo(userID)
    print("0. Username: " + str(userInfo[0][1]))
    print("1. DOB: " + str(userInfo[0][2]))
    print("2. Age: " + str(userInfo[0][3]))
    print("3. Full Name: " + str(userInfo[0][4]))
    print("4. Job Title: " + str(userInfo[0][5]))
    print("5. Years of Experience: " + str(userInfo[0][6]))
    print("6. Job Level: " + str(userInfo[0][7]))

    choice = input("\n" + "Select the corresponding number for the value you would like to change" + "\n")
    newVal = input("What would you like to change the value to?" + "\n")
    columns = ['username','dateOfBirth','age','fullName','jobTitle', 'yearsExperience', 'jobLevel']

    pickedColumn = ''
    for x in range(6):
        if int(choice) == x:
            pickedColumn = columns[x]

    if int(choice) == 0 or int(choice) == 1 or int(choice) ==  3 or int(choice) == 4 or int(choice) == 6:
        query = "UPDATE users SET " + pickedColumn + " = '" + str(newVal) + "' WHERE userID = " + str(userInfo[0][0]) + ";"
    else:
        query = "UPDATE users SET " + pickedColumn + " = " + str(newVal) + " WHERE userID = " + str(userInfo[0][0]) + ";"

    cursor.execute(query)
    connection.commit()

userCount = 0


def createNewUser(username, dob, age, fullName, jobTitle, yearsExp, jobLevel):

    query = "SELECT COUNT(*) FROM users"
    cursor.execute(query)
    userCount = str(cursor.fetchone()).strip(''' ,()'" ''')
    userCount1 = 234
    newUserID = int(userCount1) + 1
    query1 = "INSERT INTO users (userID, username, dateOfBirth, age, fullname, jobTitle, yearsExperience, jobLevel, deleteFlag) VALUES(" + str(newUserID) + ",'" + str(username) + "','" + str(dob) + "'," + str(age) + ",'" + str(fullName) + "','" + str(jobTitle) + "'," + str(yearsExp) + ",'" + str(jobLevel) + "',0);"
    #trans.beginTrans(cursor,query1,connection)
    cursor.execute(query1)
    connection.commit()
    mainmenu()

def getUserInfo(userID):
    userID = str(userID).strip(''' ,()'" ''')
    query = "SELECT  * FROM users WHERE userID = " + str(userID) + ";"

    cursor.execute(query,userID)
    info = cursor.fetchall()

    return info

#operations.unflagAllRecords(cursor,connection)
mainmenu()
#searchByCompany()
