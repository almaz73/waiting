# обработка кнопок

import keyboards as kb

async def get_keyboard(callback):
    print(' -- callback.data', callback.data)


    if callback.data== 'wb_leftovers':
       return await callback.message.answer(text='Кнопки', reply_markup=kb.leftover_buttons)
    if callback.data== 'wb_settings':
        return await callback.message.answer(text='САЙТ', reply_markup=kb.keySite)
    return  await callback.message.edit_text( 'Неизвестная кнопка')

