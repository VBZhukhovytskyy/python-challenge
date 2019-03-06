import csv
import os
total_votes = 0
candidate_list = []
all_votes = []
row2 = []
final_tally = []
winner_count = 0
winner = []

PollData = os.path.join('..', "PyPoll",  "election_data.csv")
with open(PollData) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_votes += 1
        all_votes.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            
candidates:  object 
for candidates in candidate_list:
    tally_count = (all_votes.count(candidates))
    if tally_count > winner_count:
        winner_count = tally_count
        winner = candidates
                
    tally_percent = round(((tally_count/total_votes)*100))
      
 # Open the output file, create row, and then write the object to the csv
output_file = os.path.join('..', "PyPoll", "election_final.csv")
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")   
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------------------"]) 
    writer.writerow(["Total Votes", int(total_votes)])
    writer.writerow(["--------------------------------"])
        
    writer.writerow(["candidates:", winner, "received", tally_percent, "%", tally_count])
    writer.writerow(["---------------------------------"])
    writer.writerow(["Winner:", winner])
    writer.writerow(["---------------------------------"])



# To print for inf
print("Election Results")
print("--------------------------------") 
print("Total Votes", int(total_votes))
print("--------------------------------")      
print("candidates:", winner, "received", tally_percent, "%", tally_count)
print("--------------------------------")
print("Winner:", winner)
print("--------------------------------")