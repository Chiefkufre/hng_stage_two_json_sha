

## DOCUMENTATION
*************************************************************************
**Read this documentation before usage**

# Python Scripts 

This script convert .csv files to Json files from .csv file by row and print the hashcode for each json file

## Neccessary Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python.

```bash
pip install python3.10
```

## Important
There are three (3) important scripts in this document

1. csv2jsonconverter.py
2. shascript.py
3. Main.py

#### csv2jsonconverter
This file convert your .csv files to json format by row

#### shascript.py
This file generate hash256 codes from the json files generated from csv2jsonconverter

#### Main.py
This is the *entry point to the script*

**NOTE:**
1. All json files are generated automatically and stored in the jsonpath directory - "jsonpath"

2. Hash codes are stored in hash.txt

3. codes are commented out properly


## USAGE

1. Replace the **myteamcsv.csv file** with that of your team

**NOTE:**
Please delete your .csv files column titles

2. Ensure your file is named exactly as **myteamcsv.csv**

3. Run **main.py**

Your hash256 code will show on your terminal. 

The hash codes appear according to json files appearance this directory "/jsonpath"

You can also see your codes in the hash.txt file