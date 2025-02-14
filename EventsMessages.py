from apps import citation, translationLink as trans
import keyboards as kb

# обработка текстовых сообщений

links = """/cit - Случайная цитата
/wb - склад WB (приемка)
/ost - Остатки по товарам (ost463)
/game - игра 'Угадай число
/love - I love You'"""


async def getMessage(message):
    print('---message.text', message.text)

    if message.text == '777':
        return await message.answer(text='Кнопки', reply_markup=kb.keyboard)
    if message.text == '✅ Цитата':
        answer = citation.nextCitation()
        return await message.answer(answer, reply_markup=trans.getTranslateLink(answer))
    return message.send_copy(chat_id=message.chat.id)
