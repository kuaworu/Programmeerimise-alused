def readfile(filename):
    file = open(filename, "r", encoding="utf-8")
    print(file.read())
    file.close()