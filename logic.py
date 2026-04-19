from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, hp, power):


        self.pokemon_trainer = pokemon_trainer  

         
        self.hp = randint(400, 500)
        self.power = randint(50, 100)

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()   
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self



        

    

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][self.pokemon_number]['name'])
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
        

    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покеомона: {self.name}
сила покемона: {self.power}
хп покемона: {self.hp}'''

    # Метод класса для получения картинки покемона
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
    
    
class Wizard(Pokemon):
    def attack(self, enemy):
        super_attack = randint(50, 120)
        self.power += super_attack
        res = super().attack(enemy)
        self.power -= super_attack
        return res + f"\nБоец применил супер-атаку силой:{super_attack}"            
    
    if isinstance(enemy, Wizard): 
        shans = randint(1,5)
        if shans == 1:
            return 'Покемон-волшебник применил щит в сражении'
    
    def info(self):
        parent_info = super().info()
        return f"У тебя покемон-волшебник\n{parent_info}"
