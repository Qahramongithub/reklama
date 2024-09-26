from aiogram import Router,F,html
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaPhoto, InputMediaVideo
from sqlalchemy import select, func

from bot.button.button import menu_button, back_button
from bot.hundlers.state import ProStates
from db.models import Promo, session, My

menu_router=Router()
@menu_router.callback_query(ProStates.menustate,F.data=="promo")
async def menu_handlers(callback_query: CallbackQuery,state: FSMContext):
    query_min=select(func.min(Promo.id))
    min_id=session.execute(query_min).scalars().first()
    query_title=select(Promo.title).where(Promo.id==min_id)
    title=session.execute(query_title).scalars().first()
    query_dictionary=select(Promo.dictionary).where(Promo.id==min_id)
    dictionary=session.execute(query_dictionary).scalars().first()
    query_photo=select(Promo.photo).where(Promo.id==min_id)
    photo=session.execute(query_photo).scalars().first()
    caption=(f"{html.bold(f"<i>{title}</i>")}\n"
             f"{dictionary}\n")
    pege=min_id
    await state.update_data({"pege":pege})
    media=InputMediaPhoto(media=photo, caption=caption)
    await callback_query.message.edit_media(media=media,reply_markup=menu_button(pege))
    await state.set_state(ProStates.menustate)

@menu_router.callback_query(F.data.startswith('product_'))
async def product_menu(callback:CallbackQuery,state:FSMContext):
    pege=int(callback.data.split("_")[-1])
    print(pege)
    query_max=select(func.max(Promo.id))
    max_id=session.execute(query_max).scalars().first()
    query_min=select(func.min(Promo.id))
    min_id=session.execute(query_min).scalars().first()
    if pege<=max_id and pege>=min_id:
        query_title = select(Promo.title).where(Promo.id == pege)
        title = session.execute(query_title).scalars().first()
        query_dictionary = select(Promo.dictionary).where(Promo.id == pege)
        dictionary = session.execute(query_dictionary).scalars().first()
        query_photo = select(Promo.photo).where(Promo.id == pege)
        photo = session.execute(query_photo).scalars().first()
        caption = (f"{html.bold(f"<i>{title}</i>")}\n"
                   f"{dictionary}\n")
        await state.update_data({"pege": pege})
        photo = InputMediaPhoto(media=photo, caption=caption)
        await callback.message.edit_media(media=photo, reply_markup=menu_button(pege))
        await state.set_state(ProStates.promostate)
    elif pege<min_id:
        pege=max_id
        query_title = select(Promo.title).where(Promo.id == pege)
        title = session.execute(query_title).scalars().first()
        query_dictionary = select(Promo.dictionary).where(Promo.id == pege)
        dictionary = session.execute(query_dictionary).scalars().first()
        query_photo = select(Promo.photo).where(Promo.id == pege)
        photo = session.execute(query_photo).scalars().first()
        caption = (f"{html.bold(f"<i>{title}</i>")}\n"
                   f"{dictionary}\n")
        await state.update_data({"pege": pege})
        photo = InputMediaPhoto(media=photo, caption=caption)
        await callback.message.edit_media(media=photo, reply_markup=menu_button(pege))
        await state.set_state(ProStates.promostate)
    elif pege>max_id:
        pege=min_id
        query_title = select(Promo.title).where(Promo.id == pege)
        title = session.execute(query_title).scalars().first()
        query_dictionary = select(Promo.dictionary).where(Promo.id == pege)
        dictionary = session.execute(query_dictionary).scalars().first()
        query_photo = select(Promo.photo).where(Promo.id == pege)
        photo = session.execute(query_photo).scalars().first()
        caption = (f"{html.bold(f"<i>{title}</i>")}\n"
                   f"{dictionary}\n")
        await state.update_data({"pege": pege})
        photo = InputMediaPhoto(media=photo, caption=caption)
        await callback.message.edit_media(media=photo, reply_markup=menu_button(pege))
        await state.set_state(ProStates.promostate)

@menu_router.callback_query(F.data=="qullanma")
async def qullanma_menu(callback:CallbackQuery,state:FSMContext):
    try:
        data = await state.get_data()
        query_video = select(Promo.video).where(Promo.id == data['pege'])
        video = session.execute(query_video).scalars().first()
        query_title = select(Promo.title).where(Promo.id == data['pege'])
        title = session.execute(query_title).scalars().first()
        query_dictionary = select(Promo.dictionary).where(Promo.id == data['pege'])
        dictionary = session.execute(query_dictionary).scalars().first()
        caption = (f"{html.bold(f"<i>{title}</i>")}\n"
                   f"{dictionary}\n")
        media = InputMediaVideo(media=video, caption=caption)
        await callback.message.edit_media(media=media, reply_markup=back_button())
        await state.set_state(ProStates.back)
    except Exception as e:
        pass

@menu_router.callback_query(ProStates.back,F.data=="back")
async def back_menu(callback:CallbackQuery,state:FSMContext):
    data=await state.get_data()
    pege=data['pege']
    query_title = select(Promo.title).where(Promo.id == pege)
    title = session.execute(query_title).scalars().first()
    query_dictionary = select(Promo.dictionary).where(Promo.id == pege)
    dictionary = session.execute(query_dictionary).scalars().first()
    query_photo = select(Promo.photo).where(Promo.id == pege)
    photo = session.execute(query_photo).scalars().first()
    caption = (f"{html.bold(f"<i>{title}</i>")}\n"
               f"{dictionary}\n")
    await state.update_data({"pege": pege})
    media = InputMediaPhoto(media=photo, caption=caption)
    await callback.message.edit_media(media=media, reply_markup=menu_button(pege))
    await state.set_state(ProStates.menustate)

@menu_router.callback_query(ProStates.menustate,F.data=="bizhaqimizda")
async def menustate_menu(callback:CallbackQuery,state:FSMContext):

    try:
        query_id = select(func.min(My))
        min_id = session.execute(query_id).scalars().first()
        query_dectionary = select(My.dectionary).where(Promo.id == min_id)
        dectionary = session.execute(query_dectionary).scalars().first()
        query_photo = select(My.photo).where(Promo.id == min_id)
        photo = session.execute(query_photo).scalars().first()
        query_phone = select(My.phone).where(Promo.id == min_id)
        phone = session.execute(query_phone).scalars().first()
        caption = (f"{html.bold(f"📱{phone}")}\n"
                   f"{dectionary}\n")
        media = InputMediaPhoto(media=photo, caption=caption)
        await callback.message.edit_media(media=media, reply_markup=back_button())
        await state.set_state(ProStates.my)
    except Exception as e:
        pass