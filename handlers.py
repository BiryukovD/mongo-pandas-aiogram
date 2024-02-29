from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import db
import json
import datetime
from functions import grouping

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!")


@router.message()
async def message_handler(msg: Message):
    input_data = json.loads(msg.text)
    dt_from = datetime.datetime.strptime(input_data['dt_from'], '%Y-%m-%dT%H:%M:%S')
    dt_upto = datetime.datetime.strptime(input_data['dt_upto'], '%Y-%m-%dT%H:%M:%S')
    col_filtered = db.test_col.find({"dt": {"$gte": dt_from, "$lte": dt_upto}}).sort('dt')
    result = await grouping(col_filtered, input_data['group_type'])
    json_str = json.dumps(result)
    await msg.answer(json_str)
