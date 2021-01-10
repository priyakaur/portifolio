import csv,sys
from googlesearch import search
import pandas as pd

End = "Your code has been executed!"
Er = "Some Error Occurred!"

try:
# to interact with data
    names = ['Elon Musk', 'Narendar Modi', 'mark zuckerberg', 'Barak Obama', 'Arvind Kejriwal']
    result = []
    DB = pd.DataFrame(names)
    
# to search
    for row in names:
        query = row + ' ' + 'LinkedIn'
        print(query)
        for i in search(query, tld='com', lang='en', num=1, stop=1, pause=0.5):
            print(i)
            result.append(i)

# end the code    
    print(End)

except:
    print(Er)
