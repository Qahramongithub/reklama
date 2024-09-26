from aiogram import Router,F,html
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select,insert

from bot.button.button import promo_button, instagram_button
from bot.hundlers.state import ProStates, AdminState
from db.models import User, session

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    query=select(User).where(User.id==message.from_user.id)
    user=session.execute(query).scalars().first()
    if not user:
        new_user = insert(User).values(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )
        session.execute(new_user)
        session.commit()
    await message.answer(html.bold(f"<i>{message.from_user.full_name}</i>"),reply_markup=instagram_button())
    await message.answer_photo(photo="https://t.me/reklamakanaln1mln/2",
                               reply_markup=promo_button())
    await state.set_state(ProStates.menustate)
@start_router.callback_query(F.data=='back',AdminState.photo)
async def  start_handler(call:CallbackQuery,state:FSMContext):
    await call.message.answer_photo(photo="https://t.me/reklamakanaln1mln/2",
                               reply_markup=promo_button())
    await state.set_state(ProStates.menustate)