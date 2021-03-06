import requests
import json 
import csv




def createCsv(): 
    URL = "https://quickstats.nass.usda.gov/api/api_GET/?key=12177F82-FCD6-3C46-BC03-515758C803CA"
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'commodity_dec': "TURKEYS", 'year__GE' : '1989' , 'state_alpha' : 'VA' , 'short_desc':'TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD' , 'freq_desc' :'MONTHLY' }  
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    # extracting data in json format 
    json_parsed = json.loads(r.text)
    json_data = json_parsed['data']
    info = open('TurkeysData.csv','w+')
    csvwriter = csv.writer(info)
    count = 0 
    for i in json_data:
        if count == 0:
            header = i.keys()
            csvwriter.writerow(header)
            count+=1
        csvwriter.writerow(i.values())
    info.close()

def main():
    createCsv()

main()





