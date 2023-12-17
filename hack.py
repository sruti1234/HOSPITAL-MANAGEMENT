import mysql.connector as db
#Hospital management software
pid=0
print("""
      ===========================================
           welcome to Lifeline Hospital
      ===========================================
""")
#Establishing connection and creating database along with required tables

#pd=str(input("enter database password:"))

cn=db.connect(host="localhost",user="root",password="chandu538")
print(cn)
cur=cn.cursor()
#creating database for hospital
cur.execute("create database if not exists lifeline_hospital")
cur.execute("use Lifeline_hospital")
cur.execute("create table if not exists patients\
                 (pid int,\
                 Name varchar(30),\
                 mobile varchar(10),\
                 age int,\
                 city varchar(50),\
                 blood_group varchar(20),\
                 doc_rec varchar(30))")
cur.execute("create table if not exists doctors\
            (name varchar(30) primary key,\
            age int,\
            city varchar(30),\
            mobile varchar(10),\
            salary int)")
cur.execute("create table if not exists lab_reports\
            (test varchar(35),\
            status varchar(40),\
            result varchar(35),\
            conclusion varchar(35),\
            reference varchar(100))")
cur.execute("create table if not exists nurses\
            (Name varchar(30) primary key,\
            age int,\
            city varchar(30),\
            mobile varchar(10),\
            salary int)")
cur.execute("create table if not exists workers\
            (Name varchar(30) primary key,\
            age int,\
            city varchar(30),\
            mobile varchar(10),\
            salary int)")
#login or signup options for users
#creating table for storing the username and password of the user
cur.execute("create table if not exists users\
              (username varchar(30) primary key,\
               password varchar(30))")

def sign_up():
    print("""
        ==========================================================
              !!!!!!! Please Enter new user details !!!!!!!!
        ==========================================================
          """)
    u=input("Enter New User Name:")
    p=input("Enter password:")
    #ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
    cur.execute("insert into users values('"+u+"','"+p+"')")
    cn.commit()
    print("""
          ============================================================
               !!!!!congratulations!!!!!, New User Created...!!!
          ============================================================
          """)

