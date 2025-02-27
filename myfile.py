import bookcreator as bookcreator
import bookcreator2 as bookcreator2
import filereader as filereader
import spiderman as spiderman

def main():
    print("1 - külalisteraamat")
    print("2 - tegevus")
    print("3 - lugeda faili")
    print("4 - file")
    userinput = input("sinu valik: ")

    if userinput == "1":
        bookcreator.guestBook()
    elif userinput == "2":
        bookcreator2.createlog()
    elif userinput == "3":
        userfile = input("milline file sa tahad lugeda? ")
        filereader.readfile(userfile)
    elif userinput == "4":
        userfile = input("sisesta nimi: ")
        userfile2 = input("sisesta vana: ")
        spiderman.create(userfile, userfile2)  # Здесь передаем имя и возраст
    else:
        print("vale valik")

main()