import mysql.connector

def connectsql(host, user, password):
    # Creating connection object
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
    
    # Printing the connection object
    print(mydb)
    return mydb