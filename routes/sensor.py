from fastapi import APIRouter
import mysql.connector
from db import db
import datetime

mydb = mysql.connector.connect(
    host = db.mydb2().host,
    port = db.mydb2().port,
    user = db.mydb2().username,
    password = db.mydb2().password,
    database = db.mydb2().database
)

if mydb.is_connected():
    print('db connected')

router = APIRouter(
    prefix='/add',
    tags = ['addition']
)

@router.post('/send_data')
def send_data():
    date = datetime.datetime.now()
    cursor = mydb.cursor()
    sql = "INSERT INTO dht11 (timestamp, loc, hum, temp) VALUES (%s, %s, %s, %s)"
    val = (str(date),'1','2','3')

    cursor.execute(sql, val)

    mydb.commit()
    return{
        "got it testing"
    }