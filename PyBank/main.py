import os
import csv

# Set path for file
csvpath = os.path.join("resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    rowcount = 0 
    netcount = 0


    for row in csvreader:
        rowcount +=1
        netcount = netcount + int(row[1])
        avg_change = row[1]



print ("Financial Analysis")
print ("-----------------------------")
print (f'Total Months: {rowcount}') 
print (f'Total: ${netcount}')
print (f'Average Change: ${avg_change}')
        
    
