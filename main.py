import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from menu_keyboard import menu_start
from state import AnketaState, SherikState, HodimState, UstozState, ShogirdState
from aiogram.fsm.context import FSMContext


BOT_TOKEN = "8025981584:AAG4RSlEFZlqLwhyVRaOHgwKKqvQrkxqv28"
ADMIN_ID = 8725861558

dp = Dispatcher()

# /start komandasi uchun handler


@dp.message(Command("start"))
async def start_message(message: Message, bot: Bot):
    admin_txt = f"Yangi foydalanuvchi\n\n"
    admin_txt += f"Ismi: {message.from_user.full_name}\n"
    admin_txt += f"username: @{message.from_user.username}\n"

    txt = f"Assalomu aleykum {message.from_user.full_name}"
    await message.answer(txt, reply_markup=menu_start)

    await bot.send_message(chat_id=ADMIN_ID, text=admin_txt)






#Ankate
@dp.message(F.text=="Ish joyi kerak")
async def anketa_message(message:Message,state:FSMContext):
    await message.answer("Ism Familyangizni kiriting")
    await state.set_state(AnketaState.full_name)

@dp.message(AnketaState.full_name)
async def age_answer(message:Message,state:FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(
        """
    🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19    
"""
    )
    await state.set_state(AnketaState.age)


@dp.message(AnketaState.age)
async def Texnologiya_answer(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(
        """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""

    )
    await state.set_state(AnketaState.Texnologiya)

@dp.message(AnketaState.Texnologiya)
async def tele_answer(messgae:Message,state:FSMContext):
    await state.update_data(Texnologiya=messgae.text)
    await messgae.answer(
        """
    Telegramingiz:

Masalan @...    
"""
    )
    await state.set_state(AnketaState.tele2)


@dp.message(AnketaState.tele2)
async def aloqa_answer(message: Message, state: FSMContext):
    await state.update_data(tele2=message.text)
    await message.answer(
        """
    📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    )
    await state.set_state(AnketaState.Aloqa)





@dp.message(AnketaState.Aloqa)
async def hudud_answer(message:Message,state:FSMContext):
    await state.update_data(Aloqa=message.text)
    await message.answer(
       """
    🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting
"""
    )
    await state.set_state(AnketaState.addres)


@dp.message(AnketaState.addres)
async def narxi_answer(message: Message, state: FSMContext):
    await state.update_data(addres=message.text)
    await message.answer(
        """
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    )
    await state.set_state(AnketaState.Narxi)


@dp.message(AnketaState.Narxi)
async def kasbi_answer(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)
    await message.answer(
        """
    👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    )
    await state.set_state(AnketaState.Kasbi)


@dp.message(AnketaState.Kasbi)
async def vaqti_answer(message: Message, state: FSMContext):
    await state.update_data(Kasbi=message.text)
    await message.answer(
        """
    🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    )
    await state.set_state(AnketaState.Ish_vaqti)


@dp.message(AnketaState.Ish_vaqti)
async def maqsad_answer(message: Message, state: FSMContext):
    await state.update_data(Ish_vaqti=message.text)
    await message.answer(
        """
    🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering
"""
    )
    await state.set_state(AnketaState.Maqsad)


@dp.message(AnketaState.age)
async def age_answer(message: Message, state: FSMContext):
    await state.update_data(age=message.text)


@dp.message(AnketaState.Texnologiya)
async def technology_answer(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)

@dp.message(AnketaState.tele2)
async def tele2_answer(message:Message,state:FSMContext):
    await state.update_data(tele2=message.text)



@dp.message(AnketaState.addres)
async def address(message: Message, state: FSMContext):
    await state.update_data(addres=message.text)



@dp.message(AnketaState.Narxi)
async def money(message: Message, state: FSMContext):
    await state.update_data(Narxi=message.text)


@dp.message(AnketaState.Ish_vaqti)
async def job(message: Message, state: FSMContext):
    await state.update_data(Ish_vaqti=message.text)


@dp.message(AnketaState.Aloqa)
async def murojot(message: Message, state: FSMContext):
    await state.update_data(Aloqa=message.text)


@dp.message(AnketaState.Maqsad)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)



    data=await state.get_data()
    full_name=data["full_name"]
    age=data["age"]
    texnologiya=data["Texnologiya"]
    tele2=data["tele2"]
    Aloqa=data["Aloqa"]
    addres=data["addres"]
    Narxi=data["Narxi"]
    Kasbi=data["Kasbi"]
    Ish_vaqti=data["Ish_vaqti"]
    Maqsad = data["maqsad"]

    txt=f"Ish joyi kerak:\n\n"
    txt += f"👨‍💼 Xodim: {full_name}\n"
    txt += f"🕑 Yosh: {age}\n"
    txt += f"📚 Texnologiya: {texnologiya}\n"
    txt += f"🇺🇿 Telegram: {tele2}\n"
    txt += f"📞 Aloqa: {Aloqa}\n"
    txt += f"🌐 Hudud: {addres}\n"
    txt += f"💰 Narxi: {Narxi}\n"
    txt += f"👨🏻‍💻 Kasbi: {Kasbi}\n"
    txt += f"🕰 Murojaat qilish vaqti: {Ish_vaqti}\n"
    txt += f"🔎 Maqsad: {Maqsad}\n"
    txt += f"Agar ma'lumotlar tog'ra bo'sa Ha\n"
    txt += f"Agar ma'lumotlar noto'g'ri bo'lsa Yo'q deb yoboring"  
    

    await message.answer(txt)
    await state.clear()



#Sherik
@dp.message(F.text=="Sherik kerak")
async def sherik_ism(message:Message,state:FSMContext):
    await message.answer("Ism Familyangizni kiriting")
    await state.set_state(SherikState.ism_menu)

@dp.message(SherikState.ism_menu)
async def age_answer(message:Message,state:FSMContext):
    await state.update_data(ism_menu=message.text)
    await message.answer(
        """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    )
    
    await state.set_state(SherikState.texno)


@dp.message(SherikState.texno)
async def Texnologiya_answer(message: Message, state: FSMContext):
    await state.update_data(texno=message.text)
    await message.answer(
        """
    📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""

    )
    await state.set_state(SherikState.tele)


@dp.message(SherikState.tele)
async def aloqa_answer(message: Message, state: FSMContext):
    await state.update_data(tele2=message.text)
    await message.answer(
        """
    Telegramingiz:

Masalan @...
"""
    )
    await state.set_state(SherikState.aloqa)


@dp.message(SherikState.aloqa)
async def hudud_answer(message:Message,state:FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer(
       """
    🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    )
    await state.set_state(SherikState.hudud2)


@dp.message(SherikState.hudud2)
async def narxi_answer(message: Message, state: FSMContext):
    await state.update_data(hudud2=message.text)
    await message.answer(
        """
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    )
    await state.set_state(SherikState.narxi2)


@dp.message(SherikState.narxi2)
async def kasbi_answer(message: Message, state: FSMContext):
    await state.update_data(narxi2=message.text)
    await message.answer(
        """
    👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    )
    await state.set_state(SherikState.kasbi2)


@dp.message(SherikState.kasbi2)
async def vaqti_answer(message: Message, state: FSMContext):
    await state.update_data(kasbi2=message.text)
    await message.answer(
        """
    🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    )
    await state.set_state(SherikState.ish2)

@dp.message(SherikState.ish2)
async def ish_answer(message:Message,state:FSMContext):
    await state.update_data(ish2=message.text)
    await message.answer(
        """
    🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    )
    await state.set_state(SherikState.maqsad2)





@dp.message(SherikState.texno)
async def age_answer(message: Message, state: FSMContext):
    await state.update_data(texno=message.text)


@dp.message(SherikState.tele)
async def technology_answer(message: Message, state: FSMContext):
    await state.update_data(tele2=message.text)



@dp.message(SherikState.aloqa)
async def address(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)



@dp.message(SherikState.hudud2)
async def money(message: Message, state: FSMContext):
    await state.update_data(hudud2=message.text)


@dp.message(SherikState.narxi2)
async def job(message: Message, state: FSMContext):
    await state.update_data(narxi2=message.text)


@dp.message(SherikState.kasbi2)
async def murojot(message: Message, state: FSMContext):
    await state.update_data(kasb2=message.text)


@dp.message(SherikState.ish2)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(ish2=message.text)
    
@dp.message(SherikState.maqsad2)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad2=message.text)

    data=await state.get_data()
    ism_menu=data["ism_menu"]
    texno=data["texno"]
    tele2=data["tele2"]
    aloqa=data["aloqa"]
    hudud2=data["hudud2"]
    narxi2=data["narxi2"]
    kasbi2=data["kasbi2"]
    ish2=data["ish2"]
    maqsad2=data["maqsad2"]

    txt=f"Sherik kerak:\n\n"
    txt += f"🏅 Sherik: {ism_menu}\n"
    txt += f"📚 Texnologiya: {texno}\n"
    txt += f"🇺🇿 Telegram: {tele2}\n"
    txt += f"📞 Aloqa: {aloqa}\n"
    txt += f"🌐 Hudud: {hudud2}\n"
    txt += f"💰 Narxi: {narxi2}\n"
    txt += f"👨🏻‍💻 Kasbi: {kasbi2}\n"
    txt += f"🕰 Murojaat qilish vaqti: {ish2}\n"
    txt += f"🔎 Maqsad: {maqsad2}\n"
    txt += f"Agar ma'lumotlar tog'ra bo'sa Ha\n"
    txt += f"Agar ma'lumotlar noto'g'ri bo'lsa Yo'q deb yoboring"    

    await message.answer(txt)
    await state.clear()

@dp.message(F.text=="Yo'q")
async def ha_menu(message:Message):
    await message.answer("So'rovingiz qabul qilinmadi❌",reply_markup=menu_start)

@dp.message(F.text=="Ha")
async def ha_menu(message:Message):
    await message.answer("So'rovingiz qabul qilindi🥳",reply_markup=menu_start)


#Hodim kerak
@dp.message(F.text=="Hodim kerak")
async def hodim_menu(message:Message,state:FSMContext):
    await message.answer("🏢 Idorangiz nomi:")
    await state.set_state(HodimState.idora)

@dp.message(HodimState.idora)
async def idora_answer(message:Message,state:FSMContext):
    await state.update_data(idora=message.text)
    await message.answer(
        """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    )
    
    await state.set_state(HodimState.texno2)


@dp.message(HodimState.texno2)
async def Texnologiya2_answer(message: Message, state: FSMContext):
    await state.update_data(texno2=message.text)
    await message.answer(
        """
    Telegramingiz:

Masalan @...
"""


    )
    await state.set_state(HodimState.telegram)


@dp.message(HodimState.telegram)
async def aloqa2_answer(message: Message, state: FSMContext):
    await state.update_data(telegram=message.text)
    await message.answer(
        """
    📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    )
    await state.set_state(HodimState.aloqa3)


@dp.message(HodimState.aloqa3)
async def hudud2_answer(message:Message,state:FSMContext):
    await state.update_data(aloqa3=message.text)
    await message.answer(
       """
    🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    )
    await state.set_state(HodimState.hudud3)


@dp.message(HodimState.hudud3)
async def narxi2_answer(message: Message, state: FSMContext):
    await state.update_data(hudud3=message.text)
    await message.answer("✍️Mas'ul ism sharifi?")
    await state.set_state(HodimState.masul)

@dp.message(HodimState.masul)
async def vaqti2_answer(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)
    await message.answer(
        """
    🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    )
    await state.set_state(HodimState.ish3)

@dp.message(HodimState.ish3)
async def ish2_answer(message:Message,state:FSMContext):
    await state.update_data(ish3=message.text)
    await message.answer("💰 Maoshni kiriting?")
    await state.set_state(HodimState.maosh)

@dp.message(HodimState.maosh)
async def qoshimcha2_(message:Message,state:FSMContext):
    await state.update_data(maosh=message.text)
    await message.answer("‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(HodimState.qoshimcha)






@dp.message(HodimState.texno2)
async def Texnologiya2_answer(message: Message, state: FSMContext):
    await state.update_data(texno3=message.text)


@dp.message(HodimState.telegram)
async def tele2_answer(message: Message, state: FSMContext):
    await state.update_data(telegram=message.text)



@dp.message(HodimState.aloqa3)
async def address2(message: Message, state: FSMContext):
    await state.update_data(aloqa3=message.text)



@dp.message(HodimState.hudud3)
async def money2(message: Message, state: FSMContext):
    await state.update_data(hudud3=message.text)


@dp.message(HodimState.masul)
async def job2(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)


@dp.message(HodimState.ish3)
async def murojot2(message: Message, state: FSMContext):
    await state.update_data(ish3=message.text)


@dp.message(HodimState.maosh)
async def maqsad2(message: Message, state: FSMContext):
    await state.update_data(maosh=message.text)
    
@dp.message(HodimState.qoshimcha)
async def maqsad3(message: Message, state: FSMContext):
    await state.update_data(qoshimcha=message.text)

    data=await state.get_data()
    idora=data["idora"]
    texno2=data["texno2"]
    telegram=data["telegram"]
    aloqa3=data["aloqa3"]
    hudud3=data["hudud3"]
    masul=data["masul"]
    ish3=data["ish3"]
    maosh=data["maosh"]
    qoshimcha=data["qoshimcha"]

    txt=f"Hodim kerak:\n\n"
    txt += f"🏢 Idora: {idora}\n"
    txt += f"📚 Texnologiya: {texno2}\n"
    txt += f"🇺🇿 Telegram: {telegram}\n"
    txt += f"📞 Aloqa: {aloqa3}\n"
    txt += f"🌐 Hudud: {hudud3}\n"
    txt += f"✍️ Mas'ul: {masul}\n"
    txt += f"🕰 Murojaat qilish vaqti: {ish3}\n"
    txt += f"💰 Maosh: {maosh}\n"
    txt += f"‼️ Qo`shimcha: {qoshimcha}\n"
    txt += f"Agar ma'lumotlar tog'ra bo'sa Ha\n"
    txt += f"Agar ma'lumotlar noto'g'ri bo'lsa Yo'q deb yoboring"    

    await message.answer(txt)
    await state.clear()


#Ustoz
@dp.message(F.text=="Ustoz kerak")
async def anketa_message(message:Message,state:FSMContext):
    await message.answer("Ism Familyangizni kiriting")
    await state.set_state(UstozState.shogird)

@dp.message(UstozState.shogird)
async def age_answer(message:Message,state:FSMContext):
    await state.update_data(shogird=message.text)
    await message.answer(
        """
    🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19    
"""
    )
    await state.set_state(UstozState.yosh)


@dp.message(UstozState.yosh)
async def Texnologiya_answer(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await message.answer(
        """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""

    )
    await state.set_state(UstozState.texno3)


@dp.message(UstozState.texno3)
async def aloqa_answer(message: Message, state: FSMContext):
    await state.update_data(texno3=message.text)
    await message.answer(
        """
    Telegramingiz:

Masalan @...    
"""
    )
    await state.set_state(UstozState.telegram2)

@dp.message(UstozState.telegram2)
async def telegram_answer(message:Message,state:FSMContext):
    await state.update_data(telegram2=message.text)
    await message.answer(
        """
    📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    )
    await state.set_state(UstozState.aloqa4)

@dp.message(UstozState.aloqa4)
async def hudud_answer(message:Message,state:FSMContext):
    await state.update_data(aloqa4=message.text)
    await message.answer(
       """
    🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    )
    await state.set_state(UstozState.hudud4)


@dp.message(UstozState.hudud4)
async def narxi_answer(message: Message, state: FSMContext):
    await state.update_data(hudud4=message.text)
    await message.answer(
        """
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    )
    await state.set_state(UstozState.narx3)


@dp.message(UstozState.narx3)
async def kasbi_answer(message: Message, state: FSMContext):
    await state.update_data(narx3=message.text)
    await message.answer(
        """
    👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    )
    await state.set_state(UstozState.kasb3)


@dp.message(UstozState.kasb3)
async def vaqti_answer(message: Message, state: FSMContext):
    await state.update_data(kasb3=message.text)
    await message.answer(
        """
    🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    )
    await state.set_state(UstozState.ish4)


@dp.message(UstozState.ish4)
async def maqsad_answer(message: Message, state: FSMContext):
    await state.update_data(ish4=message.text)
    await message.answer(
        """
    🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering
"""
    )
    await state.set_state(UstozState.maqsad3)


@dp.message(UstozState.yosh)
async def age_answer(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)


@dp.message(UstozState.texno3)
async def technology_answer(message: Message, state: FSMContext):
    await state.update_data(texno3=message.text)



@dp.message(UstozState.telegram2)
async def address(message: Message, state: FSMContext):
    await state.update_data(telegram2=message.text)

@dp.message(UstozState.aloqa4)
async def murojot(message: Message, state: FSMContext):
    await state.update_data(aloqa4=message.text)


@dp.message(UstozState.hudud4)
async def money(message: Message, state: FSMContext):
    await state.update_data(hudud4=message.text)


@dp.message(UstozState.narx3)
async def job(message: Message, state: FSMContext):
    await state.update_data(narx3=message.text)

@dp.message(UstozState.kasb3)
async def job(message: Message, state: FSMContext):
    await state.update_data(kasb3=message.text)

@dp.message(UstozState.ish4)
async def job(message: Message, state: FSMContext):
    await state.update_data(ish4=message.text)


@dp.message(UstozState.maqsad3)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad3=message.text)



    data=await state.get_data()
    shogird=data["shogird"]
    yosh=data["yosh"]
    texno3=data["texno3"]
    telegram2=data["telegram2"]
    aloqa4=data["aloqa4"]
    hudud4=data["hudud4"]
    narx3=data["narx3"]
    kasb3=data["kasb3"]
    ish4=data["ish4"]
    maqsad3=data["maqsad3"]

    txt=f"Ustoz kerak\n\n"
    txt += f"🎓 Shogird: {shogird}\n"
    txt += f"🌐 Yosh: {yosh}\n"
    txt += f"📚 Texnologiya: {texno3}\n"
    txt += f"🇺🇿 Telegram: {telegram2}\n"
    txt += f"📞 Aloqa: {aloqa4}"
    txt += f"🌐 Hudud: {hudud4}\n"
    txt += f"💰 Narxi: {narx3}\n"
    txt += f"👨🏻‍💻 Kasbi: {kasb3}\n"
    txt += f"🕰 Murojaat qilish vaqti: {ish4}\n"
    txt += f"🔎 Maqsad: {maqsad3}\n"
    txt += f"Agar ma'lumotlar tog'ra bo'sa Ha\n"
    txt += f"Agar ma'lumotlar noto'g'ri bo'lsa Yo'q deb yoboring"  
    

    await message.answer(txt)
    await state.clear()


#Shogird
@dp.message(F.text=="Shogird kerak")
async def anketa_message(message:Message,state:FSMContext):
    await message.answer("Ism Familyangizni kiriting")
    await state.set_state(ShogirdState.ustoz)

@dp.message(ShogirdState.ustoz)
async def age_answer(message:Message,state:FSMContext):
    await state.update_data(ustoz=message.text)
    await message.answer(
        """
    🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19    
"""
    )
    await state.set_state(ShogirdState.yosh2)


@dp.message(ShogirdState.yosh2)
async def Texnologiya_answer(message: Message, state: FSMContext):
    await state.update_data(yosh2=message.text)
    await message.answer(
        """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""

    )
    await state.set_state(ShogirdState.texno4)


@dp.message(ShogirdState.texno4)
async def aloqa_answer(message: Message, state: FSMContext):
    await state.update_data(texno4=message.text)
    await message.answer(
        """
    Telegramingiz:

Masalan @...    
"""
    )
    await state.set_state(ShogirdState.telegram3)

@dp.message(ShogirdState.telegram3)
async def telegram_answer(message:Message,state:FSMContext):
    await state.update_data(telegram3=message.text)
    await message.answer(
        """
    📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    )
    await state.set_state(ShogirdState.aloqa5)

@dp.message(ShogirdState.aloqa5)
async def hudud_answer(message:Message,state:FSMContext):
    await state.update_data(aloqa5=message.text)
    await message.answer(
       """
    🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    )
    await state.set_state(ShogirdState.hudud5)


@dp.message(ShogirdState.hudud5)
async def narxi_answer(message: Message, state: FSMContext):
    await state.update_data(hudud5=message.text)
    await message.answer(
        """
    💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    )
    await state.set_state(ShogirdState.narx4)


@dp.message(ShogirdState.narx4)
async def kasbi_answer(message: Message, state: FSMContext):
    await state.update_data(narx4=message.text)
    await message.answer(
        """
    👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    )
    await state.set_state(ShogirdState.kasb4)


@dp.message(ShogirdState.kasb4)
async def vaqti_answer(message: Message, state: FSMContext):
    await state.update_data(kasb4=message.text)
    await message.answer(
        """
    🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    )
    await state.set_state(ShogirdState.ish5)


@dp.message(ShogirdState.ish5)
async def maqsad_answer(message: Message, state: FSMContext):
    await state.update_data(ish5=message.text)
    await message.answer(
        """
    🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering
"""
    )
    await state.set_state(ShogirdState.maqsad4)


@dp.message(ShogirdState.yosh2)
async def age_answer(message: Message, state: FSMContext):
    await state.update_data(yosh2=message.text)


@dp.message(ShogirdState.texno4)
async def technology_answer(message: Message, state: FSMContext):
    await state.update_data(texno4=message.text)



@dp.message(ShogirdState.telegram3)
async def address(message: Message, state: FSMContext):
    await state.update_data(telegram3=message.text)

@dp.message(ShogirdState.aloqa5)
async def murojot(message: Message, state: FSMContext):
    await state.update_data(aloqa5=message.text)


@dp.message(ShogirdState.hudud5)
async def money(message: Message, state: FSMContext):
    await state.update_data(hudud5=message.text)


@dp.message(ShogirdState.narx4)
async def job(message: Message, state: FSMContext):
    await state.update_data(narx4=message.text)

@dp.message(ShogirdState.kasb4)
async def job(message: Message, state: FSMContext):
    await state.update_data(kasb4=message.text)

@dp.message(ShogirdState.ish5)
async def job(message: Message, state: FSMContext):
    await state.update_data(ish5=message.text)


@dp.message(ShogirdState.maqsad4)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad4=message.text)



    data=await state.get_data()
    ustoz=data["ustoz"]
    yosh2=data["yosh2"]
    texno4=data["texno4"]
    telegram3=data["telegram3"]
    aloqa5=data["aloqa5"]
    hudud5=data["hudud5"]
    narx4=data["narx4"]
    kasb4=data["kasb4"]
    ish5=data["ish5"]
    maqsad4=data["maqsad4"]

    txt=f"Shogird kerak\n\n"
    txt += f"🎓 Ustoz: {ustoz}\n"
    txt += f"🌐 Yosh: {yosh2}\n"
    txt += f"📚 Texnologiya: {texno4}\n"
    txt += f"🇺🇿 Telegram: {telegram3}\n"
    txt += f"📞 Aloqa: {aloqa5}"
    txt += f"🌐 Hudud: {hudud5}\n"
    txt += f"💰 Narxi: {narx4}\n"
    txt += f"👨🏻‍💻 Kasbi: {kasb4}\n"
    txt += f"🕰 Murojaat qilish vaqti: {ish5}\n"
    txt += f"🔎 Maqsad: {maqsad4}\n"
    txt += f"Agar ma'lumotlar tog'ra bo'sa Ha\n"
    txt += f"Agar ma'lumotlar noto'g'ri bo'lsa Yo'q deb yoboring"  
    

    await message.answer(txt)
    await state.clear()



async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())







