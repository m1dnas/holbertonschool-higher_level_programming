#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
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
    cur.execute("SELECT * FROM states ORDER BY id")
    row = cur.fetchall()

    for rows in row:
        if rows[1][0] == "N":
            print(rows)

    db.close()