def login():
    #login with username and password

            print("""
                  ====================================================
                    !!!!! (Loginwith username and password) !!!!!
                  ====================================================
                  """)
            un=input("Username:")
            ps=input("Password:")
            pid=0
            cur.execute("select password from users where username='"+un+"'")
            rec=cur.fetchall()
            for i in rec:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        #Menu for administrative tasks
                        print("""
                              1. Admin Tasks
                              2. Patient (Admit and Discharge)
                              3. Lab Reports
                              4. Sign Out
                              """)
                        #Promt message for task from user
                        a=int(input("Enter your choice:"))
                        #Admin tasks
                        if a==1:
                            print("""
                                  1. Show Details
                                  2. Add new member
                                  3. Delete existing member
                                  4. Exit
                                  """)
                            b=int(input("Enter your choice:"))
                            #Showing details of doctors, nurses and workers
                            if b==1:
                                print("""
                                      1. Doctors
                                      2. Nurses
                                      3. Workers
                                      """)
                                
                                #Prompt message for user to show details
                                c=int(input("Enter your choice:"))
                                #see the details of doctors
                                if c==1:
                                    cur.execute("select * from doctors")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        b=0
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                #see the details of nurse
                                elif c==2:
                                    cur.execute("select * from nurses")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                #see the details of workers
                                elif c==3:
                                    cur.execute("select * from workers")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                        
                                        
                            #Add new member into hospital team
                            elif b==2:
                                print("""
                                     1. Doctor
                                     2. Nurses
                                     3. Worker
                                     """)
                                c=int(input("Enter your choice"))

                                #New doctor details
                                if c==1:
                                    #prompt messages for doctor details
                                    name=input("Enter name of the doctor")
                                    age=input("Enter age")
                                    city=input("Enter city doctor belongs to")
                                    mno=input("Enter mobile number")
                                    sal=input("Enter salary of doctor")
                                    spe=input("Enter specialization")
                                    #Insert values into doctor table
                                    cur.execute("insert into doctors values('"+name+"','"+age+"','"+city+"','"+mno+"','"+sal+"','"+spe+"')")
                                    cn.commit()
                                    print("New doctor details has been added sucessfull")
                                #New nurse details
                                elif c==2:
                                      #prompt message for nurse details
                                      name=input("Enter name of the nurse")
                                      age=input("Enter age")
                                      city=input("Enter city nurse belongs to")
                                      mno=input("Enter mobile no")
                                      sal=input("Enter salary")
                                      #Insert value into nurses table
                                      cur.execute("insert into nurses values('"+name+"','"+age+"','"+city+"','"+mno+"','"+sal+"')")
                                      cn.commit()
                                      print("New nurse details has been added sucessfully.")
                             #New worker details
                                elif c==3:
                                     #prompt message for worker details 
                                      name=input("Enter name of worker")
                                      age=input("Enter age")
                                      city=input("Enter city")
                                      mno=input("Enter mobile no")
                                      sal=input("Enter salary")
                                     #Insert worker details into doctors table
                                      cur.execute("insert into workers values('"+name+"','"+age+"','"+city+"','"+mno+"','"+sal+"')")
                                      cn.commit()
                                      print("SUCESSFULLY ADDED")
                                    #menu for delete data
                            elif b==3:
                                print("""
                                              1. Doctors
                                              2. Nurses
                                              3. Workers
                                              """)
                                c=int(input("Enter your choice"))
                                        #deleting doctors details
                                if c==1:
                                    name=input("Enter doctor name to delete")
                                    cur.execute("select * from doctors where name='"+name+"'")
                                    rec=cur.fetchall()
                                    print(rec)
                                    p=input("You really wanna delete this data? (y/n)")
                                    if p=="y":
                                        cur.execute("delete from doctors where name='"+name+"'")
                                        cn.commit()
                                        print("Doctor has been deleted succesfully")
                                    else:
                                        print("Error in deletion ....")

                                        #deleting nurse details
                                elif c==2:
                                    name=input("Enter name of nurse")
                                    cur.execute("select * from nurses where name='"+name+"'")
                                    rec=cur.fetchall()
                                    print(rec)
                                    p=input("Are you really wanna delete this data? (y/n)")
                                    if p=="y":
                                        cur.execute("delete from nurses where name='"+name+"'")
                                        cn.commit()
                                        print("Nurse has been deleted sucessfully.")
                                    else:
                                        print("Error in deletion")
                                        #deleting worker details
                                elif c==3:
                                    name=input("Enter name of worker")
                                    cur.execute("select * from workers where name='"+name+"'")
                                    rec=cur.fetchall()
                                    print(rec)
                                    p=input("Are you really wanna delete this data? (y/n)")
                                    if p=="y":
                                        cur.execute("delete from workers where name='"+name+"'")
                                        cn.commit()
                                        print("Worker has been deleted")
                                    else:
                                        print("Error in deletion.")
                            
                            elif b==4:
                                print("Thank you! See you again! Have a nice day!")
                                break
                                       #entering the patient details table
                        elif a==2:

                            print("""
                                                  1. Show patient record
                                                  2. Admit new patient
                                                  3. Discharge patient
                                                  4. Exit
                                                  """)
                            b=int(input("ENTER YOUR CHOICE"))
                                           #showing the existing details of patients
                                           #see the details of patient
                            if b==1:
                                cur.execute("select * from patients")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                v=list(i)
                                k=["PID","NAME","MOBILE NO","AGE","CITY","BLOOD GROUP","DOCTOR RECOM"]
                                d=dict(zip(k,v))
                                for i in d:
                                    print(i,";",d[i])
                                            #Admit a new patient
                            elif b==2:
                                pid=str(input("Enter pid"))
                                name=str(input("Enter name of patient"))
                                mno=str(input("Enter mobile no"))
                                age=str(input("Enter age"))
                                mn=str(input("Enter city"))
                                bg=str(input("Enter blood group"))
                                cur.execute("select name,mobile,specialization from doctors")
                                rec=cur.fetchall()
                                print(rec)
                                dr=str(input("Enter doctor recommended"))
                                cur.execute("insert into patients values('"+str(pid)+"','"+str(name)+"','"+str(mno)+"','"+str(age)+"','"+str(mn)+"','"+str(bg)+"','"+str(dr)+"')")
                                cn.commit()            

                                print("""
                                                    ====================================
                                                       !!!!!!!New patient admitted!!!!!!
                                                    ====================================
                                                           """)
                                           #dischare a patient
                            elif b==3:
                                name=input("Enter the name of patient to discharge")
                                cur.execute("select * from patients where name='"+name+"'")
                                rec=cur.fetchall()
                                print(rec)
                                bill=input("Bill payemt (y/n)")
                                if bill=="y":
                                    cur.execute("delete from patients where name like'%"+name+"%'")
                                    cn.commit()
                                elif bill=="n":
                                    print("Please pay your pending bill amount to discahrge patient.")
                                else:
                                    print("Bill payment status is unknown....")
                                          #if user wants to exit
                            elif b==4:
                                break
                                      ###SIGN OUT
                        elif a==3:
                            print("""
                                    1.show reports
                                    2.Add Reports
                                    3.Exit
                                  """)
                            b=int(input("ENTER YOUR CHOICE"))
                            if b==1:
                                cur.execute("select * from lab_reports")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                v=list(i)
                                k=["test","status","result","conclusion","reference"]
                                d=dict(zip(k,v))
                                for i in d:
                                    print(i,";",d[i])
                            elif b==2:
                                tes=str(input("Enter test "))
                                sta=str(input("Enter status "))
                                res=str(input("Enter result "))
                                con=str(input("Enter conclusion "))
                                ref=str(input("Enter reference "))
                                cur.execute("insert into lab_reports values('"+str(tes)+"','"+str(sta)+"','"+str(res)+"','"+str(con)+"','"+str(ref)+"')") 
                                cn.commit()            

                                print("""
                                                    ====================================
                                                       !!!!!!!New reports added!!!!!!
                                                    ====================================
                                                           """)                       
                            elif b==3:
                               break
def change_pass():
    cur.execute("select username from users")
    rec=cur.fetchall()
    for i in rec:
        v=list(i)
        k=["USERNAME"]
        d=dict(zip(k,v))
    print(d)
    u=input("Enter username to change password from above")
    if u in d.values():
        pd=input("Enter New Password")
        pd1=input("Renter New Password again")
        if pd==pd1:
          cur.execute("update users set password='"+pd+"'where username='"+u+"'")
          cn.commit()
          print("Password Changed Successfully.")
        else:
          print("Password did not match...")
    else:
        print("Username not found")
            
#Main Menu
r=0
while r!=4:
    print("""
                    1. Sign Up (New User)
                    2. Log In
                    3. Change Password
                    4. Exit
                                                        """)

    r=int(input("Enter your choice"))    
    #New User Registration
    if r==1:
        sign_up()
    elif r==2:
        login()                 
    elif r==3:
        change_pass()
    elif r==4:
      print("Thank you for using Lifeline Hospital App, Have a nice day!")
      break
