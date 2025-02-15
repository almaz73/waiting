from apps import citation, translationLink as trans
import keyboards as kb
from apps import wb_free
import env

# обработка текстовых сообщений

links = """/cit - Случайная цитата
/wb - склад WB (приемка)
/ost - Остатки по товарам (ost463)
/game - игра 'Угадай число
/love - I love You'"""


async def get_message(message):
    print('---message.text', message.text)


    if message.text == 'web':
        return await message.answer(text='САЙТ', reply_markup=kb.keySite)
    if message.text == '☸ Wildberries':
        key = env.WB_KEY  # Пока ключ берем зашитый в код
        await message.answer('<b>Прогноз на 14 дней</b>:\n\n'+wb_free.getWB(key), parse_mode='HTML')
        return await  message.answer('Настройки WB', reply_markup=kb.wb_setting)
    if message.text == '/love': return await message.answer(kb.iloveYou)
    if message.text == '✅ Цитата':
        answer = citation.nextCitation()
        return await message.answer(answer, reply_markup=trans.getTranslateLink(answer))
    return message.send_copy(chat_id=message.chat.id)
