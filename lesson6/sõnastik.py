def arvutaKeskmineHinne(grades):

     averageGrades = {}
     for name, grade in grades.items():
         averageGrades[name] = sum(grade)/len(grade)
     return averageGrades
