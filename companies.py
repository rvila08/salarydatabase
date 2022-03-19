## Creates Class "companies"
## Holds Functions Responsible For Extracting Company Data

## Import Operations Library
from operations import operations

class companies:

    ## Function That Queries and Retrieves All Company Information
    ## Displays For User
    ## Add Functionality That Allows User To Select One Company?
    def getCompanyInfo(cursor):
        print("Displaying All Company Information...")

        # query = '''CREATE VIEW vCompanies AS
        #            SELECT c.companyName, i.industryName
        #            FROM companies c
        #            INNER JOIN industries i ON i.industryID = c.industryID
        #            '''

        query = ''' SELECT *
                    FROM vCompanies
                '''
        companies = operations.select(cursor,query)

        print(operations.clean_data(companies))
