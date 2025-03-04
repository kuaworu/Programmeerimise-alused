#fail = open("test.txt", "r/w/a",)
#file.read()
#file.write()
#file.close()
import log_parser as logs
import report_generator as generatereport

log_file = "logs.txt"

result = logs.analyze_log(log_file)
generatereport.generate_report(result)
#generate_report()

#with open("file.txt","r",encoding="utf-8") as file: 