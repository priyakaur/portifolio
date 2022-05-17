import pandas as pd
import re
from datetime import datetime
import numpy as np


#Extracting Dates from end path of a PDF File. 

DB = pd.read_excel("Extrac Dates.xlsx")
print(DB.head(5))

DB['four_digits'] = DB['File Name'].str.contains('\d{4}',case=False)
#print(DB.head(10))

DB = DB[DB['four_digits'] == True]
print(DB.count())
print(DB.head(5))

month = 'jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec'
year = range(2000,2022)
yr = range(0,20)
Date = ['\d{6,8}','\d{4}\Dd{2}\D\d{2}','[a-zA-Z]{3}\D\d{2}\D\d{2,4}','\d{2}\Dd{2}\D\d{2}']
date = '|'.join(Date)
print(list(year))

DB['date_match1'] = DB['File Name'].str.contains(date,case=False)
DB = DB[DB['date_match1'] == True]
print(DB.count())
DB.head(10)

extract = []

for x in DB['File Name']:
    r = re.findall(date,x)
    extract.append(r[0])

DB['date_extract'] = extract
DB['str_len'] = DB['File Name'].str.len()
DB = DB[DB['str_len'] >=15]
DB['dt_len'] = DB['date_extract'].str.len()

DB.head(10)

DB.to_csv('final_dates.csv')