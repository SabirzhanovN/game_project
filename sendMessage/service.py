import telepot

token = '5550023917:AAHS8uxMkS1i9ufPzOLVaXro-IP7-OOtzmA'
my_id = '1404363032'
telegramBot = telepot.Bot(token)


def send_message_bot(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")