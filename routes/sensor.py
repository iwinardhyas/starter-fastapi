from fastapi import APIRouter, Request
import mysql.connector
from db import db
import datetime
from models import model
import json

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
async def send_data(item_sensor : model.Item_sensor):
    temp = item_sensor.temp
    hum = item_sensor.hum
    loc = item_sensor.loc
    date = datetime.datetime.now()
    cursor = mydb.cursor()
    sql = "INSERT INTO dht11 (timestamp, loc, hum, temp) VALUES (%s, %s, %s, %s)"
    val = (str(date),loc,hum,temp)

    cursor.execute(sql, val)

    mydb.commit()
    return item_sensor

@router.get('/get_data')
def get_data():
    cursor = mydb.cursor()
    sql = "SELECT * FROM dht11"
    cursor.execute(sql)

    result = cursor.fetchmany(100)

    print(result)
    return result