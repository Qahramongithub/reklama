from aiogram.fsm.state import State,StatesGroup
class ProStates(StatesGroup):
    menustate = State()
    promostate = State()
    back=State()
    my=State()

class AdminState(StatesGroup):
    title=State()
    photo=State()
