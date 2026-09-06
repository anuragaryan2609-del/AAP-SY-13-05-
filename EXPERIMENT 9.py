#Develop a Python script to read data from a CSV file, convert it into JSON format, and store the converted data in a JSON output file.
  
#Step 1: Create the Input File
#1. Create the students CSV File
#Create a file named students.csv with the following data:
#id, name, department, marks
#101, Anita, CSE, 85
#102, Rahul, ECE, 78
#103, Priya, IT, 92
#104, Amit, CSE, 88

#Step 2: 
 
import csv
import json

with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")





