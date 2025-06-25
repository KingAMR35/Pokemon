import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())

    else:
        bot.reply_to(message, "Ты уже создал себе покемона.")



@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        level = 1
        feed = 1
        feed += 1
        bot.send_message(message.chat.id, "Вы покормили покемона")
    else:
        bot.send_message(message.chat.id, "Ты еще не создал себе покемона")
        
    if feed == 2:
        level = 2
        bot.send_message(message.chat.id, "Вы повысили уровень покемона")
        
        
        
@bot.message_handler(commands=['info'])
def pokemons(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.game_index)
        bot.send_message(message.chat.id, pokemon.game_abilities)
    else:
        bot.send_message(message.chat.id, "Ты еще не создал себе покемона")
        
        
        
        


bot.infinity_polling(none_stop=True)

