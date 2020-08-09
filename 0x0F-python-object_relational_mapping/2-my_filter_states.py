#!/usr/bin/python3
""" list where start letter is 'N' """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=my_user,
        passwd=my_pass,
        db=my_db)

    cursor = db.cursor()
    dbase = cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%' ORDER BY states.id".format(argv[4]))
    res = cursor.fetchall()
    for i in res:
        print(i)
    cursor.close()
    db.close()
