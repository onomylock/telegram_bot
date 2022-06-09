import telebot
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

bot = telebot.TeleBot("5392736163:AAH3-blM8aop1SDFwk_HEtxQGW77miIk40k")


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(content_types=["photo"])
def handle_docs_document(message):
    chatID = message.chat.id
    raw = message.photo[2].file_id
    name = raw+".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = open(name, 'rb')

    text = pytesseract.image_to_string(
        Image.open(img), lang="rus")

    bot.send_message(chatID, text.strip())
    bot.send_message(chatID, "Маслину поймал!")


bot.polling(none_stop=True, interval=0)
