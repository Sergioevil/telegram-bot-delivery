from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ParseMode, ContentType
from aiogram import Bot, types
import re
import config
import buttons
import all_requests

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
PAYMENTS_PROVIDER_TOKEN = config.PAYMENTS_PROVIDER_TOKEN

keyboard1 = buttons.keyboard1
keyboard2 = buttons.keyboard2
keyboard3 = buttons.keyboard3
keyboard4 = buttons.keyboard4
keyboard5 = buttons.keyboard5
keyboard6 = buttons.keyboard6
keyboard7 = buttons.keyboard7
keyboard8 = buttons.keyboard8
keyboard9 = buttons.keyboard9
keyboard10 = buttons.keyboard10
keyboard11 = buttons.keyboard11
keyboard22 = buttons.keyboard22

address = 0
articul = 0
text_of_good = ''

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    global address, articul, text_of_good
    await bot.send_message(msg.from_user.id, "Здравствуйте, этот бот поможет Вам оформить доставку на любой товар из интернет-магазина \"SixStuffs\"", reply_markup=keyboard1)
    address = 0
    articul = 0
    text_of_good = ''



@dp.callback_query_handler(lambda c: c.data == 'choose art')
async def start1(msg: types.CallbackQuery):
    global articul
    articul = 1
    await bot.send_message(msg.from_user.id, "Введите артикул товара")


@dp.message_handler()
async def start1(msg: types.Message):
    global articul, address
    if articul == 1:
        if re.search(r"^\d{6,10}$", msg.text):
            global text_of_good
            text_of_good = all_requests.get_item_text(msg.text)
            if text_of_good:
                await bot.send_message(msg.from_user.id, text_of_good.get('text'), reply_markup=keyboard2, parse_mode=ParseMode.MARKDOWN)
                articul = 0
            else:
                await bot.send_message(msg.from_user.id, 'Товар не найден\nПроверьте верность введенных данных и напишите снова')
        else:
            await bot.send_message(msg.from_user.id, 'Артикул должен содержать в себе от 6 до 10 цифр')
        return

    if address == 1:
        adresses = all_requests.check_address(msg.text)
        if len(adresses) > 0:
            keyboard_adresses = InlineKeyboardMarkup()
            for but_name in adresses:
                keyboard_adresses.add(InlineKeyboardButton(but_name, callback_data='confirm'))
            await bot.send_message(msg.from_user.id, 'Выберите адрес:', reply_markup=keyboard_adresses)
        else:
            await bot.send_message(msg.from_user.id, 'К сожалению, на данный адрес доставка невозможна, напишите другой', reply_markup=keyboard4)
    else:
        await bot.send_message(msg.from_user.id, 'Что-то пошло не так, перезапустите бота /start')


@dp.callback_query_handler(lambda c: c.data == 'confirm')
async def start1(msg: types.CallbackQuery):
    global address
    if text_of_good:
        await bot.send_message(msg.from_user.id, 'Заказ принят!', reply_markup=keyboard6)
        address = 0
    else:
        await bot.send_message(msg.from_user.id, 'Что-то пошло не так, перезапустите бота /start')


@dp.callback_query_handler(lambda c: c.data == 'info')
async def start1(msg: types.CallbackQuery):
    global text_of_good
    await bot.send_message(msg.from_user.id, f"""Стоимость доставки:100₽
Итого при получении: {text_of_good.get('price')+100}₽""", reply_markup=keyboard3)



@dp.callback_query_handler(lambda c: c.data == 'buy')
async def start1(msg: types.CallbackQuery):
    global address
    address = 1
    await bot.send_message(msg.from_user.id, f'''{msg.from_user.first_name}, укажите Ваш адрес
(город, улица, дом, квартира)''')



@dp.callback_query_handler(lambda c: c.data == 'pay')
async def process_buy_command(msg: types.CallbackQuery):
    global text_of_good
    if text_of_good:
        if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
            PRICE = types.LabeledPrice(label='SixDeliveries', amount=(text_of_good.get('price')+100)*100)
            await bot.send_invoice(
                msg.from_user.id,
                title='Доставка',
                description='Доставка товара',
                provider_token=PAYMENTS_PROVIDER_TOKEN,
                currency='rub',
                prices=[PRICE],
                start_parameter='payment-example',
                payload='some-invoice-payload-for-our-internal-use'
            )
    else:
        await bot.send_message(msg.from_user.id, 'Что-то пошло не так, перезапустите бота /start')

@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    global text_of_good
    pmnt = message.successful_payment.to_python()
    await bot.send_message(message.from_user.id, f'''Заказ успешно оплачен!
Спасибо за покупку)''', reply_markup=keyboard10)
    text_of_good = ''


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)






