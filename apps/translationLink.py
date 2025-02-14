from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def getTranslateLink(answer):
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text='Перевод',
                url=f"https://translate.google.ru/?sl=en&tl=ru&text={answer}&op=translate")
        ]]
    )
