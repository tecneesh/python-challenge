#PyBank

#Import Modules
import os
import csv

#Path
path = os.path.join('..', 'Resources', 'budget_data.csv')

#Variable Declarations 
months = 0
profit = 0
change_over_month = []
count_of_month = [] 
greatest_increase_date = 0
greatest_increase_amount = 0
greatest_decrease_date = 0
greatest_decrease_amount = 0 

#Read File
with open(path, newline='') as file:

    #Set Variables for Reader, Header & Row, Months, and Net Amount of Profit 
    reader = csv.reader(file, delimiter = ',')
    
    header = next(reader)
    row = next(reader)
    prev_row = int(row[1])
    months = (months + 1)
    profit = (profit + int(row[1]))
    greatest_increase_date = row[0]
    greatest_increase_amount = int(row[1])

    #Read the Rows
    for row in reader:

        #Calculate Month Total
        months = (months + 1)

        #Calculate Net Amount of Profit
        profit = (profit + int(row[1]))

        #Calculate Monthly Change
        change_in_rev = int(row[1]) - prev_row
        change_over_month.append(change_in_rev)
        prev_row = int(row[1])
        count_of_month.append(row[0])

        #Calculate Greatest Increase
        if int(row[1]) > greatest_increase_amount:
            greatest_increase_amount = int(row[1])
            greatest_increase_date = row[0]

        #Calculate Greatest Increase
        if int(row[1]) < greatest_decrease_amount:
            greatest_decrease_amount = int(row[1])
            greatest_decrease_date = row[0] 
        
    #Calculate Average and Highest & Lowest Monthly Change
    average = sum(change_over_month)/len(change_over_month)
    high = max(change_over_month)
    low = min(change_over_month)

#Print Output
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_date}, (${high})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_date}, (${low})")

# Specify File To Write To
output_file = os.path.join('..', 'Resources', 'budget_data_analysis.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as csvfile:

# Write New Data
    csvfile.write(f"Financial Analysis\n")
    csvfile.write(f"---------------------------\n")
    csvfile.write(f"Total Months: {months}\n")
    csvfile.write(f"Total: ${profit}\n")
    csvfile.write(f"Average Change: ${average}\n")
    csvfile.write(f"Greatest Increase in Profits:, {greatest_increase_date}, (${high})\n")
    csvfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_date}, (${low})\n")