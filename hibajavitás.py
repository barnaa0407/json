import json

with open('rpg_characters.json', 'r') as file:
    data = json.load(file)  # json.loads() helyett json.load() kell

class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name  # helyes elnevezés
        self.level = level  # helyes elnevezés
        self.health = health  # helyes elnevezés
        self.attack = attack  # helyes elnevezés
        self.defense = defense  # helyes elnevezés

    def take_damage(self, damage):
        self.health -= damage * 2  # helyes metódusnév
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and now has {self.health} health left.")

# A JSON-ból való karakterek betöltése
characters = [Character(**char) for char in data['characters']]

def fight(character1, character2):
    print(f"Battle between {character1.name} and {character2.name} starts!")
    while character1.health > 0 and character2.health > 0:
        damage = max(0, character1.attack - character2.defense)  # ne legyen negatív kár
        character2.take_damage(damage)

        if character2.health <= 0:
            print(f"{character2.name} is defeated! {character1.name} wins!")
            break

        damage = max(0, character2.attack - character1.defense)  # ne legyen negatív kár
        character1.take_damage(damage)

        if character1.health <= 0:
            print(f"{character1.name} is defeated! {character2.name} wins!")
            break

# Harc indítása
fight(characters[0], characters[1])