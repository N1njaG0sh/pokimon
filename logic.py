import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


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


@bot.message_handler(commands=['hpp'])
def restore_pokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        
        # Восстанавливаем здоровье и силу
        old_hp = pokemon.hp
        old_power = pokemon.power
        
        pokemon.hp = randint(400, 500)
        pokemon.power = randint(50, 100)
        
        bot.send_message(message.chat.id, 
                        f"Покемон восстановлен!\n"
                        f"Было: {old_hp} HP | {old_power} силы\n"
                        f"Стало: {pokemon.hp} HP |  {pokemon.power} силы")
    else: 
        bot.send_message(message.chat.id, "Сначала создай покемкомандой /go")


bot.infinity_polling(none_stop=True)
