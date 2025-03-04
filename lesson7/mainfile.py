import esimene as esimeneFail
import teine as teineFail
import kolmes as kolmesFail

userinput = input("milline ülesanne sa tahad ülevaadata")
if userinput == "1":
    esimeneFail.myFunc()
elif userinput == "2":
    teineFail.myPykkar()
else:
    pass