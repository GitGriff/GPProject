#*******TABLES*******

#GENRE
#id, Genre

#TYPE_OF
#MovieID, GenreID

#MOVIE
#id, Name, Year, Runtime, Description

#Our method of preventing SQL injection is by using paramterized SQL statements

import pymysql.err
import pymysql.cursors
import pymysql
import MySQLdb


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
            #Print our options for user
            print('To create a record, enter \t\t\'c\'')
            print('To read a record, enter \t\t\'r\'')
            print('To update a record, enter \t\t\'u\'')
            print('To delete a record, enter \t\t\'d\'')
            print('To see tables in the database, enter \t\'w\'')
            print('To see this message again, enter \t\'h\'')
            print('To quit, enter \'q\'')
        
        choice = input("Enter your choice: ")
        
        #Create record module
        if choice == 'c':
            a1 = ""
            a2 = ""
            a3 = ""
            a4 = ""
            
            q_table =   input("Enter the name of table you which to make a record for: ")

            sql = "INSERT INTO " + q_table

            tablechosen = True

            #Hard-coded creation tables per each table in our project
            if q_table == "GENRE":
                a1 = input("Enter the name of genre for the record: ")
                sql += " (id, Genre) VALUES (NULL, \"" + MySQLdb.escapestring(a1) + "\");"

            elif q_table == "TYPE_OF":
                a1 = input("Enter id of the movie: ")
                a2 = input("Enter id of the genre: ")
                sql += " (Movieid, Genreid) VALUES (\"" + MySQLdb.escapestring(a1) + "\", \"" + MySQLdb.escapestring(a2) + "\");"

            elif q_table == "MOVIE":
                a1 = input("Enter name of the movie: ")
                a2 = input("Enter release year of the movie: ")
                a3 = input("Enter runtime (in minutes) of the movie: ")
                a4 = input("Enter description of the movie: ")
                sql += " (id, Name, YearRelease, Runtime, Description) VALUES (NULL, \"" + MySQLdb.escapestring(a1) + "\", \"" + MySQLdb.escapestring(a2) + "\", \""+ MySQLdb.escapestring(a3) + "\", \"" + MySQLdb.escapestring(a4) + "\");"

            else:
                print("Please enter a table in the databse.")
                tablechosen = False

            if tablechosen:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                        connection.commit()

                except pymysql.ProgrammingError as e:
                    print ("SQL Error Caught",e)
                    
                else:
                    print("Records created.")
            
        
        #Record read module
        elif choice == 'r':
            
            sql = ''
            
            #Join flag: only two joins are possible for the tables we used in our project
            joinflag = input("Read from two tables? (y/n): ")
            
            #Join the tables
            if joinflag == 'y':
                table1 = MySQLdb.escapestring(input("Enter the name of the first table you which to access: "))
                t1att =  input("Enter attributes you wish to see, seperated by commas: ")
                
                table2 = MySQLdb.escapestring(input("Enter the name of the second table you which to access: "))
                t2att =  input("Enter attributes you wish to see, seperated by commas: ")
                
                q_cond =    input("Enter conditions on search, seperated by commas (\'none\' for no conditions): ")
                
                q_lim =     input("Enter number of records you wish to see (\'*\' for all records): ")
                
                sql += "SELECT " + t1att + ", " + t2att + " FROM " + table1 + " JOIN TYPE_OF as typeof ON "
                
                if table1 == 'MOVIE':
                    sql += "typeof.Movieid = MOVIE.id JOIN " + table2 + " ON GENRE.id = typeof.Genreid"
                
                else:
                    sql += "typeof.Genreid = GENRE.id JOIN " + table2 + " ON MOVIE.id = typeof.Movieid"
            
            #Only read form one table
            elif joinflag == 'n':   
                q_table =   MySQLdb.escapestring(input("Enter the name of the table you which to access: "))
                q_att =     MySQLdb.escapestring(input("Enter attributes you wish to see, seperated by commas (enter \'*\' for all attributes in table): "))
                q_cond =    input("Enter conditions on search, seperated by commas (\'none\' for no conditions): ")
                q_lim =     input("Enter number of records you wish to see (\'*\' for all records): ")
                
                sql += "SELECT " + q_att + " FROM " + q_table
            
            #User did not answer the question
            else:
                print("Please enter y/n.")
                    
            #Apply multiple conditions
            if q_cond != 'none':
                sql += " WHERE "
                condlist = q_cond.split(",")
                for i in range(0, len(condlist)):
                    if i == len(condlist)-1:
                        sql += condlist[i] + ";"
                        
                    else:
                        sql += condlist[i] + " AND "
            
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    
                    if q_lim == '*':
                        result = cursor.fetchall()
                        
                    else:
                        result = cursor.fetchmany(int(q_lim))
                        
                    print(result)
                
            except pymysql.ProgrammingError as e:
                print ("SQL Error Caught",e)
                    
            else:
                print("Records obtained.")
    
        #Update record module
        elif choice == 'u':
            q_table = MySQLdb.escapestring(input("Enter the name of the table you wish to update records for: "))
            
            q_attstr = input("Enter attributes you wish update, seperated by commas: ")

            q_att = q_attstr.split(',')

            q_updstr = input("Enter the updated values corresponding the desired attributes, seperated by commas: ")

            q_upd = q_updstr.split(',')

            q_cond = input("Enter conditions on update, seperated by commas: ")

            sql = "UPDATE " + q_table + " SET "

            #Build SQL string update clause from user input
            for i in range(0,len(q_att)):
                if i != len(q_att)-1:
                    sql += q_att[i] + " = \"" + q_upd[i] + "\", "
                else:
                    sql += q_att[i] + " = \"" + q_upd[i] + "\" "
            
            #Apply multiple conditions
            sql += " WHERE "
            condlist = q_cond.split(",")
            for i in range(0, len(condlist)):
                if i == len(condlist)-1:
                    sql += condlist[i] + ";"
                    
                else:
                    sql += condlist[i] + " AND "

            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)

                    connection.commit()

            except pymysql.ProgrammingError as e:
                print ("SQL Error Caught",e)
                    
            else:
                print("Records updated.")
                
        #Delete record module
        elif choice == 'd':
            sql = "DELETE FROM "
            
            q_table = MySQLdb.escapestring(input("Enter the name of the table you which to delete a record from: "))
            
            sql += q_table + " WHERE "

            #Ask user for each conditions needed to delete
            finished = ""
            while finished != "y":
                q_att = MySQLdb.escapestring(input("Enter attribute for condition: "))
                sql += q_att + " = "
                
                q_att = MySQLdb.escapestring(input("Enter value for attribute condition: "))
                sql += q_att
                
                finished = input("No more conditions? (y/n): ")

                if finished == 'n':
                    sql += " AND "

            sql += ";"
            
            print(sql)

            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)

                    connection.commit()
            
            except pymysql.ProgrammingError as e:
                print ("SQL Error Caught",e)
            
            else:
                print("Record deleted.")
            
        #Module for helping user navigate the database
        elif choice == 'w':
            print("Presenting tables and their attributes.")
            print(  " GENRE                                                     \n",
                    "+----+-------+                                             \n",
                    "| id | Genre |                                             \n",
                    "+----+-------+                                             \n",
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
        
        #Module for quitting program
        elif choice == 'q':
            print("Quitting program.")   
            
        #Module requesting user for valid input
        else:
            print("Enter \'h\' for help.")
    
    #Close connection to database
    print("Connection will be closed.")
    connection.close()
                
main()