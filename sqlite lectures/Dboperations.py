import sqlite3 as sq

conn=sq.connect('mySqlite.db')

cur=conn.cursor()
#cur.execute('create table employee(fname varchar(50),email varchar(100))')

#cur.execute("insert into employee values('Zarna','z@gmail.com')")

#cur.execute("update employee set fname='Vibhuti',email='v@gmail.com' where fname='Rinkal'")

cur.execute("delete from employee where fname='Zarna'")
conn.commit()

print(list(cur.execute("select * from employee")))
conn.close()