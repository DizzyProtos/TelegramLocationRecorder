from telebot import types


# todo: Fix "Send my location" button
def get_location_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_geo = types.KeyboardButton(text="Send my location", request_location=True)
    keyboard.add(button_geo)
    return keyboard
