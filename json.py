import json
import random

# 1. JSON fájl betöltése
def load_characters_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# 2. Character osztály
class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} received {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Level {self.level}) - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

# 3. Harci logika
def fight(character1, character2):
    print(f"\n{character1} vs {character2}")
    
    while character1.is_alive() and character2.is_alive():
        # Attack character2
        damage_to_2 = max(0, character1.attack - character2.defense)
        character2.take_damage(damage_to_2)
        
        if not character2.is_alive():
            print(f"{character1.name} wins!")
            break
        
        # Attack character1
        damage_to_1 = max(0, character2.attack - character1.defense)
        character1.take_damage(damage_to_1)

        if not character1.is_alive():
            print(f"{character2.name} wins!")
            break

# 4. Szimuláljuk a harcot két karakter között
def simulate_fight():
    # Töltsük be a karaktereket JSON-ból
    characters = load_characters_from_json('characters.json')
    
    # Készítsünk karakter objektumokat
    character_objects = []
    for char in characters:
        character = Character(char['name'], char['level'], char['health'], char['attack'], char['defense'])
        character_objects.append(character)
    
    # Válasszunk két karaktert
    char1, char2 = random.sample(character_objects, 2)
    
    # Szimuláljuk a harcot
    fight(char1, char2)

# Fő program futtatása
if __name__ == "__main__":
    simulate_fight()
    