from colorama import Fore
import emoji

#приветствуем цветным текстом
print(Fore.CYAN + "Tere tulemast, kasutaja!" + Fore.RESET)

#даем эмоциям цвет и смайлик
meeleolud = {
    'happy': (Fore.YELLOW, emoji.emojize(":grinning_face_with_smiling_eyes:")),
    'sad': (Fore.BLUE, emoji.emojize(":disappointed_face:")),
    'tired': (Fore.MAGENTA, emoji.emojize(":sleepy_face:")),
    'excited': (Fore.GREEN, emoji.emojize(":star-struck:"))
}

# Küsi kasutajalt meeleolu
print("Vali oma meeleolu järgmiste valikute hulgast:") #выберите свое настроение из перечисленных
for idx, mood in enumerate(meeleolud.keys(), start=1): #нумерует
    print(f"{idx}. {mood.capitalize()}") #делает первую букву заглавной

# Kasutaja sisend
valik = int(input("Sisesta oma meeleolu number (1-4): ")) #пользователь вводит цифру от 1 до 4

# Kuvame vastava värvi sõnumi ja emotikoni
if 1 <= valik <= 4: #если номер в диапазоне от 1 до 4
    meeleolu = list(meeleolud.keys())[valik - 1] #находит нужное настроение по номеру
    color, emoticon = meeleolud[meeleolu] 
    print(color + f"Sa oled {meeleolu}!" + Fore.RESET) #печатает: "ты - настроение" цветным текстом
    print(f"Sõnum: {emoticon}") #печатает смайлик
else:
    print(Fore.RED + "Tundub, et sisestasite vale numbri! Palun valige number vahemikus 1-4." + Fore.RESET)
    #если печатает что-то не то, выводит сообщение об ошибке красным цветом

