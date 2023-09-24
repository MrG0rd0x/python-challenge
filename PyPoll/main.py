import os
import csv

# Set path for file
csvpath = os.path.join("resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    #Now we're on row 2
    firstrow = next (csvreader)
    first = int(firstrow[1])
print (first)