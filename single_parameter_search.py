import csv,sys
import PySimpleGUI as sg
from googlesearch import search

End = "Your code has been executed!"
Er = "Some Error Occurred!"

try:
# to interact with CSV File.
    file = open("google_search.csv",'r')
    write = open("urls_results.csv",'w',newline='')
    fieldnames = ['Search', 'Result_URL']
    csvFile = csv.reader(file,delimiter=',')
    csvWrite = csv.DictWriter(write, fieldnames=fieldnames)
    result = []
    
# to search
    for row in csvFile:
        query = ",".join(row)
        print(query)
        for i in search(query, tld='com', lang='en', num=1, stop=1, pause=0.5):
            print(i)
            result.append(i)
            csvWrite.writerow({'Search': query, 'Result_URL':i})

# end the code
    file.close()
    write.close()
    
    print(End)
    sg.Popup(End)

except:
    print(Er)
    sg.Popup(Er)
