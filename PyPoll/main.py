import os
import csv
import operator

csvpath = os.path.join('..', 'election_data.csv')
sortedcsvpath = os.path.join('..', 'sorted_election_data.csv')
row_counter = 0
candidate_stored = ''
candidatelist = []
candidate_vote_ctr = 0
candidate_index = 0
candid_index = 0
vote_index = 0
current_candidate = ''
numvotes = 0

#with open(csvpath) as csvfile:
#    csvreader = csv.reader(csvfile, delimiter = ',')
#    csv_header = next(csvreader)
#    sortedlist = sorted(csvreader, key=operator.itemgetter(2), reverse=True)
   
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
#    sortedlist = sorted(csvreader, key=lambda row:(row['Candidate']), reverse=False)

#with open(sortedcsvpath), 'w') as f:
#   writer = csv.DictWriter(f, fieldnames=fieldnames)
#   writer.writeheader()
#   for row in sortedlist:
#       writer.writerow(row)

# read the input file row by row until the end fetching and calculating
# the requested information

    #the first time of this loop counts the number of votes casted 
    #current_candidate = row[2]

    for row in csvreader:

        if current_candidate == candidate_stored:
           candidate_vote_ctr += 1
           row_counter += 1
        else:  
           print(current_candidate[candidate_index])
           print(candidate_vote_ctr)

        #    candidatelist.append(row[2])
        #    candidate_vote_ctr += 1
        #    print(candidatelist[candid_index])
        #   candidate_index += 1
        #   candidate_vote.append
           
   

#generate a final analysis and print it to the terminal
print("")
print(f"  ELECTION RESULTS")
print(f"----------------------------------------------------")
print(f"  TOTAL VOTES: {row_counter}")
print(f"----------------------------------------------------")
print(f" ")   

#print(f"  AVERAGE CHANGE: ${avg_profit_loss}")
#print(f"  GREATEST INCREASE IN PROFITS: {profit_great_inc_dt} ${profit_great_inc}")
#print(f"  GREATEST DECREASE IN PROFITS: {profit_great_dec_dt} ${profit_great_dec}")    
#print("")


# Specify the file to write to
output_path = os.path.join("out_pypoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

#    Initialize csv.writer and prepare fields to print
     csvwriter = csv.writer(csvfile)
     numvotes = ["TOTAL VOTES : " + str(row_counter)]
#    profaccum = ["TOTAL AMOUNT : " + "$" + str(profit_loss_accum)]
#    avgchange = ["AVERAGE CHANGE : " + "$" + str(avg_profit_loss)]
#    greatprofinc = ["GREATEST PROFITS INCREASE : " + profit_great_inc_dt + " $" + str(profit_great_inc)]
#    greatprofdec = ["GREATEST PROFITS DECREASE : " + profit_great_dec_dt + " $" + str(profit_great_dec)]

    # Write rows to output file
     csvwriter.writerow([""])
     csvwriter.writerow([" ELECTION RESULTS"])
     csvwriter.writerow(["----------------------------------------------------"])
     csvwriter.writerow(numvotes)    
   