from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.index = self.game_index()
        self.abilities = self.game_abilities()
        self.hp = randint(200, 400)
        self.power = randint(30, 60)
        self.level = 1
        self.experience = 0
        self.feed_count = 0
        self.achievements = []

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def game_index(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['game_indices'][0]['game_index'])
        else:
            return "Pikachu"

    def game_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]['ability'])
        else:
            return "Pikachu"
    def feed(self):
        self.feed_count += 1
        self.gain_experience(10)
        print(f"{self.name} съел еду!")

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= 100 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= 100 * (self.level - 1)
        achievement_title = f"Уровень {self.level} достигнут"
        achievement_description = f"{self.name} достиг нового уровня!"
        new_achievement = Achievement(achievement_title, achievement_description)
        self.achievements.append(new_achievement)
        print(f"{self.name} теперь уровня {self.level}.")

    def achievements_list(self):
        return "\n".join([f"- {a.title}: {a.description}" for a in self.achievements])

    def feed_info_1(self):
        return (
            f"Имя: {self.name}\n"
            f"Уровень: {self.level}\n"
            f"Опыт: {self.experience}/{100*self.level}\n"
            f"Кормлений: {self.feed_count}\n"
            f"Достижения:\n{self.achievements_list()}"
        )

    # Метод класса для получения информации
    def info(self):
        pokemon_data = (
            f"Имя твоего покемона: {self.name}\n"
            f"Сила покемона: {self.power}\n"
            f"Здоровье покемона: {self.hp}\n"
            f"Индекс твоего покемона: {self.index}\n"
            f"Способность твоего покемона: {self.abilities}"
        )
        return pokemon_data

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_index(self):
        return f"Индекс твоего покемона: {self.index}"
    
    def show_abilities(self):
        return f"Способность твоего покемона: {self.abilities}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard): #если enemy - объект класса Wizard, то True, иначе False
            chance = randint(1,5)
            if chance == 3: 
                return "Покемон волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}'
        else:
            enemy.hp = 0
            return f'Покемон @{self.pokemon_trainer} победил в сражении @{enemy.pokemon_trainer}'
class Wizard(Pokemon):
    pass
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(2, 10)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'\nБоец применил супер-атаку силой {super_power}'
                
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
class Achievement:
    def __init__(self, title, description):
        self.title = title
        self.description = description