#PyPoll

#Import Modules
import os
import csv

#Set Path
path = os.path.join('..', 'Resources', 'election_data.csv')

#Variable Declaration
total = 0
cand_list = {}
cand_percent = {}
winner = ""
count = 0

# Read CSV
with open(path, newline='') as file:
    reader = csv.reader(file, delimiter = ",")
    next(reader, None)
    for row in reader:

        #Calculate vote total 
        total = (total + 1)

        #Get candidate list 
        if row[2] in cand_list.keys():
            cand_list[row[2]] = (cand_list[row[2]] + 1) 
        else:
            cand_list[row[2]] = 1
        
        #Calculate Canditate Percentages
        for i, value in cand_list.items():
            cand_percent[i] = round((value/total) * 100, 1)
        
        #Get Winner
        for i in cand_list.keys():
            if cand_list[i] > count:
                winner = i
                count = cand_list[i]

#Print Output
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total}")
print(f"-------------------------")
for i, value in cand_list.items():
    print(i + ": " + str(cand_percent[i]) + "% " + "(" + str(value) + ")")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Specify File To Write To
output_file = os.path.join('..', 'Resources', 'election_data_analysis.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as csvfile:

# Write New Data
    csvfile.write("Election Results \n")
    csvfile.write("------------------------- \n")
    csvfile.write("Total Votes: " + str(total) + "\n")
    csvfile.write("------------------------- \n")
    for i, value in cand_list.items():
        csvfile.write(i + ": " + str(cand_percent[i]) + "% (" + str(value) + ") \n")
    csvfile.write("------------------------- \n")
    csvfile.write("Winner: " + winner + "\n")
    csvfile.write("------------------------- \n")
    
