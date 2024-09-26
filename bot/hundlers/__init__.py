from aiogram import Dispatcher

from bot.hundlers.admin import admin_router
from bot.hundlers.main import menu_router
from bot.hundlers.start import start_router

dp = Dispatcher()
dp.include_routers(*[
    start_router,
    menu_router,
    admin_router
])
