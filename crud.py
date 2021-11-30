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

def main():
    
    choice = 'h'
    
    print('Welcome to Group 7\'s Python SQL UI')
    
    while choice != 'q':
    
        #Query attributes one wishes to observe
        q_att = ''
    
        #Which table to obtain the results from
        q_table = ''
        
        #Conditions on read
        q_cond = ''
        
        #Limit on records
        q_lim = ''
    
        if choice == 'h':
            print('To create a table or record, enter \t\t\'c\'')
            print('To read a table or record, enter \t\t\'r\'')
            print('To update a table or record, enter \t\t\'u\'')
            print('To delete create a table or record, enter \t\'d\'')
            print('For help, enter \'h\'')
            print('To quit, enter \'q\'')
        
        choice = input("Enter your choice: ")
        
        if choice == 'r':
            
            #SELECT name FROM cityByCountry WHERE country=226
            q_table =   input("Enter the table you which to access: ")
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
                    
                    cursor.execute(sql, [])
                    
                    if q_lim == '*':
                        result = cursor.fetchall()
                        
                    else:
                        result = cursor.fetchmany(int(q_lim))
                        
                    print(result)
                    
            finally:
                print("Records obtained.")
    
    connection.close()
                

main()