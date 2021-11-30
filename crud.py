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
    
        if choice == 'h':
            print('To create a table or record, enter \t\t\'c\'')
            print('To read a table or record, enter \t\t\'r\'')
            print('To update a table or record, enter \t\t\'u\'')
            print('To delete create a table or record, enter \t\'d\'')
            print('For help, enter \'h\'')
            print('To quit, enter \'q\'')
        
        choice = input("Enter your choice: ")
        
        if choice == 'r':
            
            q_att = input("Enter attributes you wish to see: ")
            
            try:

                with connection.cursor() as cursor:
                    # Reading records record
                    sql = "SELECT name FROM cityByCountry WHERE country=%s"
                    cursor.execute(sql, [226])
                    result = cursor.fetchmany(size=10)
                    print(result)
                    
            finally:
                connection.close()

main()