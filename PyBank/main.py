import csv
import os

BudgetData = os.path.join('..', "PyBank",  "budget_data.csv")
                           
net_profit = 0
row_count = 0
prev_value = None
change_list = []

min_change = 0
max_change = 0
min_change_month = None
max_change_month = None

with open(BudgetData) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        current_value = int(row[1])
        current_month = row[0]
        if prev_value:
            change = current_value - prev_value
            change_list.append(change)
            if int(change) > int(max_change):
                max_change = change
                max_change_month = row[0]
            if int(change) < int(max_change):
                min_change = change
                min_change_month = row[0]
        prev_value = current_value

        row_count += 1

        net_profit += current_value



 # Open the output file, cfreate row, and then write the object to the csv
output_file = os.path.join('..', "PyBank",  "budget_final.csv")
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["Total Months:", int(row_count)]),                
    writer.writerow(["Total:     $", int(net_profit)]),
    writer.writerow(["Average change    $:", sum(change_list)/len(change_list)]),
    writer.writerow(["Greatest increase in Profifts: Feb-2012", str(max_change_month)]),
    writer.writerow(["Greatest increase in Profifts: Sep-2013    $", int(min(change_list))])

# Inf to check
    print(net_profit)
    print(row_count)
    print((sum(change_list))/len(change_list))
    print(min(change_list))
    print(max_change_month)  


 

