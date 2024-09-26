import asyncio
from itertools import cycle

from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy import select, func

from bot.button.button import back_button
from db.models import session, User
from bot.hundlers.state import *

admin_router=Router()

@admin_router.callback_query(F.text == "back", AdminState.title)
@admin_router.message(F.text == "Qahram0n")
async def admin(message: Message, state: FSMContext):
    await message.answer("Reklama rasmini kiriting !", reply_markup=back_button())
    await state.set_state(AdminState.photo)


@admin_router.message(AdminState.photo, ~F.text, F.photo)
async def admin(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data({"photo": photo})
    await state.set_state(AdminState.title)
    await message.answer("Reklama haqida to'liq malumot bering !", reply_markup=back_button())


@admin_router.message(AdminState.title,~F.photo)
async def admin(message: Message, state: FSMContext):
    title = message.text
    await state.update_data({"title": title})
    tasks = []
    data = await state.get_data()
    await state.clear()
    counts = 0
    users = []
    cnt=0
    query_min = select(func.min(User.id))
    query_max = select(func.max(User.id))

    min_id = session.execute(query_min).scalars().first()
    max_id = session.execute(query_max).scalars().first()
    for i in range(min_id, max_id+1):

        query_user = select(User.user_id).where(User.id == i)
        user = session.execute(query_user).scalars().first()

        users.append(user)
        cnt+=1

    for i in cycle(users):
        a = message
        if counts == cnt:
            break
        if len(tasks) == 28:
            await asyncio.gather(*tasks)
            tasks = []
            try:
                 a = await message.bot.send_photo(chat_id=i, photo=data['photo'], caption=data['title'])
            except:
                pass
        tasks.append(a)
        counts += 1
    await message.answer("Reklama yuborildi !")

@admin_router.message(F.text!="Qahram0n")
async def not_message(message:Message):
    await message.delete()