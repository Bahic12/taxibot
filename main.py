import sqlite3
import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.utils import executor

import logging

from markup import AdminMenu, start_keyboard, DrivePeopleMenu, ABPassengerMenu, PeopleMenu, PhoneMenu, OrderMenu, DayPassengerMenu, HourPassengerMenu, DriveTrueMenu


logging.basicConfig(level=logging.INFO)

TOKEN = '2120398645:AAG0HH6AWTOSJPiE5yIqIr_qPs51DkgVyoU'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#  ---config---
users = None
conn = sqlite3.connect('sqlite.db')



@dp.message_handler(commands=['admin'])
async def password(message: types.Message):
    if message.chat.id == 1756891119:
        conchi = conn.execute("select * from COMPANY")
        son = list(conchi)
        P_number = 0
        v_seti = 0
        D_number = 0
        dup = []
        pup = []
        pups = []
        for i in son:
            i = list(i)
            if i[1] == 'Passenger':
                if i[5] == None:
                    P_number += 1
                    pups.append(i)
                else:
                    pup.append(i)
                    v_seti += 1
            elif i[1] == 'Drive':
                D_number += 1
                dup.append(i)

        await bot.send_message(message.from_user.id,f"Yo'lovchi soni: {P_number}\nHaydovchi soni:{D_number}\nSet:{v_seti}",reply_markup=AdminMenu)
        # son = 0
        # for i in pup:
        #     son += 1
        #     await bot.send_message(message.from_user.id,F"{son}\nBoriladigan joy: {i[2]}\nKuni: {i[3]}\nVaqti: {i[4]}\nOdam soni: {i[5]}\nMobil raqam: {i[7]}\nIsmi: {i[8]}")
        # son = 0
        # for i in pups:
        #     son += 1
        #     await bot.send_message(message.from_user.id,f"{son}: Ismi: {i[8]}")
        # son = 0
        # for i in dup:
        #     son += 1
        #     await bot.send_message(message.from_user.id,f"{son} : Ismi: {i[8]}\nMobile raqam: {i[7]}")

    else:
        await bot.send_message(message.from_user.id,'Siz Admin emassiz')


@dp.message_handler(text='Passenger')
async def passenger(message: types.Message):
    if message.chat.id == 1756891119:
        conchi = conn.execute("select * from COMPANY")
        son = list(conchi)
        p = 0
        for i in son:
            if i[1] == 'Passenger' and i[5] == None:
                p += 1
                await bot.send_message(message.from_user.id, f"{p}: Ismi: {i[8]}")
        if p == 0:
            await bot.send_message(message.chat.id, 'Hozircha hech kim yo\'q')
@dp.message_handler(text='Drive')
async def passenger(message: types.Message):
    if message.chat.id == 1756891119:
        conchi = conn.execute("select * from COMPANY")
        son = list(conchi)
        p = 0
        for i in son:
            if i[1] == 'Drive':
                p += 1
                await bot.send_message(message.from_user.id, f"{p}: Ismi: {i[8]}")
        if p == 0:
            await bot.send_message(message.chat.id, 'Hozircha hech kim yo\'q')
@dp.message_handler(text='Set')
async def passenger(message: types.Message):
    if message.chat.id == 1756891119:
        conchi = conn.execute("select * from COMPANY")
        son = list(conchi)
        p = 0
        for i in son:
            if i[1] == 'Passenger' and i[7] != None:
                p += 1
                await bot.send_message(message.from_user.id,F"{p}\nBoriladigan joy: {i[2]}\nKuni: {i[3]}\nVaqti: {i[4]}\nOdam soni: {i[5]}\nMobil raqam: {i[7]}\nIsmi: {i[8]}")
        if p == 0:
            await bot.send_message(message.chat.id,'Hozircha hech kim yo\'q')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    conchi = conn.execute("select ID from COMPANY where ID=(?);",(str(message.chat.id),))
    i = list(conchi)
    if i != []:
        son = list(i)
        if len(son) >=2:
            man = message.chat.id
            i = list(i[0])
            if i[1] == "Drive":
                await bot.send_message(message.from_user.id,'Assalomu aleykum {0.first_name} odam olishingiz mumkin'.format(message.from_user),reply_markup=DrivePeopleMenu)
            elif i[1] == "Passenger":
                await bot.send_message(message.from_user.id,'Assalomu aleykum {0.first_name} qayerga va qachon borasiz'.format(message.from_user),reply_markup=ABPassengerMenu)

    if i == []:
        conn.execute("insert into COMPANY (ID) values (?)",(str(message.chat.id),))
        await message.answer("😊Assalomu aleykum User\n"
                             "🚘Andijonga borish kerakmi yoki Toshkentga borish kerakmi?\n"
                             "🗒unda joyni tanlang, ⏱vaqti belgilang,\n"
                             "📑nechikishiligini tanlang va\n"
                             "🗳contactingizni kiriting".format(message.from_user), reply_markup=start_keyboard)
        await message.answer("🚗Siz haydovchi bo'lsangiz\n"
                             "🗳contactingizni kriting\n"
                             "🚘mashina raqamingizni kiritng\n"
                             "Va odam olish tugmasini ezib osongina \n"
                             "kochada turmasdan odam to'plashingiz mumkin")



