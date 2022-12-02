import sqlite3
Bookstore=sqlite3.connect('bookstore.db')
curbook=Bookstore.cursor()
curbook.execute("CREATE TABLE books (BookID INTEGER PRIMARY KEY AUTOINCREMENT, Book_Name TEXT, Author TEXT, Price TEXT);")
curbook.execute("INSERT INTO books VALUES (1,'Mrutunjay','Shivaji Sawant',450);")
curbook.execute("INSERT INTO books VALUES (2,'Karney','Shivaji Sawant',450);")
curbook.execute("INSERT INTO books VALUES (3,'Atomic Habits','James Clear',250);")
curbook.execute("INSERT INTO books VALUES (4,'Rich Dad Poor dad','Robert Kiyosaki',175);")
curbook.execute("INSERT INTO books VALUES (5,'Think Python','Allen B Drowney',475);")
curbook.execute("INSERT INTO books VALUES (6,'Chava','Shivaji Sawant',400);")


while True:
    mybooktitle=input("Book Title: ")
    sql="SELECT * FROM books where Book_name='"+mybooktitle+"';"
    curbook.execute(sql)
    record=curbook.fetchone()
    print(record)
    Total_cost=0
    n=int(input('No. of Copies:'))
    Total_cost=Total_cost + int(int(record[3])*n)
    morebooks=input("Add more books?Y/N")
    if morebooks=='N':
        break
print('Total Cost {}'.format(Total_cost))
mycopies=input("enter to exit")
Bookstore.close()



