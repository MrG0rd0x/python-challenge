import os
import csv

# Set path for file
csvpath = os.path.join("resources", "election_data.csv")

#Set up variables
rowcount = 1
list_of_candidates = []
dict = {}
winner_count = 0


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    #Now we're on row 2

    for row in csvreader:
        rowcount +=1
        current_candidate = row[2]
        
        #Add the current candidate to the list
        #Create the dictionary
        if str(current_candidate) not in list_of_candidates:
            list_of_candidates.append(current_candidate)
            dict[current_candidate] = 0
        
        #Adds the vote count to the dictionary key
        dict[current_candidate] += 1

#Calculate number of candidates
num_candidates = len(dict)

#Prints results to the terminal        
print("Election Results")
print("-----------------------------")
print(f'Total votes: {rowcount}')

#Loops through candidates, printing results and calculating winner
for name in list_of_candidates:
    count = int(dict.get(name)) 
    percentage = count / rowcount * 100
    print(f'{name}: {percentage:.3f}% ({count})')
    if count > winner_count:
        winner = name
        winner_count = count

#Prints winner
print("-----------------------------")
print(f'Winner: {winner}')
print("-----------------------------")

#Creates analysis file with same results
with open('analysis/analysis.txt', 'w') as f:
    f.write(f'Election Results\n')
    f.write(f'-----------------------------\n')
    f.write(f'Total votes: {rowcount}\n')

    #Loops through candidates, printing results and calculating winner
    for name in list_of_candidates:
        count = int(dict.get(name)) 
        percentage = count / rowcount * 100
        f.write(f'{name}: {percentage:.3f}% ({count})\n')
        if count > winner_count:
            winner = name
            winner_count = count

    #Prints winner
    f.write(f'-----------------------------\n')
    f.write(f'Winner: {winner}\n')
    f.write(f'-----------------------------\n')