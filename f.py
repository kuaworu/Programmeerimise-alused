# stack = []
# 
# for i in range(1,11):
#     stack.append(f"{i} element")
#     print(f"{i} element append")
#     for i in stack:
#         print(i, end=" ")
#         
# for i in range(0,11):
#     print(i, "hello world")
    
#näide
# def helloPrinter(n):
#     if n <= 10:
#         n += 1
#         print("hello world")
#         helloPrinter(n)
#     else:
#         return False
#     
# helloPrinter(0)

# def helloPrinter(userInt, n):
#     if n < userInt:
#         n += 1
#         helloPrinter(userInt, n)
#     elif n==userInt:
#             print("hello"*n)
# helloPrinter(int(input("sisesta arv :")),0)

# def delit(words,n):
#     if n >= len[words]:
#         return ""
#     if words[n] = "!":
#         return delit(words, n+1)
#     else:
#         return words[n] + delit(words, n+1)
# 
# result = delit("!t",0)
# print(result)

# def find_upper(text, index=0):
#     if index >= len(text):
#         return -1  # если нет заглавных — возвращаем -1
#     if text[index].isupper():
#         return index
#     return find_upper(text, index + 1)
# 
# text = input("Sisesta tekst: ")
# result = find_upper(text)
# print("Esimese suurtähe indeks:", result)

# def print_chars(text, index=0):
#     if index >= len(text):
#         return  # базовый случай — остановка рекурсии
#     print(text[index])  # выводим текущий символ
#     print_chars(text, index + 1)  # рекурсивно вызываем для следующего символа
# 
# sentence = input("Sisesta lause: ")
# print_chars(sentence)

def remove_digits(text):
    if text == "":
        return ""
    first_char = text[0]
    if first_char.isdigit():
        first_char = ""  # удаляем цифру
    return first_char + remove_digits(text[1:])

user_input = input("Sisesta tekst: ")
print("Tulemus:", remove_digits(user_input))