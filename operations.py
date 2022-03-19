## Import Libraries
import pandas as pd
import sqlite3

class operations:
    ## Import Data - Make Sure Path is Your Own
    def importData(path):
        data = pd.read_csv(path)
        df = pd.DataFrame(data)
        return df

    ## Select Records With User Parameter
    def select_records(cursor, query, dictionary):
        cursor.execute(query,dictionary)
        return cursor.fetchall()

    ## Select Records (No User Input)
    def select(cursor, query):
        cursor.execute(query)
        return cursor.fetchall()

    def select(cursor, query):
        cursor.execute(query)
        return cursor.fetchall()


    ## Cleans the Tuple From Query
    def clean_data(results):
        list = []

        for x in range(len(results)):
            list.append(results[x])

        df = pd.DataFrame(list)
        return df

    def clean_data_with_flags(results):
        list = []
        counter = 0

        for x in range(len(results)):
            list.append(results[x])

        deleteColIndex = len(list[0])-1
        df = pd.DataFrame(list)
        #drop the deleteFlag Column
        df = df.drop(columns = [deleteColIndex], axis = 1)
        return df

    def exportToCSV(data):
        fileName = input("Enter the Name of Export File (Must Be CSV Format): ")
        fileName = str(fileName)

        data.to_csv(fileName)
        print("Data Exported.")

    #creates a subquery which filters records with delete = 0
    def checkDelete(query):
        newQuery = "SELECT * FROM(" + query + ") AS newTable WHERE deleteFlag = 0 "
        return newQuery

    def unflagAllRecords(cursor,connection):
        table = ['users','salaries','companies']

        for x in table:
            query = "UPDATE " + x + " SET deleteFlag = 0"
            cursor.execute(query)
            connection.commit()

    def flagRecord(username, cursor, connection):
        query = "UPDATE users SET deleteFlag = 1 WHERE username = '" + username + "';"
        cursor.execute(query)
        query1 = "SELECT userID FROM users WHERE username = '" + username + "';"
        cursor.execute(query1)
        salaryID = str(cursor.fetchone()).strip(''' ,()'" ''')
        query2 = "UPDATE salaries SET deleteFlag = 1 WHERE salaryID = '" + str(salaryID) + "';"
        cursor.execute(query2)
        connection.commit()