@dp.message_handler(content_types='contact')
async def contact(message: types.Message):
    conchi = conn.execute("select * from COMPANY where ID=(?);", (str(message.chat.id),))
    i = list(conchi)
    if i != []:
        conchi = conn.execute("select * from COMPANY where ID =(?);",
                                  (str(message.chat.id),))
        sons = list(i[0])
        if sons[1] == "Passenger":
            await bot.send_message(message.from_user.id,'Iltimos kuting sizga tez orada telefon boladi\nAgar bekor qilmoqchi bolsangiz bekor qilish tugmasini ezing\nVa yana botdan foydalanmoqchi bo\'lsangiz chatga /start yozing')
            await bot.send_message(message.from_user.id, "Haydovchi bilan kelishib olgandan so'ng aytib qo'ying \noldim degan tugmani ezib qo'yisn yo'qsa sizga qo'ng'iroq qilaverishadi", reply_markup=OrderMenu)
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute(
                    "insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN, PHONE_NUMBER, NAME) values (?,?,?,?,?,?,?,?,?);",
                    (son[0], son[1], son[2], son[3], son[4], son[5], son[6],str(message.contact.phone_number),message.contact.full_name))
        elif sons[1] == "Drive":
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute(
                    "insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN, PHONE_NUMBER,NAME) values (?,?,?,?,?,?,?,?,?);",
                    (son[0], son[1],None,None,None,None,None,str(message.contact.phone_number),message.contact.full_name))
            await bot.send_message(message.from_user.id, 'Odam olishingiz mumkin. \nYo\'lingiz bexatar bo\'lsin', reply_markup=DrivePeopleMenu)



# @dp.message_handler(content_types='location')
# async def location(message: types.Message):
#     for i in people:
#         if i[0] == message.chat.id:
#             i.append([message.location.longitude,message.location.latitude])

@dp.message_handler(commands='help')
async def location(message: types.Message):
    await bot.send_message(message.from_user.id,'Assalomu aleykum bu botda siz Andijondan Tashkentga va Tashkentdan Andijonga borishingiz mumkin\n\nAgar muammolar bo\'layotgan bo\'sa murajat uchun: @baxtlimanjudajuda')


