import mysql.connector as sql

user=[]
def valid_mail(mailid):
    if mailid.endswith('.com') and (mailid.index('@'))!=0:
        return True
    else:
        return False

def chk(pwd, mailid):
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

    
    

def menu_emp():
    print('''\n1.view applicants
    2.view and mangae your listed jobs. 
    3.view and edit your information
    4.log out\n''')
    c3 = int(input('\nEnter Your Choice\n'))
    mydb = sql.connect(host='localhost', user='root', password='root', database='portal')
    cursor = mydb.cursor()

    if c3 == 1:
        # Code to view applicants for listed jobs
        job_id = int(input('Back[0] or Enter the Job ID to view applicants: '))
        cursor.execute('SELECT * FROM applicants1 where job_id=%s;',[job_id])
        r=cursor.fetchall()
        c=1
        if job_id==0:
            menu_emp()
        else:
            for i in r:
                print('\n{}:{}'.format(c,i))
                c+=1
            else:
                print('\nNo more applicants for this job. \nPress [0] for menu OR [Applicant_ID] to remove applicant')
                c31=int(input('choice:'))
                if c31==0:
                    
                    menu_emp()
                else:
                    for i in r:
                        if c31==i[0]:
                            cursor.execute('delete from applicants11 where applicant_id=%s',[c31])
                            print('deleted successfully')
                            menu_emp()
                    

    elif c3 == 2:
        # Code to view and manage listed jobs
        cursor.execute('SELECT * FROM emp_job_listed1;')
        r= cursor.fetchall()
        for i in r:
            print('\nJob ID: {}, Company: {}, Job Type: {}, Salary: {}'.format(i[0], i[1], i[4], i[8]))
        
        while True:
            job_id = int(input('\nEnter the Job ID to manage or 0 to go back: '))
            if job_id == 0:
                menu_emp()
            else:
                for i in r:
                    if job_id==i[0]:
                        print(''' 1.Company
    2.Location
    3.industry
    4.job_type
    5.Job-Description
    6.Requirements
    7.Application deadline date
    8.Salary
    9.Email-ID
    10.Job Posted on''')
                        c21=int(input('Enter your choice or Back(0)'))
                        if c21==0:
                              menu_emp()
                        elif c21==1:
                            company=input('\nNew Company Name')
                            cursor.execute("UPDATE emp_job_listed1 SET company_name = %s WHERE job_id = %s;", (company, job_id))
                            cursor.execute("UPDATE job_listed1 SET company_name = %s WHERE job_id = %s;", (company, job_id))
                            print('\n...Updated...\n')
                            
                        elif c21==2:
                            location=input('\nLocation')
                            cursor.execute("UPDATE emp_job_listed1 SET location = %s WHERE job_id = %s;", (location, job_id))
                            cursor.execute("UPDATE job_listed1 SET location = %s WHERE job_id = %s;", (location, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==3:
                            ind=input('Industry')
                            cursor.execute("UPDATE emp_job_listed1 SET industry = %s WHERE job_id = %s;", (ind, job_id))
                            cursor.execute("UPDATE job_listed1 SET industry = %s WHERE job_id = %s;", (ind, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==4:
                            job_type=input('JOb-Type')
                            cursor.execute("UPDATE emp_job_listed1 SET job_type = %s WHERE job_id = %s;", (job_type, job_id))
                            cursor.execute("UPDATE job_listed1 SET job_type = %s WHERE job_id = %s;", (job_type, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==5:
                            desc=input('job_desccription')
                            cursor.execute("UPDATE emp_job_listed1 SET job_desc = %s WHERE job_id = %s;", (desc, job_id))
                            cursor.execute("UPDATE job_listed1 SET job_desc = %s WHERE job_id = %s;", (desc, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==6:
                            req=input('Requirements')
                            cursor.execute("UPDATE emp_job_listed1 SET req = %s WHERE job_id = %s;", (req, job_id))
                            cursor.execute("UPDATE job_listed1 SET req = %s WHERE job_id = %s;", (req, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==7:
                            app_dead=input('Application Deadline')
                            cursor.execute("UPDATE emp_job_listed1 SET app_deadline = %s WHERE job_id = %s;", (app_dead, job_id))
                            cursor.execute("UPDATE job_listed1 SET app_deadline = %s WHERE job_id = %s;", (app_dead, job_id))
                            
                            mydb.commit()
                            print('\n...updated successfully...\n')
                        elif c21==8:
                            salary=input('salary')
                            cursor.execute("UPDATE emp_job_listed1 SET salary = %s WHERE job_id = %s;", (salary, job_id))
                            cursor.execute("UPDATE job_listed1 SET salary = %s WHERE job_id = %s;", (salary, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==9:
                            mail=input('Contact Email_ID')
                            cursor.execute("UPDATE emp_job_listed1 SET mail = %s WHERE job_id = %s;", (mail, job_id))
                            cursor.execute("UPDATE job_listed1 SET mail = %s WHERE job_id = %s;", (mail, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c21==10:
                            job_post_on=input('JOb posted Date')
                            cursor.execute("UPDATE emp_job_listed1 SET created_on = %s WHERE job_id = %s;", (job_post_on, job_id))
                            cursor.execute("UPDATE job_listed1 SET created_on = %s WHERE job_id = %s;", (job_post_on, job_id))
                            print('\n...Updated...\n')
                            mydb.commit()
                              
                        


            
            
    elif c3 == 3:
        # Code to view and edit employee information
        cursor.execute("SELECT * FROM employee;")
        r = cursor.fetchall()
        pwd=input('enter your password')
        for i in r:
            if pwd==i[3] and user[0][2]==i[2]:
                print("{}:{}".format('1.Company_ID',i[0]),'\n{}:{}'.format('2.name',i[1]),'\n{}:{}'.format('3.Email-ID',i[2]),'\n{}:{}'.format('4.password',i[3]),'\n{}:{}'.format('5.Position',i[4]))
        # Display employee information

                c21=int(input('\nedit(2-5) or Back(0)\n'))
                if c21==0:
                    menu_emp()
                elif c21==2:
                    name=input('\nNew Name')
                    cursor.execute("UPDATE employee SET name = %s WHERE company_id = %s", (name, i[0]))
                    print('\n...Updated...\n')
                    mydb.commit()
                    menu_emp()
                elif c21==3:
                    mail=input('New Email-ID')
                    cursor.execute("UPDATE employee SET email = %s WHERE company_id = %s", (mail, i[0]))
                    print('\n...Updated...\n')
                    mydb.commit()
                    menu_emp()
                elif c21==4:
                    pwd=input('New password')
                    cursor.execute("UPDATE employee SET password = %s WHERE company_id = %s", (pwd, i[0]))
                    print('\n...Updated...\n')
                    mydb.commit()
                    menu_emp()
                elif c21==5:
                    pos=input('Position')
                    cursor.execute("UPDATE employee SET position = %s WHERE company_id = %s", (pos, i[0]))
                    print('\n...Updated...\n')
                    mydb.commit()
                    menu_emp()
                else:
                    print('invalid choice')
                    menu_emp()
        

    elif c3 == 4:
        user.pop()
        login()
def menu_seek():
    print('''\n    1.browse for jobs
    2.View and edit applied jobs
    3.view and edit your info
    4.log out\n''')
    c2=int(input('\nEnter Your Choice\n'))
    mydb=sql.connect(host='localhost',user='root',password='root',database='portal')
    cursor=mydb.cursor()
    loop=True
    if c2==1:
        q='select * from job_listed1;'
        cursor.execute(q)
        r=cursor.fetchall()
        
        for i in r:
            
            print('\n....type job id for more info....\n')
            print("{}:{}".format('job_id',i[0]),'\n{}:{}'.format('company_name',i[1]),'\n{}:{}'.format('job type',i[4]),'\n{}:{}'.format('job',i[5]),'\n{}:{}'.format('job type',i[4]),'\n{}:{}'.format('Salary',i[8]))
        print('\nback(0)\n')
        
        while True:
            c21=int(input('\nEnter Job_ID for more Information  \nback(0)\n'))
            
            if c21==0:
                    
                menu_seek()
            else:
                
                for i in r:
                    if i[0]==c21:
                
                
                        print(i)
                        c22=int(input('\napply(1) \nback(0)\n'))
                        if c22==1:
                            cursor.execute('insert into applied_job1 values(%s,%s);',(c21,i[5]))
                            cursor.execute('select * from emp_job_listed1;')
                            mydb.commit
                            j=cursor.fetchall()
                            for p in j:
                                if p[0]==i[0]:
                                    #user.append(c21)
                                    print(user)
                                    cursor.execute('insert into applicants1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',user[0]+(c21,))
                                    #user.pop()
                                    print('\n...applied\n...')
                                    mydb.commit()
                            
                        elif c22==0:
                            pass
                        else:
                            print('\n...invalid choice...\n')
                    else:
                        pass        
            
    elif c2==2:
        c=1
        q="select * from applied_job1"
        cursor.execute(q)
        r=cursor.fetchall()
        for i in r:
            print("{}:{}".format(c,i),end='\n')
            c+=1
        while True:

            c21=int(input('\nwithdraw from job(JOB ID) or Back(0)\n'))
            if c21==0:
                menu_seek()

            else:

                for i in r:

                    if c21==i[0]:
                        cursor.execute('delete from applied_job1 where job_id=%s;',[c21])
                        mydb.commit()
                        print('\n...opted out job successfully deleted...\n')
                        cursor.execute('select * from emp_job_listed1;')
                        j=cursor.fetchall()
                        for p in j:
                                if p[0]==i[0]:
                                    cursor.execute('delete from applicants1 where applicant_id=%s',(user[0][0],))
                                    mydb.commit()
                    else:
                        True
                



                    
    elif c2==3:
        cursor.execute("select * from seeker")
        r=cursor.fetchall()
        c21=input('\nenter your password or back(0)\n')
        flg1=True
        if flg1==True:

            for i in r:
                if c21==i[3]:
                    print("{}:{}".format('1.your id',i[0]),'\n{}:{}'.format('2.name',i[1]),'\n{}:{}'.format('3.Email-ID',i[2]),'\n{}:{}'.format('4.password',i[3]),'\n{}:{}'.format('5.resume link',i[4]),'\n{}:{}'.format('6.skill',i[5]),'\n{}:{}'.format('7.years of experience',i[6]),'\n{}:{}'.format('8.educational background',i[7]))
                
                    while True:
                        c22=int(input('\n....edit(2-8) or back(0)....\n'))
                        if c22==0:
                            menu_seek()
                        elif c22==2:
                            name=input('\nNew Name')
                            cursor.execute("UPDATE seeker SET name = %s WHERE seeker_id = %s", (name, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c22==3:
                            mail=input('New Email-ID')
                            cursor.execute("UPDATE seeker SET email = %s WHERE seeker_id = %s", (mail, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c22==4:
                            pwd=input('New password')
                            cursor.execute("UPDATE seeker SET password = %s WHERE seeker_id = %s", (pwd, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c22==5:
                            link=input('New resume link')
                            cursor.execute("UPDATE seeker SET resume_link = %s WHERE seeker_id = %s", (link, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c22==6:
                            skill=input('New skill')
                            cursor.execute("UPDATE seeker SET skill = %s WHERE seeker_id = %s", (skill, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        elif c22==7:
                            exp=input('updated experience')
                            cursor.execute("UPDATE seeker SET experience_yrs = %s WHERE seeker_id = %s", (exp, i[0]))
                            
                            mydb.commit()
                            print('\n...updated successfully...\n')
                        elif c22==8:
                            bg=input('updated background')
                            cursor.execute("UPDATE seeker SET educational_background = %s WHERE seeker_id = %s", (bg, i[0]))
                            print('\n...Updated...\n')
                            mydb.commit()
                        else:
                            print('\n...invalid choice...\n')
                elif c21==0:
                    menu_seek()
                else:
                    flg1=False
                
    
                
        elif flg1==False:
            print('\nWrong Password\n')
            menu_seek()
    
    elif c2==4:
        user.pop()
        login()
    mydb.close()
    
def login():

    while True:
        
        print('''TO Proceed
        1.Login
        2.Sign Up
        3.quit''')
        c1=int(input('Enter your choice'))
        if c1==1:
            print('enter your E-mail ID and Password')
        
            mailid=input('email:-')

            if valid_mail(mailid)==True:#checks whether the mailid is correct or not

                pwd=input('password')

                user_type=chk(pwd,mailid)

                if user_type=='employee':#checks whether the user exists or not
                
                    menu_emp()#for displaying menu to the employee
                    break
                elif user_type=='seeker':
                
                    menu_seek()
                    break
                else:
                    print("\nWrong email or password \n\nIf You don't Have an account does not exist sign up first'",end='\n')
                    
            else:
                print('Invalid Email ID. \nTRY AGAIN')
                
        elif c1==2:
            print('''\nAre you a Recruiter or Job Seeker.
1.Recruiter
2.Job Seeker''')
            c12=int(input())
            if c12==1:
                
                name=input('enter your name')
                email=input('enter email id')
                pwd=input('create password')
                position=input("what's your position")

                mydb=sql.connect(host='localhost',user='root',password='root',database='portal')
                cursor=mydb.cursor()
                q="insert into employee(name,email,password,position) values(%s,%s,%s,%s);"
                cursor.execute(q,(name,email,pwd,position))
                print('....successfully signed up....\n')
                r=cursor.fetchall()
                for i in r:
                    if i[2]==email:
                        print("your id is:-",i[0])
                mydb.commit()
                mydb.close
            elif c12==2:
                #id=input('enter id')
                name=input('enter your name:')
                email=input('enter email id:')
                pwd=input('create password:')
                link=input("PROVIDE RESUME LINK:")
                skill=input('Enter Your Skills:')
                experience=input('Years of Experience:')
                bg=input('courses done:')

                mydb=sql.connect(host='localhost',user='root',password='root',database='portal')
                cursor=mydb.cursor()
                q="insert into seeker(name,email,password,resume_link,skill,experience_yrs,educational_background) values(%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(q,(name,email,pwd,link,skill,experience,bg))
                print('....successfully signed up....')
                mydb.commit()
                mydb.close
        
        elif c1==3:
            print('exiting...')
            break

        else:
            print('invalid choice')
            
        
                
login()
