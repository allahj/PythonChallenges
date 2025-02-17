import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        player_invulnerable = hasattr(opponent, 'invulnerable') and opponent.invulnerable
        attack_range = 1, self.attack_power
        min_attack, max_attack = attack_range
        attack_damage = random.randint(min_attack, max_attack)

        if player_invulnerable:
            print(f"{opponent.name} is invulnerable and will not be attacked! {opponent.name}'s current health: {opponent.health}/{opponent.max_health}")
            opponent.invulnerable = False
        else:
            opponent.health -= attack_damage

            if opponent.health <= 0:
                print(f'{opponent.name} has been defeated!')
            else:
                print(f"{self.name} attacked {opponent.name} with {attack_damage} attack damage. {opponent.name}'s current health: {opponent.health}/{opponent.max_health}")
                return attack_damage

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_range = 1, 30
        min_heal, max_heal = heal_range
        heal = random.randint(min_heal, max_heal)
        restored_health = heal + self.health

        if not restored_health > self.max_health:
            self.health  = restored_health
            print(f'{self.name} healed {heal} health! Current health: {self.health}')

# Warrir class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen_heal = 5
        regenerated_health = self.health + regen_heal

        if not regenerated_health > self.max_health:
            self.health += 5
            print(f"{self.name} regenerates {regen_heal} health! Current health: {self.health}/{self.max_health}")

# Create Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.invulnerable = False

    def quick_shot(self, opponent):
        arrow_attack = self.attack(opponent)

        if arrow_attack is not None:
            quick_shot_attack = arrow_attack
            double_damage_msg = f'Quick Shot has dealt double damage! The normal arrow attack was {arrow_attack} but Quit Shot dealt {arrow_attack * 2} damage!'
            opponent.health -= quick_shot_attack
            remaining_opponent_health_msg = f'{opponent.name} has {opponent.health}/{opponent.max_health} health.'
            damage_output_msg = f'{double_damage_msg} \n{remaining_opponent_health_msg}'
            print(damage_output_msg)

            if opponent.health <= 0:
                print(f'{opponent.name} has been defeated!')

    def evade(self):
        self.invulnerable = True

# Create Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.invulnerable = False

    def holy_strike(self, opponent):
        paladin_strike = self.attack(opponent)

        if paladin_strike is not None:
            bonus_damage_range = 1, 20
            min_bonus_damage, max_bonus_damage = bonus_damage_range
            bonus_damage = random.randint(min_bonus_damage, max_bonus_damage)
            opponent.health -= bonus_damage
            bonus_damage_msg = f'Holy Strike has dealt bonus damage! The normal strike attack was {paladin_strike} but Holy Stike dealt {paladin_strike + bonus_damage} damage!'
            remaining_opponent_health_msg = f'{opponent.name} has {opponent.health}/{opponent.max_health} health.'
            damage_output_msg = f'{bonus_damage_msg} \n{remaining_opponent_health_msg}'
            print(damage_output_msg)

            if opponent.health <= 0:
                print(f'{opponent.name} has been defeated!')

    def divine_shield(self):
        self.invulnerable = True

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            archer = isinstance(player, Archer)
            paladin = isinstance(player, Paladin)

            if archer:
                abilities = ['quick_shot', 'evade']
                chosen_ability = random.choice(abilities)
                archer_special_ability = getattr(player, chosen_ability)

                if chosen_ability == 'quick_shot':
                    archer_special_ability(wizard)
                else:
                    archer_special_ability()
            elif paladin:
                abilities = ['holy_strike', 'divine_shield']
                chosen_ability = random.choice(abilities)
                archer_special_ability = getattr(player, chosen_ability)

                if chosen_ability == 'holy_strike':
                    archer_special_ability(wizard)
                else:
                    archer_special_ability()

        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
