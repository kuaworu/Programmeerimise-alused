def main():
    with open("test.txt", "a", encoding="utf-8") as file:
        file.write(f"Pealkiri: {input('Sisesta pealkiri: ')}\nTekst: {input('Sisesta tekst: ')}\n---\n")
    print("Märge test.txt faili lisatud!")

main()