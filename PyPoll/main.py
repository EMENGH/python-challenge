import os
import csv
import operator

csvpath = os.path.join('..', 'election_data.csv')
sortedcsvpath = os.path.join('..', 'sorted_election_data.csv')
row_counter = 0
#profit_loss_accum = 0
#profit_value = 0
#profit_great_inc = 0
#profit_great_dec = 0
#profit_great_inc_dt = ''
#profit_great_dec_dt = ''

#with open(csvpath) as csvfile:
#    csvreader = csv.reader(csvfile, delimiter = ',')
#    csv_header = next(csvreader)
#    sortedlist = sorted(csvreader, key=operator.itemgetter(2), reverse=True)
   
with open(csvpath) as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(row['Candidate']), reverse=False)

with open((sortedcsvpath), 'w') as f:
    fieldnames = ['Voter ID', 'County', 'Candidate']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedlist:
        writer.writerow(row)

# read the input file row by row until the end fetching and calculating
# the requested information

    #the first time of this loop counts the number of votes casted 
       
    for row in spamreader:
        row_counter += 1
        print(row[2])
#        profit_value = int(row[1])
#        profit_loss_accum = (profit_loss_accum + profit_value)

        #find greatest increase for profits/losses + date for entire period
#        if profit_value > 0:
 #          if profit_great_inc < profit_value:
  #            profit_great_inc = profit_value
   #           profit_great_inc_dt = str(row[0])

        #find greatest decrease for profits/losses + date for entire period           
#          if profit_great_dec > profit_value:
 #             profit_great_dec = profit_value
  #            profit_great_dec_dt = str(row[0])

#calculate the average change for entire period
#avg_profit_loss = float("{0:.2f}".format(profit_loss_accum / row_counter))

#generate a final analysis and print it to the terminal
#print("")
#print("")
#print("----------------------------------------------------")
#print("            FINANCIAL ANALYSIS")
#print("----------------------------------------------------")
print(f"  TOTAL MONTHS: {row_counter}")    
#print(f"  TOTAL AMOUNT: ${profit_loss_accum}")
#print(f"  AVERAGE CHANGE: ${avg_profit_loss}")
#print(f"  GREATEST INCREASE IN PROFITS: {profit_great_inc_dt} ${profit_great_inc}")
#print(f"  GREATEST DECREASE IN PROFITS: {profit_great_dec_dt} ${profit_great_dec}")    
#print("")


# Specify the file to write to
#output_path = os.path.join("out_pybank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and prepare fields to print
#    csvwriter = csv.writer(csvfile)
#    numrows = ["TOTAL MONTHS : " + str(row_counter)]
#    profaccum = ["TOTAL AMOUNT : " + "$" + str(profit_loss_accum)]
#    avgchange = ["AVERAGE CHANGE : " + "$" + str(avg_profit_loss)]
#    greatprofinc = ["GREATEST PROFITS INCREASE : " + profit_great_inc_dt + " $" + str(profit_great_inc)]
#    greatprofdec = ["GREATEST PROFITS DECREASE : " + profit_great_dec_dt + " $" + str(profit_great_dec)]

    # Write rows to output file
#    csvwriter.writerow(["----------------------------------------------------"])
#    csvwriter.writerow(["            FINANCIAL ANALYSIS                      "])
#    csvwriter.writerow(["----------------------------------------------------"])
#    csvwriter.writerow(numrows)    
#    csvwriter.writerow(profaccum)
#    csvwriter.writerow(avgchange)
#    csvwriter.writerow(greatprofinc)
#    csvwriter.writerow(greatprofdec)  