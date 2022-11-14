#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_usr = sys.argv[1]
    mysql_pswd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_usr,
            passwd=mysql_pswd,
            db=mysql_db)

    cur = db.cursor()
    cur.execute("SELECT * FROM states
                WHERE name LIKE %s
                ORDER BY id".format(sys.argv[4]))
    row = cur.fetchall()

    for rows in row:
        print(rows)

    db.close()
