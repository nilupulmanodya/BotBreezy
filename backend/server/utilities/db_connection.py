import mysql.connector
from .db_auths import auths

mydb = mysql.connector.connect(
  host=str(auths.host),
  user=str(auths.user),
  password=str(auths.password),
    database =str(auths.database)
)
mycursor = mydb.cursor()

print("mysql connection success for server : ",mydb) 
