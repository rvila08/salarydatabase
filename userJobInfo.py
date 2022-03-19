## Class for searching for average salaries based off of job title / company level

## Import operations library
from operations import operations

class userJobInfo:

    ## Main Interface For This Section
    ## Prompts user to choose between searching for average salaries by job title or company level
    def searchByUser(cursor):
        print("Would You Like To Search Salaries By Job Title or Company Level?")
        choice = input("Press 1 For Job Title. Press 2 For Company Level: ")

        ## User chooses job Title
        ## Prompts user to then choose to search for job title salaries by locations or companies
        if choice == "1":
            print("Would You Like To Search Based Off Location Or Company? ")
            choice_two = input("Enter 1 For Location and 2 For Company: ")

            ## Queries average salary for job titles by city
            if choice_two == "1":
                query_one = '''SELECT users.jobTitle, cities.cityName, AVG(salaries.totalYearlyCompensation)
                               FROM users
                               INNER JOIN salaries ON users.userID = salaries.salaryID
                               INNER JOIN cities ON salaries.cityID = cities.cityID
                               WHERE users.deleteFlag = 0 AND salaries.deleteFlag = 0
                               GROUP BY users.jobTitle, cities.cityName
                               ORDER BY users.jobTitle, cities.cityName DESC'''

                print("Displaying Average Salary By Job Title and City")
                location = operations.select(cursor,query_one)
                locationDF = operations.clean_data(location)
                print(locationDF)

                ## Gives user option to export to excel
                export_choice = input("Would You Like To Export To A CSV. Press 1 for Yes. Press 2 For No. ")

                ## Export to Excel (as CSV)
                if export_choice == "1":
                     operations.exportToCSV(locationDF)

                elif export_choice == "2":
                    pass

                ## Allows user to select one specific city and job title city
                choice = input("Would You Like To View A Specific City And Job Title? Press 1 For Yes. Press 2 For No. ")

                if choice == "1":
                    specificJobTitleCity(cursor)

                elif choice == "2":
                    ("Returning To Main Menu.")

                else:
                    print("Incorrect Selection.")
                    pass

            ## User chooses to search for average salaries by job title and company name
            elif choice_two == "2":
                query_two = ''' SELECT users.jobTitle, companies.companyName, AVG(salaries.totalYearlyCompensation)
                                FROM users
                                INNER JOIN salaries ON users.userID = salaries.salaryID
                                INNER JOIN companies ON salaries.companyID = companies.companyID
                                WHERE users.deleteFlag = 0 AND salaries.deleteFlag = 0
                                GROUP BY users.jobTitle, companies.companyName
                                ORDER BY users.jobTitle, companies.companyName DESC'''

                print("Displaying Average Salary By Job Title and Company")
                companies = operations.select(cursor, query_two)
                companiesDF = operations.clean_data(companies)

                print(companiesDF)

                ## Prompts user to export to CSV
                export_choice = input("Would You Like To Export To A CSV. Press 1 for Yes. Press 2 For No. ")

                ## Exports DF to CSV
                if export_choice == "1":
                     operations.exportToCSV(companiesDF)

                elif export_choice == "2":
                    pass

                ## Functionality to allow user to get the average salary a job title at one specific company
                choice = input("Would You Like To View Average Salary For A Job Title At A Specific Company? Press 1 For Yes. Press 2 For No. ")

                if choice == "1":
                    specificJobTitleCompany(cursor)
                elif choice == "2":
                    print("Returning to Main Menu")
                else:
                    print("Incorrect Selection.")
                    pass

            else:
                print("Incorrect Selection. Please Try Again.")
                pass

        ## SEARCHING FOR SALARIES BY JOB LEVEL
        elif choice == "2":
            print("Would You Like To Search Based Off Location Or Company? ")
            choice_two = input("Enter 1 For Location and 2 For Company: ")

            if choice_two == "1":
                query_one = '''SELECT companies.companyName, users.jobLevel, cities.cityName, AVG(salaries.totalYearlyCompensation)
                               FROM users
                               INNER JOIN salaries ON users.userID = salaries.salaryID
                               INNER JOIN cities ON salaries.cityID = cities.cityID
                               INNER JOIN companies ON salaries.companyID = companies.companyID
                               WHERE users.deleteFlag = 0 AND salaries.deleteFlag = 0
                               GROUP BY companies.companyName, users.jobLevel, cities.cityName
                               ORDER BY companies.companyName,users.jobLevel, cities.cityName DESC'''

                print("Displaying Average Salary By Job Level and City")
                location = operations.select(cursor,query_one)
                locationDF = operations.clean_data(location)
                print(locationDF)

                export_choice = input("Would You Like To Export To A CSV. Press 1 for Yes. Press 2 For No. ")

                if export_choice == "1":
                    operations.exportToCSV(locationDF)

                elif export_choice == "2":
                    pass

                choice = input("Would You Like To View Average Salary For A Job Level For A Specific City? Press 1 For Yes. Press 2 For No. ")

                if choice == "1":
                    specificJobLevelCity(cursor)
                elif choice == "2":
                    print("Returning to Main Menu.")

            elif choice_two == "2":
                query_two = ''' SELECT users.jobLevel, companies.companyName, AVG(salaries.totalYearlyCompensation)
                                FROM users
                                INNER JOIN salaries ON users.userID = salaries.salaryID
                                INNER JOIN companies ON salaries.companyID = companies.companyID
                                WHERE users.deleteFlag = 0 AND salaries.deleteFlag = 0
                                GROUP BY users.jobLevel, companies.companyName'''

                print("Displaying Average Salary By Job Level and Company")
                companies = operations.select(cursor, query_two)
                companiesDF = operations.clean_data(companies)
                print(companiesDF)

                export_choice = input("Would You Like To Export To A CSV. Press 1 for Yes. Press 2 For No. ")

                if export_choice == "1":
                    operations.exportToCSV(companiesDF)

                elif export_choice == "2":
                    pass

                choice = input("Would You Like To View Average Salary For A Job Level At A Specific Company? Press 1 For Yes. Press 2 For No. ")

                if choice == "1":
                    specificJobLevelCompany(cursor)
                elif choice == "2":
                    print("Returning to Main Menu.")

            else:
                print("Incorrect Selection. Please Try Again.")

        else:
            print("Incorrect Selection")
            pass

