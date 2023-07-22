from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='6393228976:AAEyUaw8YWw8W2vjmIJ-4OTvWgNEnSJw9k0', parse_mode='html') 

faker = Faker() 

card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
    types.KeyboardButton(text='Maestro'),
)

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет!!! Я умею генерировать тестовые банковские карты\nВыбери тип карты:', 
        reply_markup=card_type_keybaord,
    )

@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return

    card_number = faker.credit_card_number(card_type)
    card_expire = faker.credit_card_expire()
    card_security_code = faker.credit_card_security_code()

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\nНомер карты: {card_number}\nСрок действия: {card_expire}\nCVV/CVC: {card_security_code}'
    )

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()