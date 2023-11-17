from fastapi import APIRouter, Request, Form
import mysql.connector
from db import db
import datetime
from models import model
import json

mydb = mysql.connector.connect(
    host = db.mydb3().host,
    port = db.mydb3().port,
    user = db.mydb3().username,
    password = db.mydb3().password,
    database = db.mydb3().database
)

if mydb.is_connected():
    print('db connected')

router = APIRouter(
    prefix='/add',
    tags = ['addition']
)

@router.post('/send_data')
async def send_data(loc: str = Form(), hum: str = Form(), temp: str = Form()):

    date = datetime.datetime.now()
    cursor = mydb.cursor()
    sql = "INSERT INTO dht11 (timestamp, loc, hum, temp) VALUES (%s, %s, %s, %s)"
    val = (str(date),loc,hum,temp)

    cursor.execute(sql, val)

    mydb.commit()
    return (loc,hum,temp)

@router.get('/get_data')
def get_data():
    cursor = mydb.cursor()
    sql = "SELECT * FROM dht11"
    cursor.execute(sql)

    result = cursor.fetchmany(100)

    print(result)
    return result