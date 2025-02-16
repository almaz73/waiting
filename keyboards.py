from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo

startMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Цитата'),
            KeyboardButton(text='☸ Wildberries'),
            KeyboardButton(text='☸ САЙТ', web_app=WebAppInfo(url='https://fmap.ru/tg_wbFree/set.html'))
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Начальное меню'
)



iloveYou = """░░░░░░░░░░░░░░░░
▄▄▄░░░░▄▄▄░░░▄▄▄
██▀░░▄█████▄████
█░░░████████████
█░░░████████████
█░░░▀███████████
█▄░░░░▀█████████
████░░░░▀█████▀░
░░░░░░░░░░▀█▀░░░
░░░░░░░▄▄░░░░░░░
█░██▀▄█▀▀█▄░▀█░█
█▄█▀▄█░░░░█▄░█░█
░█░░██░░░░██░█░█
░█░░░█▄░░▄█░░█░█
███▄░░▀██▀░░░▀█▀
░░░░░░░░░░░░░░░░"""

# Создаем объекты инлайн-кнопок
bt1 = InlineKeyboardButton(text='262',callback_data='262')
bt2 = InlineKeyboardButton(text='382',callback_data='382')
bt3 = InlineKeyboardButton(text='463',callback_data='463')
bt4 = InlineKeyboardButton(text='542',callback_data='542')
bt5 = InlineKeyboardButton(text='567',callback_data='567')
bt6 = InlineKeyboardButton(text='755',callback_data='755')
leftover_buttons = InlineKeyboardMarkup(
    inline_keyboard=[[bt1, bt2, bt3, bt4, bt5, bt6]]
)


keySite = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[[InlineKeyboardButton(
        text='Сайт', web_app=WebAppInfo(url='https://fmap.ru/tg_wbFree/set.html')
    )]])
wb_setting = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[[InlineKeyboardButton(
        text='Остатки',
        callback_data='wb_leftovers'
    ),InlineKeyboardButton(
        text='Настройки WB',
        callback_data='wb_settings'
    )]])

keyboard222 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Open Mini App",
        web_app=WebAppInfo(url="https://fmap.ru/tg_wbFree/set.html")  # Укажите URL вашего Mini App
    )],
    [InlineKeyboardButton(
        text='Профиль',
        web_app=WebAppInfo(url='https://fmap.ru/tg_wbFree/set.html'))]

])