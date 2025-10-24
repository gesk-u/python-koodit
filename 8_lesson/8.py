import mariadb

print(mariadb.__version__)

print("yep")

def get_employees_by_last_name(connection, last_name):
    sql = "select number, Last_name, First_name, Salary from employee1 where last_name = ?"

    cursor = connection.cursor()

    cursor.execute(sql, (last_name,))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"Hello! I'm {row[2]}{row[1]}. My salary is {row[3]} euros per month")
    return