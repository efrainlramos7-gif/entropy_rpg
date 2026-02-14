import random # For random number generation
import time # For simulating time delays


class Mage:# A simple mage class to demonstrate entropy-based spellcasting
    def __init__(self, name):# Instance data for each mage
        self.name = name# Unique name for the mage
        self.entropy = 0# Starting entropy level
        self.spells = {# Available spells and their entropy costs
            "Fireball": 20,# Spell name and cost
            "Heal": 15,# Spell name and cost
            "Lightning": 25,# Spell name and cost
            "Shield": 10# Spell name and cost
        }
        self.history = []# To log spellcasting history


    def generate_entropy(self):# Simulate generating entropy through random events
        amount = random.randint(5, 15)# Random amount of entropy generated
        self.entropy += amount# Update the mage's entropy level
        print(f"{self.name} gained {amount} entropy.")# Log the entropy gain
        return amount# Return the amount of entropy generated


    def cast_spell(self):# Cast a random spell if there is enough entropy
        spell = random.choice(list(self.spells.keys()))# Randomly select a spell to cast
        cost = self.spells[spell]# Get the cost of the selected spell

        if self.entropy >= cost:# Check if the mage has enough entropy to cast the spell
            self.entropy -= cost# Deduct the cost from the mage's entropy
            result = f"Cast {spell} (Cost: {cost})"# Log the successful spell cast
            print(result)# Log the successful spell cast
        else:# Not enough entropy to cast the spell
            result = f"Failed to cast {spell} (Not enough entropy)"# Log the failed spell cast
            print(result)# Log the failed spell cast

        self.history.append(result)# Save the result to history
        return result# Return the result of the spell cast


    def status(self):# Return the current status of the mage
        return f"Entropy: {self.entropy}"# Log the current entropy level of the mage


    def save_log(self):# Save the spellcasting history to a file
        with open("magic_log.txt", "a") as file:# Open the log file in append mode
            for entry in self.history:# Write each entry in the history to the file
                file.write(entry + "\n")# Write the entry to the file

        self.history.clear()# Clear the history after saving


def run_simulation():# Main function to run the mage simulation
    mage = Mage("Ziggie the Ascendant")# Create a mage instance

    print("Entropy Magic Simulator Started")# Log the start of the simulation
    print("-------------------------------")# Log a separator for clarity

    rounds = 10# Number of rounds to simulate

    for i in range(rounds):# Loop through the specified number of rounds
        print(f"\nRound {i + 1}")# Log the current round number

        mage.generate_entropy()# Generate entropy for the mage
        mage.cast_spell()# Attempt to cast a spell based on the current entropy level

        print(mage.status())# Log the current status of the mage after each round

        time.sleep(1)# Simulate a delay between rounds

    mage.save_log()# Save the spellcasting history to a log file at the end of the simulation
    print("\nSimulation Complete")# Log the completion of the simulation
    print("Results saved to magic_log.txt")# Log the location of the saved results


if __name__ == "__main__":# Run the simulation if this script is executed directly
    run_simulation()# Start the mage simulation
    import random
import time


class Mage:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.entropy = 0
        self.max_entropy = 50

        self.spells = {
            "Fireball": 20,
            "Heal": 15,
            "Lightning": 25,
            "Shield": 10
        }

        self.history = []


    def generate_entropy(self):
        amount = random.randint(8, 18)
        self.entropy += amount

        if self.entropy > self.max_entropy:
            self.entropy = self.max_entropy

        print(f"{self.name} gained {amount} entropy.")


    def cast_spell(self, enemy_hp):
        spell = random.choice(list(self.spells.keys()))
        cost = self.spells[spell]

        if self.entropy < cost:
            result = "Not enough entropy"
            print(result)
            return 0, result

        self.entropy -= cost

        damage = random.randint(10, 25) + (self.level * 2)

        result = f"Cast {spell} for {damage} damage"
        print(result)

        self.history.append(result)

        return damage, result


    def gain_exp(self, amount):
        self.exp += amount
        print(f"Gained {amount} EXP")

        if self.exp >= self.level * 50:
            self.level_up()


    def level_up(self):
        self.exp = 0
        self.level += 1
        self.max_entropy += 10

        print(f"LEVEL UP! Now Level {self.level}")

        if self.level == 3:
            self.spells["Meteor"] = 40
            print("Unlocked spell: Meteor")

        if self.level == 5:
            self.spells["Void Blast"] = 60
            print("Unlocked spell: Void Blast")


    def status(self):
        return f"Level: {self.level} | Entropy: {self.entropy}/{self.max_entropy}"


    def save_log(self):
        with open("magic_log.txt", "a") as file:
            for entry in self.history:
                file.write(entry + "\n")

        self.history.clear()



