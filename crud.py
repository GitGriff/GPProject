#*******TABLES*******

#GENRE
#id, Genre

#TYPE_OF
#MovieID, GenreID

#MOVIE
#id, Name, Year, Runtime, Description

import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='deltona.birdnest.org',
                             user='my.diazn3',
                             password='Nd!@z201877',
                             db='my_diazn3_GPProject',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

def main():
    
    choice = 'h'
    
    print('Welcome to Group 7\'s Python SQL UI')
    
    while choice != 'q':
    
        #Attributes one wishes to create/read from/update/delete frpm a table
        q_att = ''
    
        #Which table we want to create/read from/update/delete
        q_table = ''
        
        #Conditions on read
        q_cond = ''
        
        #Limit on records retreived
        q_lim = ''
    
        if choice == 'h':
            print('To create a record, enter \t\t\'c\'')
            print('To read a record, enter \t\t\'r\'')
            print('To update a record, enter \t\t\'u\'')
            print('To delete create a record, enter \t\'d\'')
            print('To see tables in the database, enter \t\'w\'')
            print('To see this message again, enter \t\'h\'')
            print('To quit, enter \'q\'')
        
        choice = input("Enter your choice: ")
        
        if choice == 'c':
            q_table =   input("Enter the name of table you which to make a record for: ")

        
        elif choice == 'r':
            
            q_table =   input("Enter the name of the table you which to access: ")
            q_att =     input("Enter attributes you wish to see, seperated by commas: ")
            q_cond =    input("Enter conditions on search (\'none\' for no conditions): ")
            q_lim =     input("Enter number of records you wish to see (\'*\' for all records): ")
            
            try:
                with connection.cursor() as cursor:
                    # Reading records
                    sql = "SELECT " + q_att + " FROM " + q_table
                    
                    if q_cond != 'none':
                        sql += " WHERE " + q_cond
                    
                    print(sql)
                    
                    cursor.execute(sql)
                    
                    if q_lim == '*':
                        result = cursor.fetchall()
                        
                    else:
                        result = cursor.fetchmany(int(q_lim))
                        
                    print(result)
                
            except:
                print("Could not obtain records.")
                    
            else:
                print("Records obtained.")
    
        elif choice == 'u':
            q_table = input("Enter the name of the table you wish to update records for: ")
            
        elif choice == 'd':
            q_table = input("Enter the name of the table you which to delete a record from: ")
            
            q_cond = input("Enter the conditions of your delete (\'none\' for no conditions): ")
            
            sql = "DELETE FROM " + q_table
            
            if q_cond != "none":
                sql += " WHERE " + q_cond
            
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
            
            except:
                print("Unable to delete records.")
            
            else:
                print("Record deleted.")
            
        elif choice == 'w':
            print("Presenting tables and their attributes.")
            print(  "GENRE                                                      \n",
                    "+----+--------+                                            \n",
                    "| id | Genre  |                                            \n",
                    "+----+--------+                                            \n",
                    "                                                           \n",
                    "TYPE_OF                                                    \n",
                    "+---------+---------+                                      \n",
                    "| Movieid | Genreid |                                      \n",
                    "+---------+---------+                                      \n",
                    "                                                           \n",
                    "MOVIE                                                      \n",
                    "+----+------+-------------+---------+-------------+        \n",
                    "| id | Name | YearRelease | Runtime | Description |        \n",
                    "+----+------+-------------+---------+-------------+          ")
        
        elif choice == 'q':
            print("Quitting program.")   
            
        else:
            print("Enter \'h\' for help.")
    
    print("Connection will be closed.")
    connection.close()
                
main()