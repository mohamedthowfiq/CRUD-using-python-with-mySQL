from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="7867",database="StudentDB")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users (name,age,city) values(%s,%s,%s)"
    users = (name,age,city)
    res.execute(sql,users)
    con.commit()
    print("data insert success")

def update(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s"
    users = (name,age,city,id)
    res.execute(sql,users)
    con.commit()
    print("data updated success")

def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("data deleted successfully")

def select():

    res = con.cursor()
    sql="Select ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
    con.commit()


while True:
    print("1 to insert data")
    print("2 to update data")
    print("3 to delete data")
    print("4 to select data")
    print("5 to exit")
    
    choice=int(input("Enter your choice : "))
    if choice==1:

        name=input("Enter the name")
        age=input("Enter the age")
        city=input("Enter the city")
        insert(name,age,city)

    elif choice==2:
        id=input("Enter the id :")
        name=input("Enter the name :")
        age=input("Enter the age :")
        city=input("Enter the city :")
        update(name,age,city,id)
    
    elif choice==3:
        id=input("Enter the id")
        delete(id)

    elif choice==4:
        select()

    elif choice==5:
        quit()

    else:
        print("Invalid Choice")