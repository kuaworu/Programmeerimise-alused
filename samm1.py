import random

with open('characters.txt', 'r', encoding='utf-8') as file:
    characters = [line.strip() for line in file.readlines()]

with open('output.txt', 'w', encoding='utf-8') as out:
    for character in characters:
        status = random.choice(['alive', 'dead'])
        out.write(f"{character} – {status}\n")

print("output.txt created with character statuses.")
