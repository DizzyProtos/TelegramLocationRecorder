from misc import bot, db_service
from Models.Locations import LocationCreateModel, LocationUpdateModel
import constants


@bot.message_handler(content_types=['location', 'text'])
def location_handler(message):
    if message.location is not None:
        bot.send_message(message.chat.id, "Hold tight, I'm recording your location")
        new_location = LocationCreateModel(
            chat_link=constants.telegram_base_link + str(message.chat.username),
            lat=message.location.latitude,
            long=message.location.longitude
        )
        responce = db_service.add_new_location(new_location)
        if responce.is_succesful:
            start_second_step(message)
        else:
            bot.send_message(message.chat.id, "Sorry, something went wrong. Please try again.")
    else:
        bot.send_message(message.chat.id,
                         "Sorry I don't see a geolocation, it's okay if you don't want to share it tho.")


def start_second_step(message):
    bot.send_message(message.chat.id, "Leave a comment about this place. Type 'no' if you don't want to.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, comment_handler)


def comment_handler(message):
    if message.text.lower() == 'no':
        restart_process(message)
        return

    bot.send_message(message.chat.id, "Please wait a while, I'm recording your comment.")
    is_recorded = db_service.add_comment_for_last_location(LocationUpdateModel(
        chat_link=constants.telegram_base_link+message.chat.username,
        comment=str(message.text)
    ))
    if is_recorded:
        restart_process(message)
    else:
        bot.send_message(message.chat.id, "Sorry, can't record your comment, please try again.")


def restart_process(message):
    bot.send_message(message.chat.id, "Thanks for your contribution! You can send another location to record.")
    bot.register_next_step_handler_by_chat_id(message.chat.id, location_handler)
