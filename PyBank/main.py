import os
import csv

# set paths for reading source data and writing output data files
PyBank_csv = os.path.join("Resources", "budget_data.csv")
PyBank_analysis = os.path.join("analysis", "financial_analysis.txt")

# Initialize variables
month = 0
net_profloss = 0
old_profloss = 0
new_profloss = 0
change_profloss = 0
total_change = 0
great_prof_inc = 0
great_prof_inc_date = ""
great_prof_dec = 0
great_prof_dec_date = ""

# Read data file
with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        # Count the months
        month +=1

        # Add current profit or loss to total profit/loss
        net_profloss += int(row[1])

        # After the first month, calculate and track the change in profit/loss
        if month >1:
            change_profloss = int(row[1]) - old_profloss
            total_change += change_profloss

            # Track the greatest increase and decrease in profit
            if change_profloss > great_prof_inc:
                great_prof_inc = change_profloss
                great_prof_inc_date = row[0]
            elif change_profloss < great_prof_dec:
                great_prof_dec = change_profloss
                great_prof_dec_date = row[0]
        
        # Update Old profit/loss tracker to prepare for next change calculation
        old_profloss = int(row[1])

# Calculate the average change in profit/loss
avg_change_profloss = total_change/(month - 1)

# Print results to the terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {month}")
print(f"Total: ${net_profloss}")
print(f"Average Change: ${round(avg_change_profloss, 2)}")
print(f"Gratest Increase in Profits: {great_prof_inc_date} (${great_prof_inc})")
print(f"Gratest Decrease in Profits: {great_prof_dec_date} (${great_prof_dec})")

# Export results to file
with open(PyBank_analysis, 'w') as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("--------------------------------\n")
    analysis.write(f"Total Months: {month}\n")    
    analysis.write(f"Total: ${net_profloss}\n")
    analysis.write(f"Average Change: ${round(avg_change_profloss, 2)}\n")
    analysis.write(f"Gratest Increase in Profits: {great_prof_inc_date} (${great_prof_inc})\n")
    analysis.write(f"Gratest Decrease in Profits: {great_prof_dec_date} (${great_prof_dec})\n")
    