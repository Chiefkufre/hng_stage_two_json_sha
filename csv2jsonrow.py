

import json
import csv


# open the team csv fil

def create_json():
    csv_file = open("myteamcsv.csv", "r")

    csv_reader = csv.DictReader(csv_file, fieldnames=("Serial Number","Filename","Description","Gender","UUID","HASH"))


    count = 0

    for row in csv_reader:
        output = json.dumps(row)
        jsonoutput = open('jsonpath/jsonfile'+str(count)+'.json', 'w')
        jsonoutput.write(output)
        count += 1


    jsonoutput.close()
    csv_file.close()