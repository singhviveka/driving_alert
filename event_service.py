from datetime import datetime

import mysql.connector

from model import Event

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Singh@54321",
    database="mydb"
)

mycursor = mydb.cursor()

events = []


def addEvent(event: Event):
    events.append(event)
    count = 0
    for e in events:
        diff = datetime.now() - datetime.fromisoformat(e.timestamp)
        if (diff.total_seconds() / 60 <= 5) and (not e.is_driving_safe):
            count += 1
    if count >= 3:
        addAlert("unsafe")


def addAlert(message):
    query = "insert into alert(message) values ('%s')" % message
    mycursor.execute(query)


def getAlert(id):
    query = "select * from alert where id = " + str(id)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
