enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
def game():
    def drink_portion():
        portion_strength=10
        print(portion_strength)

drink_portion() #Function inside another function is local function
# print(portion_strength)

player_health=10
def increase_health():
    player_health=20
    print(f"player_health inside function: {player_health}")
    print(f"{enemies} health inside function: {player_health}")
increase_health()