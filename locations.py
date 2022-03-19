## Creates Class location
## Holds Functions For Querying By Geographical location

## Import Operations Library
from operations import operations

class locations:
    ## Extracts Average Salaries For Each Country
    ## Prints To User
    ## Allows User To Print All Records For That Country
    def searchByCountry(cursor):
        print("Displaying Average Salaries By Country: ")
        print("")
        query_two = '''SELECT cities.county, AVG(salaries.totalYearlyCompensation)
                       FROM cities
                       INNER JOIN salaries ON cities.cityID = salaries.cityid
                       WHERE salaries.deleteFlag = 0
                       GROUP by cities.county
                       '''
        salaries_by_country = operations.select(cursor,query_two)

        print(operations.clean_data(salaries_by_country))

        choice = input("Enter the Name of a Country To View All Salaries: ")

        query = '''SELECT cities.county, salaries.totalYearlyCompensation
                   FROM cities
                   INNER JOIN salaries ON cities.cityID = salaries.cityid
                   WHERE cities.county = %s AND salaries.deleteFlag = 0'''

        countries = operations.select_records(cursor, query, (choice,))

        print(operations.clean_data(countries))

    ## Extracts Average Salaries For Each State + Province
    ## Prints To User
    ## Allows User To Print All Records For That State/Province
    def searchByState(cursor):
        print("Displaying Salaries By US State or Canadian Province: ")
        print("")
        query_two = '''SELECT cities.stateProvince, AVG(salaries.totalYearlyCompensation)
                       FROM cities
                       INNER JOIN salaries ON cities.cityID = salaries.cityid
                       GROUP by cities.stateProvince
                       '''
        salaries_by_state = operations.select(cursor,query_two)

        print(operations.clean_data(salaries_by_state))
        choice = input("Enter the Abbreviation for an American State or Canadian Province To View All Salaries. Press 2 To Skip: ")

        if choice == "2":
            print("Returning to Main Menu.")
            return

        query =    '''
                   SELECT *
                   FROM salaries s
                   WHERE s.deleteFlag = 0 AND cityID = ANY (
                        SELECT cityID
                        FROM cities
                        WHERE stateProvince = %s
                   );
                   '''
        states = operations.select_records(cursor,query,(choice,))

        print(operations.clean_data(states))

    ## Extracts Average Salaries For Each City
    ## Prints To User
    ## Allows User To Print All Records For That City
    def searchByCity(cursor):
        print("Displaying Salaries By City: ")
        print("")
        query_two = '''SELECT cities.cityName, AVG(salaries.totalYearlyCompensation)
                   FROM cities
                   INNER JOIN salaries ON cities.cityID = salaries.cityid
                   GROUP by cities.cityName
                   '''

        salaries_by_cities = operations.select(cursor,query_two)

        print(operations.clean_data(salaries_by_cities))

        choice = input("Enter the Name of a City To View All Salaries. Press 2 To Skip: ")

        if choice == "2":
            print("Returning to Main Menu")
            return

        query =    '''
                   SELECT *
                   FROM salaries s
                   WHERE s.deleteFlag = 0 AND cityID = ANY (
                        SELECT cityID
                        FROM cities
                        WHERE cityName = %s
                   );
                '''


        cities = operations.select_records(cursor,query,(choice,))

        print(operations.clean_data(cities))
