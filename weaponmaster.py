import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 20

class AI:
    def __init__(self):
        self.health = 20

weapons = ['Sword', 'Axe', 'Lance', 'Dagger']

def calculate_damage(weapon):
    if weapon == 'Dagger':
        return random.randint(1, 3)
    else:
        return random.randint(1, 5)

def get_valid_player_weapon():
    while True:
        player_weapon = input("Choose a weapon (Sword, Axe, Lance, Dagger): ")
        player_weapon_lower = player_weapon.lower()
        if player_weapon_lower in [weapon.lower() for weapon in weapons] or player_weapon_lower == 'exit':
            return player_weapon
        else:
            print("Invalid weapon choice. Please choose again.")

def battle(player, ai, player_weapon):
    if player_weapon.lower() == 'exit':   # leave the game early
        print("You chose to exit the game. Goodbye!")
        return False

    ai_weapon = random.choice(weapons)
    weapon_emojis = {'sword': '⚔️', 'Sword': '⚔️', 'axe': '🪓', 'Axe': '🪓', 'lance': '🔱', 'Lance': '🔱', 'dagger': '🗡️', 'Dagger': '🗡️'}

    player_weapon_emoji = weapon_emojis.get(player_weapon, player_weapon)
    ai_weapon_emoji = weapon_emojis.get(ai_weapon, ai_weapon)

    print(f"{player.name} chooses {player_weapon} {player_weapon_emoji}. AI chooses {ai_weapon} {ai_weapon_emoji}.")
    print()

    # Player's turn
    if player_weapon == 'Dagger':
        damage = calculate_damage(player_weapon)
        hit_rate = -0.1
        print(f"You're using a {player_weapon_emoji}. -10% hit rate.")
    elif (player_weapon == 'Sword' and ai_weapon == 'Axe') or \
         (player_weapon == 'Axe' and ai_weapon == 'Lance') or \
         (player_weapon == 'Lance' and ai_weapon == 'Sword'):
        damage = calculate_damage(player_weapon) + 2
        hit_rate = 0.2
        print(f"You have weapon advantage with {player_weapon_emoji}!")
    elif (player_weapon == 'Sword' and ai_weapon == 'Lance') or \
         (player_weapon == 'Axe' and ai_weapon == 'Sword') or \
         (player_weapon == 'Lance' and ai_weapon == 'Axe'):
        damage = calculate_damage(player_weapon)
        hit_rate = -0.3
        print(f"You have weapon disadvantage with {player_weapon_emoji}!")
    else:
        damage = calculate_damage(player_weapon)
        hit_rate = 0
        print(f"No weapon advantage or disadvantage with {player_weapon_emoji}.")

    if random.random() < (0.8 + hit_rate):  # 80% base hit rate
        ai.health -= damage
        print(f"You dealt {damage} damage to the AI.")
    else:
        print("Your attack missed!")

    print(f"AI's health: {ai.health}")
    print()

    if ai.health <= 0:
        print("Congratulations! You defeated the AI!")
        return False

    # AI's turn (counterattack)
    ai_damage = calculate_damage(ai_weapon)
    ai_hit_rate = 0

    if ai_weapon == 'Dagger':
        ai_hit_rate = -0.1
        print(f"AI is using a {ai_weapon_emoji}. -10% hit rate.")
    elif (ai_weapon == 'Sword' and player_weapon == 'Axe') or \
         (ai_weapon == 'Axe' and player_weapon == 'Lance') or \
         (ai_weapon == 'Lance' and player_weapon == 'Sword'):
        ai_damage += 2
        print(f"AI has weapon advantage with {ai_weapon_emoji}!")
    elif (ai_weapon == 'Sword' and player_weapon == 'Lance') or \
         (ai_weapon == 'Axe' and player_weapon == 'Sword') or \
         (ai_weapon == 'Lance' and player_weapon == 'Axe'):
        ai_hit_rate = -0.3
        print(f"AI has weapon disadvantage with {ai_weapon_emoji}!")

    if random.random() < (0.8 + ai_hit_rate):  # 80% base hit rate for AI
        player.health -= ai_damage
        print(f"AI dealt {ai_damage} damage to you.")
    else:
        print("AI's attack missed!")

    print(f"Your health: {player.health}")
    print()

    if player.health <= 0:
        print("Game over. You were defeated by the AI.")
        return False

    return True

def play_game():
    # Main game loop
    print("Welcome to the world of WeaponMaster, where you will duel an AI opponent with a variety of weapons. (Sword beats Axe, Axe beats Lance, Lance beats Sword, and Dagger is neutral.)")
    print("")
    print("Do your best to defeat your opponent bRaveefore they can defeat you. Good Luck.")
    print("")
    player_name = input("Enter your name: ")
    print("")
    player = Player(player_name)
    ai = AI()

    while battle(player, ai, get_valid_player_weapon()):
        pass

def rematch():
    while True:
        rematch_choice = input("Do you want a rematch? (yes/no): ").lower()
        if rematch_choice == 'yes':
            play_game()
        elif rematch_choice == 'no':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Start the game
play_game()
rematch()
