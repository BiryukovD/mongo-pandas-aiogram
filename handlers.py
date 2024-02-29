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

    await msg.answer("Привет!")
