import os
import csv

# Set path for file
csvpath = os.path.join("resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    rowcount = 1     
    max_profit = 0
    min_profit = 0
    firstrow = next (csvreader)
    netcount = int(firstrow[1])
    first = int(firstrow[1])
    second = int(firstrow[1]) 
    avg_sum = 0  


    for row in csvreader:
        rowcount +=1
        netcount = netcount + int(row[1])

        change = int(row[1]) - second
        second = int(row[1])
        avg_sum = avg_sum + change

        if int(change) > max_profit:
            max_profit = change
            date_max = row[0]
        
        if int(change) < min_profit:
            min_profit = change
            date_min = row[0]

average = avg_sum/(rowcount-1)

#Prints the analysis to the terminal
print ("Financial Analysis")
print ("-----------------------------")
print (f'Total Months: {rowcount}') 
print (f'Total: ${netcount}')
print (f'Average Change: $ {average:.2f}')
print (f'Greatest Increase in Profits: {date_max} (${max_profit})')
print (f'Greatest Decrease in Profits: {date_min} (${min_profit})')        

#Creates analysis text file with results    
with open('analysis/analysis.txt', 'w') as f:
    f.write ("Financial Analysis")
    f.write ("\n")
    f.write ("-----------------------------")
    f.write ("\n")
    f.write (f'Total Months: {rowcount}')
    f.write ("\n") 
    f.write  (f'Total: ${netcount}')
    f.write ("\n")
    f.write (f'Average Change: $ {average:.2f}')
    f.write ("\n")
    f.write (f'Greatest Increase in Profits: {date_max} (${max_profit})')
    f.write ("\n")
    f.write (f'Greatest Decrease in Profits: {date_min} (${min_profit})')    
    