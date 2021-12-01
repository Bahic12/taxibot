import random

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    ReplyKeyboardRemove


#  ----introduction----
btnDrive = KeyboardButton('Haydovchi', callback_data='btnPessanger')
btnPassenger = KeyboardButton("Yo'lovchi", callback_data='btnDrive')


#  ---2 condition Drive----
btnCar = KeyboardButton('Mashinangizni davlat raqamini kiriting')
btnMan = KeyboardButton('Odam olish')

#  ---3 condition Drive----
btnTrue = KeyboardButton('Oldim')
btnFalse = KeyboardButton('Boshqasi')

#  ---2 condition passenger----
btnA = KeyboardButton('Andijondan Tashkentga')
btnB = KeyboardButton('Tashkentdan Andijonga')

#  ---3 condition passenger----
#  ---1 day ----
btnToday = KeyboardButton('Bugun')
btnTomorrow = KeyboardButton('Ertaga')
btnIndinga = KeyboardButton("Indinga")

#  ---2 hour ----
btnHour1 = KeyboardButton('1:00')
btnHour2 = KeyboardButton('2:00')
btnHour3 = KeyboardButton('3:00')
btnHour4 = KeyboardButton('4:00')
btnHour5 = KeyboardButton('5:00')
btnHour6 = KeyboardButton('6:00')
btnHour7 = KeyboardButton('7:00')
btnHour8 = KeyboardButton('8:00')
btnHour9 = KeyboardButton('9:00')
btnHour10 = KeyboardButton('10:00')
btnHour11 = KeyboardButton('11:00')
btnHour12 = KeyboardButton('12:00')
btnHour13 = KeyboardButton('13:00')
btnHour14 = KeyboardButton('14:00')
btnHour15 = KeyboardButton('15:00')
btnHour16 = KeyboardButton('16:00')
btnHour17 = KeyboardButton('17:00')
btnHour18 = KeyboardButton('18:00')
btnHour19 = KeyboardButton('19:00')
btnHour20 = KeyboardButton('20:00')
btnHour21 = KeyboardButton('21:00')
btnHour22 = KeyboardButton('22:00')
btnHour23 = KeyboardButton('23:00')
btnHour24 = KeyboardButton('24:00')


#  ---4 condition passenger----
btnPeople1 = KeyboardButton("1ta odam ")
btnPeople2 = KeyboardButton("2ta odam")
btnPeople3 = KeyboardButton("3ta odam")
btnPeople4 = KeyboardButton("4ta odam")

#  ---5 condition passenger----
btnPhone = KeyboardButton('Raqamingizni kiritng',request_contact=True)
# btnLocation = KeyboardButton("Turgan joyingizni kiriting",request_location=True)


#  ---6 condition return order passenger----
btnOrder = KeyboardButton('Bekor qilish')

#  ---admin----
PassengerAdmin = KeyboardButton('Passenger')
DriveAdmin = KeyboardButton('Drive')
SetAdmin = KeyboardButton('Set')


#  ---Main Menu----
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrive,btnPassenger)

#  ---Menu Drive----
DriveCarMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCar)
DrivePeopleMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMan)
DriveTrueMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTrue,btnFalse)


#  ---Menu Passenger----
ABPassengerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnA,btnB)

#  ---day Menu----
DayPassengerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnToday,btnTomorrow,btnIndinga)
#  ---hour Menu----
HourPassengerMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHour1,btnHour2,btnHour3,btnHour4,btnHour5,btnHour6,btnHour7,btnHour8,btnHour9,btnHour10,btnHour11,btnHour12,btnHour13,btnHour14,btnHour15,btnHour16,btnHour17,btnHour18,btnHour19,btnHour20,btnHour21,btnHour22,btnHour23,btnHour24)
#  ---Number of People----
PeopleMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPeople1,btnPeople2,btnPeople3,btnPeople4)


#  ---General----
PhoneMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPhone)
# LocationMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnLocation)
OrderMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOrder)


#  ---Admin Menu----
AdminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(PassengerAdmin,DriveAdmin,SetAdmin)