@dp.message_handler()
async def process_start_command(message: types.Message):
   cur = conn.execute("select ID from COMPANY where ID =(?)",(str(message.chat.id),))
   i = list(cur)
   if i != []:
        if message.text == 'Haydovchi':
            await bot.send_message(message.from_user.id,'Mobil raqamingizni kiriting',reply_markup=PhoneMenu)
            conn.execute("delete from COMPANY where ID=(?);",(str(message.chat.id),))
            conn.execute(f"insert into COMPANY (ID, TURI) values (?,?);",(str(message.chat.id),'Drive',))
        elif message.text == "Yo'lovchi":
            await bot.send_message(message.from_user.id,'Qayerga borishingizni tanlang',reply_markup=ABPassengerMenu)
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute(f"insert into COMPANY (ID, TURI) values (?,?);",(str(message.chat.id),'Passenger',))
        elif message.text == 'Odam olish':
            conchi = conn.execute("select *  from COMPANY where ID =(?);", (str(message.chat.id),))
            son = list(conchi)
            i = list(son[0])
            if i[1] == 'Drive':
                son = 0
                while True:
                    son += 1
                    man = conn.execute("select * from COMPANY order by RANDOM() LIMIT 1")
                    man = list(man)
                    man = list(man[0])
                    if son >= 30:
                        await bot.send_message(message.from_user.id,"Hozircha odam yo'q")
                        son = 0
                        break
                    if i[2] != man[0] and man[7] != None and man[1] == "Passenger":
                        if man[3] == 'Ertaga' and man[6] != datetime.datetime.now().strftime('%d'):
                            man[3] = 'Bugun'
                        if man[3] == 'Indinga' and man[6] != datetime.datetime.now().strftime('%d'):
                            man[3] = 'Ertaga'
                        await bot.send_message(message.from_user.id,
                                                       f"Boriladigan joy: {man[2]}\nKuni: {man[3]}\nVaqti: {man[4]}\nOdam soni: {man[5]}\nMobil raqam: {man[7]}",
                                                       reply_markup=DriveTrueMenu)
                        conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
                        conn.execute(
                                    "insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN, PHONE_NUMBER) values (?,?,?,?,?,?,?,?);",
                                    (i[0], i[1], man[0], i[3], i[4], i[5], i[6], i[7]))
                        son = 0
                        break
                    else:
                        continue



        elif message.text == 'Andijondan Tashkentga':
            await bot.send_message(message.from_user.id,'Borish kunini kiriting',reply_markup=DayPassengerMenu)
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS) values (?,?,?);", (str(message.chat.id), 'Passenger','Andijondan Tashkentga',))
        elif message.text == 'Tashkentdan Andijonga':
            await bot.send_message(message.from_user.id,'Borish kunini kiriting',reply_markup=DayPassengerMenu)
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS) values (?,?,?);", (str(message.chat.id), 'Passenger','Tashkentdan Andijonga',))
        elif message.text == 'Bugun':
            await bot.send_message(message.from_user.id,'Vaqtni kiriting',reply_markup=HourPassengerMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS  from COMPANY where ID =(?);",(str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY) values (?,?,?,?);",(son[0], son[1], son[2],'Bugun',))
        elif message.text == 'Ertaga':
            await bot.send_message(message.from_user.id,'Vaqtni kiriting',reply_markup=HourPassengerMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY) values (?,?,?,?);",(son[0], son[1], son[2], 'Ertaga',))
        elif message.text == 'Indinga':
            await bot.send_message(message.from_user.id,'Vaqtni kiriting',reply_markup=HourPassengerMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY) values (?,?,?,?);",(son[0], son[1], son[2], 'Indinga',))
        elif message.text == '1:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR ) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3],'1:00',))
        elif message.text == '2:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '2:00',))
        elif message.text == '3:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '3:00',))
        elif message.text == '4:00':
            i.append('4:00')
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '4:00',))
        elif message.text == '5:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '5:00',))
        elif message.text == '6:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '6:00',))
        elif message.text == '7:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '7:00',))
        elif message.text == '8:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '8:00',))
        elif message.text == '9:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '9:00',))
        elif message.text == '10:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '10:00',))
        elif message.text == '11:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '11:00',))
        elif message.text == '12:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '12:00',))
        elif message.text == '13:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '13:00',))
        elif message.text == '14:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '14:00',))
        elif message.text == '15:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '15:00',))
        elif message.text == '16:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], '16:00',))
        elif message.text == '17:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0],son[1], son[2], son[3], '17:00',))
        elif message.text == '18:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '18:00',))
        elif message.text == '19:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '19:00',))
        elif message.text == '20:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '20:00',))
        elif message.text == '21:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '21:00',))
        elif message.text == '22:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '22:00',))
        elif message.text == '23:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '23:00',))
        elif message.text == '24:00':
            await bot.send_message(message.from_user.id,'Odam sonini tanlang',reply_markup=PeopleMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR) values (?,?,?,?,?);",(son[0], son[1], son[2], son[3], '24:00',))
        elif message.text == '1ta odam':
            await bot.send_message(message.from_user.id,'Mobil raqamingizni kiriting',reply_markup=PhoneMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY, HOUR  from COMPANY where ID =(?);", (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE,DAYN) values (?,?,?,?,?,?,?);",(son[0], son[1], son[2], son[3], son[4],'1ta odam',datetime.datetime.now().strftime("%d")))
        elif message.text == '2ta odam':
            await bot.send_message(message.from_user.id,'Mobil raqamingizni kiriting',reply_markup=PhoneMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY, HOUR  from COMPANY where ID =(?);",(str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE,DAYN) values (?,?,?,?,?,?,?);",(son[0], son[1], son[2], son[3], son[4], '2ta odam',datetime.datetime.now().strftime("%d")))
        elif message.text == '3ta odam':
            await bot.send_message(message.from_user.id,'Mobil raqamingizni kiriting',reply_markup=PhoneMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY, HOUR  from COMPANY where ID =(?);",
                                  (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN) values (?,?,?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], son[4], '3ta odam',datetime.datetime.now().strftime("%d")))

        elif message.text == '4ta odam':
            await bot.send_message(message.from_user.id,'Mobil raqamingizni kiriting',reply_markup=PhoneMenu)
            conchi = conn.execute("select ID, TURI, ADDRESS, DAY, HOUR  from COMPANY where ID =(?);",
                                  (str(message.chat.id),))
            cur = list(conchi)
            son = list(cur[0])
            conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
            conn.execute("insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN) values (?,?,?,?,?,?,?);",
                         (son[0], son[1], son[2], son[3], son[4], '4ta odam',datetime.datetime.now().strftime("%d")))

            # conn.execute("insert into COMPANY (ID,TYPE,ADDRESS,DAY,HOUR,PEOPLE) values (?,?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))
        elif message.text == 'Bekor qilish':
            conchi = conn.execute("select * from COMPANY where ID = (?);",(str(message.chat.id),))
            conchi = list(conchi)
            i = list(conchi[0])
            if i[1] == 'Passenger':
                if i[6] != None:
                    conchi = conn.execute("select *  from COMPANY where ID =(?);",
                                          (str(message.chat.id),))
                    cur = list(conchi)
                    son = list(cur[0])
                    conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
                    conn.execute(
                        "insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN, PHONE_NUMBER, NAME) values (?,?,?,?,?,?,?,?,?);",
                        (son[0],son[1],None,None,None,None,None,None,son[8]))
                    await bot.send_message(message.from_user.id, 'Yana kerak bolsa \n\nQayerga borishingizni tanlang', reply_markup=ABPassengerMenu)
                else:
                    await bot.send_message(message.from_user.id,'Yana kerak bolsa \n\nQayerga borishingizni tanlang',reply_markup=ABPassengerMenu)
        elif message.text == 'Oldim':
            son = conn.execute("select * from COMPANY where ID = (?);", (str(message.chat.id),))
            son = list(son)
            i = list(son[0])
            if i[2] != None:
                conchi = conn.execute("select ID, TURI  from COMPANY where ID =(?);", (i[2],))
                cur = list(conchi)
                son = list(cur[0])
                conn.execute("delete from COMPANY where ID = (?);", (i[2],))
                conn.execute("insert into COMPANY (ID, TURI) values (?,?);", (son[0], son[1],))
            await bot.send_message(message.from_user.id,"Yaxshi yana odam kerak bo'lsa \"Odam olish\" tugmasini bosing", reply_markup=DrivePeopleMenu)
        elif message.text == 'Boshqasi':
            conchi = conn.execute("select *  from COMPANY where ID =(?);", (str(message.chat.id),))
            son = list(conchi)
            i = list(son[0])
            if i[1] == 'Drive':
                son = 0
                while True:
                    son += 1
                    man = conn.execute("select * from COMPANY order by RANDOM() LIMIT 1")
                    man = list(man)
                    man = list(man[0])
                    if son >= 30:
                        await bot.send_message(message.from_user.id, "Hozircha odam yo'q")
                        son = 0
                        break
                    if i[2] != man[0] and man[7] != None and man[1] == "Passenger":
                        if man[3] == 'Ertaga' and man[6] != datetime.datetime.now().strftime('%d'):
                            man[3] = 'Bugun'
                        if man[3] == 'Indinga' and man[6] != datetime.datetime.now().strftime('%d'):
                            man[3] = 'Ertaga'
                        await bot.send_message(message.from_user.id,
                                               f"Boriladigan joy: {man[2]}\nKuni: {man[3]}\nVaqti: {man[4]}\nOdam soni: {man[5]}\nMobil raqam: {man[7]}",
                                               reply_markup=DriveTrueMenu)
                        conn.execute("delete from COMPANY where ID=(?);", (str(message.chat.id),))
                        conn.execute(
                            "insert into COMPANY (ID, TURI, ADDRESS, DAY, HOUR, PEOPLE, DAYN, PHONE_NUMBER) values (?,?,?,?,?,?,?,?);",
                            (i[0], i[1], man[0], i[3], i[4], i[5], i[6], i[7]))
                        son = 0
                        break
                    else:
                        continue









if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)