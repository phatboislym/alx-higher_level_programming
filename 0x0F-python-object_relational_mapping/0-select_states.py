#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """
    lists all states from the database hbtn_0e_0_usa
    in ascending order by states.id
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall()]
