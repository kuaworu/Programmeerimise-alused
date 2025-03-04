import sõnastik as avgGrade

# opilane = {
#     #key
#     'nimi': "Thomas",
#     'vanus': 18,
#     'klass': "12A"
# }

# # print(opilane['nimi'])
# # print(opilane.get['vanus'])

# # print(opilane.values())
# # print(opilane.keys())

# opilane["address"] = "Tallinn" #add element
# # opilane.pop('nimi') #delete element
# # def opilane['klass']

# print(opilane.values())
# print(opilane.keys())

# # for i in range(len(opilane))
# # print(opilane[i])

# for elem in opilane keys():
#     print(opilane[elem])

# # for elem in opilane values():
# #     print(elem)  
  
# for key, value in opilane.items():
#     print('see on võrti: ', key, 'see on värtsus')

grades = {
     "Mari": [4,5,3,4],
     'Jaan': [2,3,2,3,3],
     'Thomas': [3,2,4]
 }

result = avgGrade.arvutaKeskmineHinne(grades)
print(result)
