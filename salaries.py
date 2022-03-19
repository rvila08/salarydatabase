## Class For Extracting Salary Data

## Import Operations Library
from operations import operations

class salaries:

    ## Prompts User To Enter Min + Max Salary...
    ## Prints All Records Within That range
    ## maybe we should add functionality to print more than just salaries and ids
    def searchBySalaries(cursor):
        int1 = input("What is the minimum salary you are looking for? ")
        int2 = input("What is the maximum salary you are looking for? ")

        print("Searching For All Salaries Between", int1, "And", int2, "...")

        try:
                query = '''
                SELECT totalYearlyCompensation, yearsatcompany, basesalary, stockgrantvalue, bonus, deleteFlag
                FROM salaries
                WHERE totalYearlyCompensation >=''' + int1 +  ''' AND totalYearlyCompensation <= ''' + int2;

                cursor.execute(operations.checkDelete(query))
                salaries = cursor.fetchall()

                print(operations.clean_data_with_flags(salaries))
        except:
           print("Couldn't Find Any Records Within That Range.")
           print("")
           if type(int1) == str or type(int) == str:
               print("Please Enter Numerical Values.")
           pass
