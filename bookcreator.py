def guestBook():
    name = input("sinu nimi: ")
    comment = input("sinu sõnum: ")
    text = f"nimi: {name}, sõnum: {comment}\n"
    file = open("guestbook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("sõnum oli salvestatu edukalt")