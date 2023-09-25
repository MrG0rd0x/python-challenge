import os
import csv

rowcount = 1
votes = {}
# Some comment here about the expected structure of the CSV file
with open(os.path.join('resources', 'election_data.csv'), encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    # Now we're on row 2

    for row in csv_reader:
        rowcount +=1
        current_candidate = row[2]
        
        # Add the current candidate to the list
        votes[current_candidate] = votes.get(current_candidate, 0) + 1

candidates = []
winner_count = 0
# Loops through candidates, printing results and calculating winner
for name, count in votes.items():
    percentage = count / rowcount * 100
    candidates.append(f'{name}: {percentage:.3f}% ({count})')
    if count > winner_count:
        winner = name
        winner_count = count

results = [
    'Election Results',
    '-----------------------------',
    f'Total votes: {rowcount}',
    *candidates,
    '-----------------------------',
    f'Winner: {winner}',
    '-----------------------------',
]

print('\n'.join(results))

# Creates analysis file with same results
with open('analysis/analysis.txt', 'w') as f:
    f.write('\n'.join(results))