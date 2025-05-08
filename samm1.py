with open("characters.txt", "r", encoding="utf-8") as file:
    characters = [line.strip() for line in file.readlines()]
    
print(characters)