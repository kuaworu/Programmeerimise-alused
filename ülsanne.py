from bs4 import BeautifulSoup #возможность посмотреть код страницы
import requests #качивает сайт

#пользователь вводит ссылку сайта
url = input('Sisesta URL (sisesta http:// või https://): ')

#скачивает сайт по адресу, который ввел и сохраняем html-код в переменную
response = requests.get(url)
html = response.text

#принимает html-код как структуру, чтобы могли искать h1, h2, h3...
soup = BeautifulSoup(html, "html.parser")

headings = []

#цикл по цифрам от 1 до 6
for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):  #находит все заголовки h{i}
        headings.append(heading.text.strip())  #добавляет в список
        print(f"Leitud H{i}: {heading.text.strip()}")  #показывает заголовок в окне

#считает, сколько заголовков с списке
print("Leitud kokku {} pealkirja.".format(len(headings)))
