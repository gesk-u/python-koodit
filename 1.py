connection = mariadb.connect(
    host='127.0.0.1',

    port=3306,

    user='root',

    password='password',

    database='people1',

    autocommit=True
)