class Boss:
    def __init__(self, level):
        self.name = f"Entropy Beast Lv{level}"
        self.hp = 80 + (level * 30)
        self.attack = 10 + (level * 3)


    def attack_player(self):
        return random.randint(self.attack - 3, self.attack + 5)



def boss_fight(mage, boss):

    print("\nBOSS FIGHT!")
    print(f"{boss.name} Appears!")
    print(f"HP: {boss.hp}")

    while boss.hp > 0:

        mage.generate_entropy()

        damage, _ = mage.cast_spell(boss.hp)

        boss.hp -= damage

        if boss.hp <= 0:
            print("Boss Defeated!")
            mage.gain_exp(40 + mage.level * 10)
            return True


        enemy_damage = boss.attack_player()
        mage.entropy -= enemy_damage

        if mage.entropy < 0:
            mage.entropy = 0

        print(f"Boss hits you for {enemy_damage} entropy damage")
        print(mage.status())

        time.sleep(1)

    return True



def normal_round(mage):

    mage.generate_entropy()

    damage, _ = mage.cast_spell(0)

    mage.gain_exp(random.randint(5, 12))

    print(mage.status())



def run_game():

    mage = Mage("Ziggie the Ascendant")

    print("Entropy Mage RPG Started")
    print("-------------------------")

    rounds = 20

    for i in range(1, rounds + 1):

        print(f"\nRound {i}")

        if i % 5 == 0:
            boss = Boss(mage.level)
            boss_fight(mage, boss)
        else:
            normal_round(mage)

        time.sleep(1)


    mage.save_log()

    print("\nAdventure Complete")
    print("Log saved to magic_log.txt")



if __name__ == "__main__":
    run_game()
import random
import json
import time


# -------------------------------
# WORLD MAP
# -------------------------------

WORLD_MAP = {
    "Village": ["Forest"],
    "Forest": ["Village", "Ruins"],
    "Ruins": ["Forest", "Tower"],
    "Tower": ["Ruins"]
}


# -------------------------------
# ITEMS
# -------------------------------

ITEMS = {
    "Potion": {"heal": 20},
    "Elixir": {"heal": 50},
    "Entropy Crystal": {"entropy": 30}
}

WEAPONS = {
    "Staff": 5,
    "Sword": 7,
    "Void Blade": 12,
    "Chaos Relic": 20
}


# -------------------------------
# SKILL TREE
# -------------------------------

SKILLS = {
    "Mage": ["Fire Boost", "Mana Flow"],
    "Knight": ["Iron Skin", "Power Strike"],
    "Summoner": ["Spirit Bond", "Double Summon"]
}


# -------------------------------
# PLAYER
# -------------------------------

class Player:

    def __init__(self, name, job):

        self.name = name
        self.job = job

        self.level = 1
        self.exp = 0

        self.hp = 100
        self.max_hp = 100

        self.entropy = 30
        self.max_entropy = 30

        self.weapon = None

        self.inventory = ["Potion"]
        self.skills = []

        self.location = "Village"


    # -------------------

    def generate_entropy(self):

        gain = random.randint(5, 12)
        self.entropy += gain

        if self.entropy > self.max_entropy:
            self.entropy = self.max_entropy

        print(f"Entropy +{gain}")


    # -------------------

    def attack(self):

        base = random.randint(8, 15)

        weapon_bonus = 0

        if self.weapon:
            weapon_bonus = WEAPONS[self.weapon]

        skill_bonus = len(self.skills) * 2

        total = base + weapon_bonus + skill_bonus

        return total


    # -------------------

    def gain_exp(self, amount):

        self.exp += amount
        print(f"EXP +{amount}")

        if self.exp >= self.level * 40:
            self.level_up()


    # -------------------

    def level_up(self):

        self.level += 1
        self.exp = 0

        self.max_hp += 15
        self.max_entropy += 5

        self.hp = self.max_hp
        self.entropy = self.max_entropy

        print("LEVEL UP!")

        if self.level % 2 == 0:
            self.unlock_skill()


    # -------------------

    def unlock_skill(self):

        tree = SKILLS[self.job]

        for skill in tree:
            if skill not in self.skills:
                self.skills.append(skill)
                print(f"Unlocked skill: {skill}")
                return


    # -------------------

    def use_item(self, item):

        if item not in self.inventory:
            return

        data = ITEMS[item]

        if "heal" in data:
            self.hp += data["heal"]

        if "entropy" in data:
            self.entropy += data["entropy"]

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        if self.entropy > self.max_entropy:
            self.entropy = self.max_entropy

        self.inventory.remove(item)

        print(f"Used {item}")


    # -------------------

    def equip_weapon(self, weapon):

        if weapon in WEAPONS:
            self.weapon = weapon
            print(f"Equipped {weapon}")


    # -------------------

    def status(self):

        return f"{self.name} | {self.job} | Lv {self.level} | HP {self.hp}/{self.max_hp} | Ent {self.entropy}/{self.max_entropy} | {self.location}"


