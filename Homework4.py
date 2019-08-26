import random


# Task 1
def calculate_ending(age):
    last_number = age % 10
    if last_number == 1:
        return "год"
    elif last_number in range(2, 5):
        return "года"
    elif last_number in range(5, 10) or last_number == 0:
        return "лет"


def print_person_info(name="Неизвестный", age=0, city="Неизвестном"):
    ageStr = str(age)
    if int(ageStr) == 0:
        ageStr = "неизвестного"

    return f'"{name}, {ageStr} {calculate_ending(age)}, проживает в городе {city}"'


print(print_person_info())
print(print_person_info("Петя", 25, "Питер"))
print(print_person_info("Петя", 30, "Питер"))
print(print_person_info("Петя", 21, "Питер"))
print(print_person_info("Петя", 22, "Питер"))
print(print_person_info("Петя", 24, "Питер"))
print(print_person_info("Петя", 29, "Питер"))


# Task 2

def find_max_number(*args):
    max_number = None
    for i in args:
        if max_number is None:
            max_number = i
        if max_number < i:
            max_number = i
    return max_number


print(find_max_number(1000, 1, 5, 50, 25, -70, 100))

# Task 3 / 4

name = input("Enter player's name:\n")
amount_of_porridge_eaten = input("Have you eaten much porridge today? (yes, no, so-so)\n")


def calculate_damage():
    if amount_of_porridge_eaten == "yes":
        return 100
    elif amount_of_porridge_eaten == "so-so":
        return 50
    elif amount_of_porridge_eaten == "no":
        return 25
    else:
        return 10


def calculate_damage_done(damage, armor):
    return damage / armor


def random_int_from_range(range_var: range):
    return random.randint(range_var.start, range_var.stop)


player = {
    "name": name,
    "health": 100,
    "damage": calculate_damage(),
    "armor": 1.2
}

enemy_names = ("Godzilla", "Shredder", "Shao Kahn")
enemy_damage = [range(70, 100), range(25, 50), range(50, 70)]

enemy = {
    "name": enemy_names[random.randint(0, 2)],
    "health": 100,
    "damage": random_int_from_range(enemy_damage[random.randint(0, 2)]),
    "armor": 1.2
}


def announce_fighters():
    player_name = player.get("name")
    enemy_name = enemy.get("name")
    print("This is Python Combat")
    print(f"Epic battle: {player_name} VS {enemy_name}")
    print("Let the fight begin!")


announce_fighters()


def attack(attacker: dict, victim: dict):
    victim_armor = victim.get("armor")
    attacker_name = attacker.__getitem__("name")
    victim_name = victim.__getitem__("name")
    attacker_damage = int(calculate_damage_done(attacker.__getitem__("damage"), victim_armor))
    victim_health = victim.__getitem__("health")
    victim.__setitem__("health", victim_health - attacker_damage)
    victim_health = victim.__getitem__("health")
    print(f"{attacker_name} attacks(-{attacker_damage} DMG) {victim_name} ({victim_health} HP left) ")
    if victim_health <= 0:
        print(f"{victim_name} has been crushed")
        return True
    else:
        return False


while True:
    result = attack(player, enemy)
    if result:
        break
    result = attack(enemy, player)
    if result:
        break
