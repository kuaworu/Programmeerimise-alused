# filter_characters.py

with open('output.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

alive = []
dead = []

for line in lines:
    if line.endswith('alive'):
        alive.append(line.split(' – ')[0])
    elif line.endswith('dead'):
        dead.append(line.split(' – ')[0])

with open('alive-characters.txt', 'w', encoding='utf-8') as f_alive:
    for name in alive:
        f_alive.write(f"{name}\n")

with open('dead-characters.txt', 'w', encoding='utf-8') as f_dead:
    for name in dead:
        f_dead.write(f"{name}\n")

print("Characters filtered into alive-characters.txt and dead-characters.txt")
