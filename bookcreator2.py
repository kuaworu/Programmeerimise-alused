import datetime

def createlog():
    name = input("sinu nimi: ")
    action = input("sinu tegevus: ")
    time = datetime.datetime.now()
    text = f"date: {time},nimi: {name}, tegevus: {action}\n"
    file = open("guestbook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("logid oli salvestatu edukalt")