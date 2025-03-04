#Функция для подсчёта количества каждой буквы в слове
def count_letters(word):
     letter_count = {}
     for letter in word:
         if letter in letter_count:
             letter_count[letter] += 1
         else:
             letter_count[letter] = 1
     return letter_count