# -------------------------------
# ENEMY AI
# -------------------------------

class Enemy:

    def __init__(self, level):

        self.level = level

        self.hp = 50 + level * 15
        self.attack_power = 8 + level * 3

        self.mode = random.choice(["aggressive", "drain", "defensive"])


    # -------------------

    def attack(self, player):

        if self.mode == "aggressive":
            return self.attack_power + 5

        if self.mode == "drain":
            player.entropy -= 5
            return self.attack_power

        if self.mode == "defensive":
            self.hp += 3
            return self.attack_power - 2


# -------------------------------
# COMBAT SYSTEM
# -------------------------------

def battle(player):

    enemy = Enemy(player.level)

    print("\nEnemy Appears!")
    print(f"Mode: {enemy.mode}")

    while enemy.hp > 0 and player.hp > 0:

        player.generate_entropy()

        damage = player.attack()

        enemy.hp -= damage

        print(f"You deal {damage}")

        if enemy.hp <= 0:
            break


        enemy_damage = enemy.attack(player)

        player.hp -= enemy_damage

        print(f"Enemy hits {enemy_damage}")

        if player.hp <= 30 and "Potion" in player.inventory:
            player.use_item("Potion")

        time.sleep(1)


    if player.hp > 0:
        print("Victory!")
        player.gain_exp(25)
        loot(player)


    else:
        print("Defeated...")


# -------------------------------
# LOOT SYSTEM
# -------------------------------

def loot(player):

    reward = random.choice(["Potion", "Elixir", "Entropy Crystal", "Weapon"])

    if reward == "Weapon":
        weapon = random.choice(list(WEAPONS.keys()))
        player.equip_weapon(weapon)

    else:
        player.inventory.append(reward)
        print(f"Found {reward}")


# -------------------------------
# WORLD TRAVEL
# -------------------------------

def travel(player):

    places = WORLD_MAP[player.location]

    new_place = random.choice(places)

    player.location = new_place

    print(f"Traveled to {new_place}")


# -------------------------------
# SAVE / LOAD
# -------------------------------

def save_game(player):

    data = player.__dict__

    with open("save.json", "w") as file:
        json.dump(data, file)

    print("Game Saved")


def load_game():

    try:
        with open("save.json", "r") as file:
            data = json.load(file)

        p = Player(data["name"], data["job"])
        p.__dict__.update(data)

        print("Game Loaded")

        return p

    except:
        return None


# -------------------------------
# MAIN GAME
# -------------------------------

def create_character():

    name = "Ziggie"

    job = random.choice(["Mage", "Knight", "Summoner"])

    print(f"Class: {job}")

    return Player(name, job)



def game_loop():

    player = load_game()

    if not player:
        player = create_character()


    print("\nEntropy RPG Started\n")


    turns = 25


    for i in range(turns):

        print("\n-------------------")
        print(player.status())


        event = random.choice(["battle", "travel", "loot"])


        if event == "battle":
            battle(player)

        elif event == "travel":
            travel(player)

        else:
            loot(player)


        if i % 5 == 0:
            save_game(player)


        time.sleep(1)


    save_game(player)

    print("\nAdventure Complete")



if __name__ == "__main__":
    game_loop()

