from pydantic import BaseModel


class Item_sensor(BaseModel):
    loc: int
    hum: int
    temp: int