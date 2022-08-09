import config
import telebot

bot = telebot.TeleBot(config.token)

# Функция шифрования текста
def soso(text):
    glasnye_zaglavnye: str = "АУОИЭЫЯЮЕЁ"
    glasnye_strochnye: str = "ауоиэыяюеё"
    result: str = ""
    for letter in text:
        # если встретится заглавная гласная то мы запишем в новую строку заглавную потом  букву с а потом строчную гласную
        if letter in glasnye_zaglavnye:
            result = result + letter + 'с' + letter.lower()
        # а если встретится строчная то запишем в новую строку строчную добавим с и добавим опять такую же гласную
        elif letter in glasnye_strochnye:
            result = result + letter + 'с' + letter
        # иначе добавляем в результат все остальные значения которые встретили в введенной строке
        else:
            result = result + letter

    return result

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь на русском языке, я зашифрую :)')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, soso(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
