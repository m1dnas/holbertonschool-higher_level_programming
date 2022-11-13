#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    # connect to a mysql database
    mysql_usr = sys.argv[1]
    mysql_pswd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_usr, passwd=mysql_pswd, db=mysql_db)

    # getting a cursor
    cur = db.cursor()

    # executing mysql queries
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)

    # obtain the data from the state table
    row = cur.fetchall()

    # print the rows
    for rows in row:
        print(rows)

    db.close()
