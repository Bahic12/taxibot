import sqlite3

people = []
# conn = sqlite3.connect('../sqlite.db')
# conn.execute("""CREATE TABLE COMPANY(
#     ID,
#     TURI,
#     ADDRESS,
#     DAY,
#     HOUR,
#     PEOPLE,
#     DAYN,
#     PHONE_NUMBER,
#     NAME)
#     """)
#
# if __name__=='__main__':
#     pass
# if people:
#     if len(people) >= 1:
#         # b = numpy.array(people)
#         a = choice(people)
#         if len(a) >= 5:
#             a = a
#         else:
#             a = choice(people)
#
#         i.append(a[0])
#         if i[2] == 'Ertaga' and i[-1] != datetime.datetime.now().strftime('%d'):
#             i[2] = 'Bugun'
#         if i[2] == 'Indinga' and i[-1] != datetime.datetime.now().strftime('%d'):
#             i[2] = 'Ertaga'
#         await bot.send_message(message.from_user.id,
#                                f"Boriladigan joy: {a[2]}\nKuni: {a[3]}\nVaqti: {a[4]}\nOdam soni: {a[5]}\nMobil raqam: {a[6]}",
#                                reply_markup=DriveTrueMenu)
#     else:
#         if people[0] == 6:
#             b = people[0]
#         await bot.send_message(message.from_user.id,
#                                f"Boriladigan joy: {b[2]}\nKuni: {b[3]}\nVaqti: {b[4]}\nOdam soni: {b[5]}\nMobil raqam: {b[6]}")
#         i.append(b[0])
#     if people[1] == 6:
#         b = people[1]
#         await bot.send_message(message.from_user.id,
#                                f"Boriladigan joy: {b[2]}\nKuni: {b[3]}\nVaqti: {b[4]}\nOdam soni: {b[5]}\nMobil raqam: {b[6]}")
#         i.append(b[0])
# else:
#     await bot.send_message(message.from_user.id, 'hozirda odam mavjud emas')