def specificJobLevelCity(cursor):
    city = input("Enter Name of City: ")
    jobLevel = input("Enter Name of Job Level: ")

    # query_three = ''' CREATE VIEW vJobLevelCity AS
    #                   SELECT users.jobLevel, cities.cityName, AVG(salaries.totalYearlyCompensation)
    #                   FROM users
    #                   INNER JOIN salaries ON users.userID = salaries.salaryID
    #                   INNER JOIN cities ON salaries.cityID = cities.cityID
    #                   WHERE cities.cityName = %s AND users.jobLevel = %s AND users.deleteFlag = 0 AND salaries.deleteFlag = 0
    #                   GROUP BY users.jobLevel, cities.cityName'''

    query_three = ''' SELECT * FROM vJobLevelCity'''

    user_choices= (city, jobLevel)

    result = operations.select(cursor, query_three)
    print("")
    print("Printing Average Salary Of", jobLevel, "In", city)
    print(operations.clean_data(result))

def specificJobLevelCompany(cursor):
    company = input("Enter Name of Company: ")
    jobLevel = input("Enter Name of Job Level: ")

    # query_three = '''
    #                   ALTER VIEW vJobLevelCompany AS
    #                   SELECT users.jobLevel, companies.companyName, AVG(salaries.totalYearlyCompensation)
    #                   FROM users
    #                   INNER JOIN salaries ON users.userID = salaries.salaryID
    #                   INNER JOIN companies ON salaries.companyID = companies.companyID
    #                   WHERE companies.companyName = %s AND users.jobLevel = %s AND users.deleteFlag = 0 AND salaries.deleteFlag = 0
    #                   GROUP BY users.jobLevel, companies.companyName'''

    user_choices=  (company, jobLevel)

    query_three = ''' SELECT * FROM vJobLevelCompany'''

    result = operations.select(cursor, query_three)
    print("")
    print("Printing Average Salary Of", "Level" , jobLevel, "At", company)
    print(operations.clean_data(result))


def specificJobTitleCity(cursor):
    city = input("Enter Name of City: ")
    jobTitle = input("Enter Name of Job Title: ")

    # query_three = ''' ALTER VIEW vSpecificJobTitleCity AS
    #                   SELECT users.jobTitle, cities.cityName, AVG(salaries.totalYearlyCompensation)
    #                   FROM users
    #                   JOIN salaries ON users.userID = salaries.salaryID
    #                   JOIN cities ON salaries.cityID = cities.cityID
    #                   WHERE cities.cityName = %s AND users.jobTitle = %s AND users.deleteFlag = 0 AND salaries.deleteFlag = 0
    #                   GROUP BY users.jobTitle, cities.cityName'''

    query_three = ''' SELECT * FROM vSpecificJobTitleCity'''

    user_choices=  (city, jobTitle)

    result = operations.select(cursor, query_three)
    print("")
    print("Printing Average Salary Of", jobTitle, "In", city)
    print(operations.clean_data(result))

def specificJobTitleCompany(cursor):
    company = input("Enter Name of Company: ")
    jobTitle = input("Enter Name of Job Title: ")

    # query_three = ''' ALTER VIEW vSpecificJobTitleCompany AS
    #                   SELECT users.jobTitle, companies.companyName, AVG(salaries.totalYearlyCompensation)
    #                   FROM users
    #                   INNER JOIN salaries ON users.userID = salaries.salaryID
    #                   INNER JOIN companies ON salaries.companyID = companies.companyID
    #                   WHERE companies.companyName = %s AND users.jobTitle = %s
    #                   AND users.deleteFlag = 0 AND salaries.deleteFlag = 0
    #                   GROUP BY users.jobTitle, companies.companyName'''

    query_three = ''' SELECT * FROM vSpecificJobTitleCompany'''

    user_choices=  (company, jobTitle)

    result = operations.select(cursor, query_three)
    print("")
    print("Printing Average Salary Of", jobTitle, "At", company)
    print(operations.clean_data(result))

def getUserInfo(userID):
    userID = str(userID).strip(''' ,()'" ''')
    query = "SELECT  * FROM users WHERE userID = " + str(userID) + ";"

    cursor.execute(operations.checkDelete(query),userID)
    info = cursor.fetchall()

    return info
