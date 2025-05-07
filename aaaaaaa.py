import os
import time

import csv
import datetime

#1) salvesta tulemused failise ping_log-csv
# Time,status
# 05.04.20.25,OK
# 05.04.20.25,Fail

hosts = ["8.8.8.8", "1.1.1.1", "192.168.56.1", "169.254.55.184"]

while True:
    print("kättesadavuse kontroll")
    for elem in hosts:
        response = os.system(f"ping -n 1 {elem} > null")
        if response == 0:
            result = "OK"
            print(elem, "kätesadavalt")
        else:
            result = "fail"
            print(elem, "ei ole kätesadavalt")
        print("-"*30)
        time.sleep(5)
       
with open ('ping_log-csv', 'a') as file:
    writer = csv.writer(file)
    wrter.writerow(["", result])