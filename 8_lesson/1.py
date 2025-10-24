import mariadb

connection = mariadb.connect(
    host='127.0.0.1',

    port=3306,

    user='root',

    password='password',

    database='people1',

    autocommit=True
)

print("Connected to Mriadb")

#CREATE USER 'anastasiia'@'localhost' IDENTIFIED BY '';
#GRANT ALL PREVILEGES ON people.* to
# Flush previlegieses
#GRANT SELECT, INSERT, UPDATE








def get_employees_by_last_name(connection, last_name):
    sql = "select number, Last_name, First_name, Salary from employee1 where last_name = ?"

    cursor = connection.cursor()

    cursor.execute(sql, (last_name,))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"Hello! I'm {row[2]}{row[1]}. My salary is {row[3]} euros per month")
    else:
        print(f"No employees with last name {last_name} found.")
    cursor.close()


def update_salary(connection, nb, new_salary):
    sql = "UPDATE Employee1 SET Salary= ? WHERE Number= ?"
    cursor = connection.cursor()
    cursor.execute(sql, (new_salary, nb))
    connection.commit()
    if cursor.rowcount != 0:
        print("Salary updated")
    else:
        print("Damn!")

ln = input("Enter the last name of the employee whose salary you wish to check: ")
get_employees_by_last_name(connection, ln)


nm = input("Enter employee id: ")
new_number = input("Enter new salary: ")
update_salary(connection, nm, new_number)
