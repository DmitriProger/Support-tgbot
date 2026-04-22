from aiogram.fsm.state import State, StatesGroup


# Стейт для отправки тикета
class UserReport(StatesGroup):
    report = State()
    waiting = State()
