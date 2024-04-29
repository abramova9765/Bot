import logging
from aiogram import Bot, Dispatcher, types, executor
from dataclasses import dataclass
from typing import List
from aiogram.types import LabeledPrice


API_TOKEN = '6044931296:AAE6_HXcw4UhinHvg0G6EOgU0r77t7yJ6Rw'
PROVIDER_TOKEN = '381764678:TEST:83896'
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dataclass
class Item:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    max_tip_amount: int = None
    provider_token: str = PROVIDER_TOKEN

    def generate_invoices(self):
        return self.__dict__


Portal = Item(

    title='Игра в жанре action Portal',
    description='Portal — однопользовательский шутер-головоломка от первого лица.Игра состоит из серии головоломок, которые должны быть решены при помощи телепортации игрока и других простых объектов с помощью портальной пушки. Целью каждого уровня является достижение точки выхода, представленной круглым лифтом. "Портальная пушка" и необычная физика создают акценты в этой игре.',
    start_parameter='Portal',
    currency='RUB',
    prices=[LabeledPrice(label='Portal', amount=400_00),
            LabeledPrice(label='Доставка', amount=300_00)],
    photo_url='https://i.pinimg.com/originals/57/4b/5d/574b5de1ec051ca72db2b16579660a15.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000

)

NeonWhite = Item(

    title='Игра в жанре action Neon White',
    description='Neon White – это сверхдинамичный экшн-платформер от первого лица, действие которого происходит за жемчужными вратами Рая.',
    start_parameter='NeonWhite',
    currency='RUB',
    prices=[LabeledPrice(label='Neon White', amount=775_00),
            LabeledPrice(label='Доставка', amount=450_00)],
    photo_url='https://gamebomb.ru/files/galleries/001/c/c1/409096.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000

)


Fortnite = Item(

    title='Игра в жанре mmo Fortnite',
    description='Собирайте друзей и отправляйтесь в игру Fortnite от Epic Games, в которой вас ждёт грандиозная битва для 100 игроков. В ней вам предстоит искать полезную добычу, добывать материалы, создавать предметы и отстреливаться от врагов.',
    start_parameter='Fortnite',
    currency='RUB',
    prices=[LabeledPrice(label='Fortnite', amount=500_00),
            LabeledPrice(label='Доставка', amount=200_00)],
    photo_url='https://catherineasquithgallery.com/uploads/posts/2021-02/1613247637_115-p-skachat-sinii-fon-fortnait-149.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000
)


Minecraft = Item(

    title='Игра в жанре mmo Minecraft',
    description='Minecraft - это компьютерная игра с бесконечными мирами, созданными из блоков, где нужно строить и выживать. Главный герой игры - Стив, именно им управляет игрок. Он попадает в мир, где ничего нет. Задача Стива построить себе жилище и собрать необходимые для жизни ресурсы, либо отвоевать их у других',
    start_parameter='Minecraft',
    currency='RUB',
    prices=[LabeledPrice(label='Minecraft', amount=680_00),
            LabeledPrice(label='Доставка', amount=250_00)],
    photo_url='https://wallpaper-house.com/data/out/7/wallpaper2you_175629.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000

)

Genshin = Item(

    title='Игра в жанре rpg Genshin Impact',
    description='Вас ждёт захватывающее однопользовательское приключение, где вы станете гостем из другого мира в поисках потерянного родного человека. Разгадайте тайны Тейвата и самого себя',
    start_parameter='GenshinImpact',
    currency='RUB',
    prices=[LabeledPrice(label='Genshin Impact', amount=400_00),
            LabeledPrice(label='Доставка', amount=300_00)],
    photo_url='https://pic.rutubelist.ru/video/e7/82/e782517acd07284abf3a80f869b99d12.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000

)

Undertale = Item(

    title='Игра в жанре rpg Undertale',
    description='Игрок управляет ребенком, который упал в Подземелье: большую уединенную область под поверхностью Земли, отделенную магическим барьером. Игрок встречает различных монстров во время возвращения на поверхность, хотя некоторые монстры могут вступить с игроком в бой. ',
    start_parameter='Undertale',
    currency='RUB',
    prices=[LabeledPrice(label='Undertale', amount=380_00),
            LabeledPrice(label='Доставка', amount=350_00)],
    photo_url='http://pm1.narvii.com/7179/f9126613f0ef4d104026683f202b0a6a27b74bd1r1-968-825v2_uhq.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True,
    max_tip_amount=100000

)


POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Обычная коробка', 0
        ),
        types.LabeledPrice(
            'Почтой', 500_00
        ),
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Ускоренная почта',
    prices=[
        types.LabeledPrice(
            'Подарочная упаковка', 200_00
        ),
        types.LabeledPrice(
            'Ускоренная доставка', 1000_00
        ),
    ]
)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте!")


@dp.message_handler(commands=['about'])
async def send_welcome(message: types.Message):
    await message.reply("Данный бот умеет продавать игры различных жаров")


@dp.message_handler(commands='action')
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **Portal.generate_invoices(), payload='12345')
    await bot.send_invoice(message.from_user.id, **NeonWhite.generate_invoices(), payload='12345')


@dp.message_handler(commands='mmo')
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **Minecraft.generate_invoices(), payload='12345')
    await bot.send_invoice(message.from_user.id, **Fortnite.generate_invoices(), payload='12345')


@dp.message_handler(commands='rpg')
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **Genshin.generate_invoices(), payload='12345')
    await bot.send_invoice(message.from_user.id, **Undertale.generate_invoices(), payload='12345')


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == 'RU':
        await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[POST_REGULAR_SHIPPING,
                                                                                      POST_FAST_SHIPPING],
        ok=True)

    elif query.shipping_address.country_code == 'US':
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False,

                                        error_message='Сюда не доставляем')


@dp.pre_checkout_query_handler()
async def pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    await bot.send_message(chat_id=query.from_user.id,
                           text='Спасибо за покупку!')

''' для тестовой оплаты: 1111 1111 1111 1026
12/22 000
'''

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)