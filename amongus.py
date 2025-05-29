import random
import time

def start_game():
    print("Игра началась!")

def create_crew():
    players = ["Игрок1", "Игрок2", "Игрок3", "Игрок4", "Игрок5"]
    print("Создание экипажа:", players)
    return players

def choose_impostor(players):
    impostor = random.choice(players)
    print("Предатель выбран (секретно)")
    return impostor

def kill(players, impostor):
    potential_victims = [p for p in players if p != impostor]
    victim = random.choice(potential_victims)
    print(f"{impostor} убивает {victim}")
    players.remove(victim)
    return victim

def check_alive(players):
    print("Проверка живых:", players)

def vote(players):
    voted_out = random.choice(players)
    print(f"Голосование: исключён {voted_out}")
    players.remove(voted_out)
    return voted_out

def show_status(players, impostor):
    print("Оставшиеся игроки:", players)
    if impostor not in players:
        print("Предатель выведен. Победа экипажа!")
    elif len(players) == 2:
        print("Предатель победил!")
    else:
        print("Игра продолжается...")

# Основной цикл
start_game()
players = create_crew()
impostor = choose_impostor(players)

while True:
    time.sleep(1)
    kill(players, impostor)
    check_alive(players)
    time.sleep(1)
    voted = vote(players)
    show_status(players, impostor)

    if impostor not in players or len(players) <= 2:
        break
