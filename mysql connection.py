# import the data base

import MySQLdb

con = MySQLdb.connect(host='localhost', user = 'root', passwd = 'ganesh123456', port = 3306, db = 'school')

print(con)

cur = con.cursor()

#cur.execute("create table student (studentid int, studentname char(20),studentfee int)")
#cur.execute("insert into student values(1,'rama',5000)")
#cur.execute("insert into student values(2,'ravi',6000)")
#cur.execute("insert into student values(3,'ramakrishna',7000)")
#cur.execute("insert into student values(4,'ramaiah',8000)")
#cur.execute("insert into student values(5,'ramesh',9000)")
#cur.execute("insert into student values(6,'ravikuamr',10000)")
#cur.execute("insert into student values(7,'anil',12000)")
#cur.execute("delete from student where studentid=6")
cur.execute("update student set studentid=7,studentname='hello'where studentfee=9000 ")

cur.close()

con.commit()
con.close()
