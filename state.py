from aiogram.fsm.state import StatesGroup,State

class AnketaState(StatesGroup):
    full_name=State()
    age=State()
    Texnologiya=State()
    tele2=State()
    Aloqa=State()
    addres=State()
    Narxi=State()
    Kasbi=State()
    Ish_vaqti=State()
    Maqsad=State()


class SherikState(StatesGroup):
    ism_menu=State()
    texno=State()
    tele=State()
    aloqa=State()
    hudud2=State()
    narxi2=State()
    kasbi2=State()
    ish2=State()
    maqsad2=State()

class HodimState(StatesGroup):
    idora=State()
    texno2=State()
    telegram=State()
    aloqa3=State()
    hudud3=State()
    masul=State()
    ish3=State()
    maosh=State()
    qoshimcha=State()

class UstozState(StatesGroup):
    shogird=State()
    yosh=State()
    texno3=State()
    telegram2=State()
    aloqa4=State()
    hudud4=State()
    narx3=State()
    kasb3=State()
    ish4=State()
    maqsad3=State()

class ShogirdState(StatesGroup):
    ustoz=State()
    yosh2=State()
    texno4=State()
    telegram3=State()
    aloqa5=State()
    hudud5=State()
    narx4=State()
    kasb4=State()
    ish5=State()
    maqsad4=State()