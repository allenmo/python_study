import MySQLdb

conn = MySQLdb.connect("192.168.1.77", "pyer", "abc-123", "testdb")
cur = conn.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print "Database version: %s" % data

cur.execute("DROP TABLE IF EXISTS testdb.EMPLOYEE")
sql1 = """CREATE TABLE EMPLOYEE (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20), 
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""
cur.execute(sql1)

sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME, 
    LAST_NAME, AGE, SEX, INCOME)
    VALUES('Mac', 'Mohan', 20, 'M', 2000),
          ('allen', 'mo', 32, 'M', 3000)"""
try:
    cur.execute(sql2)
    conn.commit()
except:
    conn.rollback()

sql3 = "SELECT * FROM EMPLOYEE \
        WHERE INCOME > '% d'" % (1000)
try:
    cur.execute(sql3)
    results = cur.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname= %s, lname=% s, age=% d, sex=% s, income=% d" % \
                (fname, lname, age, sex, income)
except:
    print "Error: unable to fetch data"


conn.close()

