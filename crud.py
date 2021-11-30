import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='deltona.birdnest.org',
                             user='CSCI355',
                             password='CSCI355',
                             db='IPAllocations',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        # Reading records record
        sql = "SELECT name FROM cityByCountry WHERE country=%s"
        cursor.execute(sql, [226])
        result = cursor.fetchmany(size=10)
        print(result)
        
finally:
    connection.close()
