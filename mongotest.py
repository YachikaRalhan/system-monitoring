from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData


def insert():
    employeeId = raw_input('Enter Employee id :')
    employeeName = raw_input('Enter Name :')
    employeeAge = raw_input('Enter age :')
    employeeCountry = raw_input('Enter Country :')

    db.Employees.insert_one(
        {
            "id": employeeId,
            "name": employeeName,
            "age": employeeAge,
            "country": employeeCountry
        })
    print '\nInserted data successfully\n'


def read():
    empCol = db.Employees.find()
    print '\n All data from EmployeeData Database \n'
    for emp in empCol:
        print emp



def update():
    criteria = raw_input('\nEnter id to update\n')
    name = raw_input('\nEnter name to update\n')
    age = raw_input('\nEnter age to update\n')
    country = raw_input('\nEnter country to update\n')

    db.Employees.update_one(
        {"id": criteria},
        {
            "$set": {
                "name": name,
                "age": age,
                "country": country
            }
        })
    print "\nRecords updated successfully\n"


def delete():
    criteria = raw_input('\nEnter employee id to delete\n')
    db.Employees.delete_many({"id": criteria})
    print '\nDeletion successful\n'


if __name__ == "__main__":

    while (1):
        # chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print '\n INVALID SELECTION \n'
