import telebot
import constants
from Services.GoogleSheetService import GoogleSheetService

bot = telebot.AsyncTeleBot(constants.telegram_token)
db_service = GoogleSheetService()
