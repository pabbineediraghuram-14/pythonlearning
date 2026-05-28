master_covid_data = { 'usa' : {'+ive': 20, 'test': 200 },
                    'india': {'+ive': 15, 'test': 100 },
                    'af': {'+ive': 2, 'test': 20 },
                    'zim': {'+ive': 10, 'test': 1 }}


today_data = {'usa' : {'+ive': 1, 'test': 1.5 },
         'india': {'+ive': 0.75, 'test': 1 },
         'af' : {'+ive': 0, 'test': 0 }}

merge = {}
for i in master_covid_data:
    if i in today_data:
        merge[i] = {'+ive': master_covid_data[i]['+ive'] + today_data[i]['+ive']
        ,
        'test': master_covid_data[i]['test'] + today_data[i]['test']
        }
    else:
        merge[i] = master_covid_data[i]
            
            
          
print(merge)
