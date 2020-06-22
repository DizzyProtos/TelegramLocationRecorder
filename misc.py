import telebot
import constants
from Services.GoogleSheetService import GoogleSheetService
from Services.OSMapService import OSMapService

bot = telebot.AsyncTeleBot(constants.telegram_token)
db_service = GoogleSheetService()
map_service = OSMapService()
