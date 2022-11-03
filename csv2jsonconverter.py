
import json
import csv



# this function to convert csv file into a json format 
def create_json(csvFIlePath, jsonFIlePath):

    data = {}

    # CSV file handler
    with open(csvFIlePath, encoding='utf-8') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for rows in csvReader:
            key = rows['Serial Number']
            data[key] = rows
    
    # Json handler
    with open(jsonFIlePath, "w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))



csvFIlePath = r"teamnft.csv"
jsonFIlePath = r"teamnft.json"


create_json(csvFIlePath, jsonFIlePath)


