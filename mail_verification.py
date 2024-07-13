import mysql.connector as sql

def valid_mail(mailid):
    if mailid.endswith('.com') and (mailid.index('@'))!=0:
        return True
    else:
        return False
    
#################################

def chk(pwd, mailid,user):
    mydb = sql.connect(host='localhost', user='root', password='root', database='portal')
    cursor = mydb.cursor()
    
        # Check in the employee table
    q = 'select * from employee;'
    cursor.execute(q)
    r = cursor.fetchall()

    for i in r:
        if i[2] == mailid and i[3] == pwd:
            print('Welcome', i[1])
            user.append(i)
            
            return 'employee'

        # Check in the seeker table
    q = 'select * from seeker;'
    cursor.execute(q)
    r = cursor.fetchall()

    for i in r:
        if i[2] == mailid and i[3] == pwd:
            
            print('Welcome', i[1])
            user.append(i)
            print(user)
            return 'seeker'
        
###############################

