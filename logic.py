from random import randint
import requests
from datetime import datetime, timedelta   

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer  

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()   
        self.name = self.get_name()

        self.power = randint(50, 100)
        self.hp = randint(400, 500)

        self.last_feed_time = datetime.now()  
        Pokemon.pokemons[pokemon_trainer] = self

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return None

   
    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)

        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time
            return f"Следующее время кормления покемона: {next_feed_time}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard): 
            shans = randint(1,5)
            if shans == 1:
                self.hp += 30
                return 'Покемон-волшебник применил щит в сражении, и элексир с hp+30'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    def info(self):
        return f'''Имя твоего покеомона: {self.name}
сила покемона: {self.power}
хп покемона: {self.hp}'''

    def show_img(self):
        return self.img
    

class Fighter(Pokemon):
    def attack(self, enemy):
        super_attack = randint(50, 120)
        self.power += super_attack
        res = super().attack(enemy)
        self.power -= super_attack
        return res + f"\nБоец применил супер-атаку силой:{super_attack}"
    
    def info(self):
        parent_info = super().info()
        return f"У тебя покемон-боец\n{parent_info}"

   
    def feed(self):
        return super().feed(feed_interval=10, hp_increase=10)
    
    
class Wizard(Pokemon):
    def attack(self, enemy):
        super_attack = randint(50, 120)
        self.power += super_attack
        res = super().attack(enemy)
        self.power -= super_attack
        return res + f"\nВолшебник применил супер-атаку силой:{super_attack}"            
    
    def info(self):
        parent_info = super().info()
        return f"У тебя покемон-волшебник\n{parent_info}"

    
    def feed(self):
        return super().feed(feed_interval=20, hp_increase=20)
