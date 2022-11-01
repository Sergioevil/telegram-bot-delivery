from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn11 = InlineKeyboardButton('Выбрать товар', callback_data='choose art')
keyboard1 = InlineKeyboardMarkup().row(btn11)

btn21 = InlineKeyboardButton('Да, это он', callback_data='info')
btn22 = InlineKeyboardButton('Изменить', callback_data='choose art')
keyboard2 = InlineKeyboardMarkup().row(btn21).row(btn22)

keyboard22 = InlineKeyboardMarkup().row(btn22)

btn31 = InlineKeyboardButton('Купить', callback_data='buy')
btn32 = InlineKeyboardButton('Задать вопрос',  url='https://t.me/jojobaa')
btn33 = InlineKeyboardButton('Отменить', callback_data='choose art')
keyboard3 = InlineKeyboardMarkup().row(btn31).row(btn32).row(btn33)

btn41 = InlineKeyboardButton('Связатьcя с менеджером', url='https://t.me/jojobaa')
btn42 = InlineKeyboardButton('Назад', callback_data='info')
keyboard4 = InlineKeyboardMarkup().row(btn41).row(btn42)

btn51 = InlineKeyboardButton('Назад', callback_data='choose art')
keyboard5 = InlineKeyboardMarkup().row(btn51)

btn61 = InlineKeyboardButton('Оплатить', callback_data='pay')
keyboard6 = InlineKeyboardMarkup().row(btn61)

btn71 = InlineKeyboardButton('Хорошо', callback_data='info_after_pay')
keyboard7 = InlineKeyboardMarkup().row(btn71)

btn81 = InlineKeyboardButton('Узнать статус', callback_data='status')
keyboard8 = InlineKeyboardMarkup().row(btn81)

btn91 = InlineKeyboardButton('Связаться с менеджером', url='https://t.me/jojobaa')
keyboard9 = InlineKeyboardMarkup().row(btn91)

btn101 = InlineKeyboardButton('Узнать статус', url='https://t.me/jojobaa')
keyboard10 = InlineKeyboardMarkup().row(btn101)

btn111 = InlineKeyboardButton('Назад', callback_data='buy')
keyboard11 = InlineKeyboardMarkup().row(btn41).row(btn111)