from mysql.connector import Error, connect
import sql_config

def connection_to_SQL(host_name, username, user_password, database_name):
    connection = ""
    try:
        connection = connect(
            host=host_name,
            user=username,
            password=user_password,
            database=database_name

        )
        cursor = connection.cursor()
        print("Connection successful")
    except Error:
        print("Error: " + {Error})
    
    return connection, cursor

connection_to_SQL(sql_config.mydb._host,sql_config.mydb._user, sql_config.mydb._password, sql_config.mydb.database)

mycursor = sql_config.mydb.cursor()

mycursor.execute("USE fitness_buddy")
