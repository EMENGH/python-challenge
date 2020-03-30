import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')

row_counter = 0
profit_loss_accum = 0
profit_value = 0
profit_great_inc = 0
profit_great_dec = 0
profit_great_inc_dt = ''
profit_great_dec_dt = ''
period_ctr = 0
valuelist = []
current_value = 0
previous_value = 0
delta_value = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#    print(csvreader)

    csv_header = next(csvreader)

#    print(f"CSV Header: {csv_header}")


#--------------------------------------------
# read the input file row by row until the end fetching and calculating
# the requested information
# all the information is gathered using just one initial read since there
# is no need to read the file again and again to get the desired results

    #   the first time of this loop counts the number of records and sums all
    #   the values in the profit/losses column
    
#    avg_daily_ctr = 0
#    avg_daily_accum = 0
#    avg_daily_total = 0
#    next_profit_value = 0

    for row in csvreader:
        row_counter += 1
        profit_value = int(row[1])
        profit_loss_accum = (profit_loss_accum + profit_value)

#-------------------------------------------
        #finding average
#       current_value = int(row[1])
        period_ctr += 1
        if period_ctr == 1:
           previous_value = int(row[1])
        else:   
           delta_value = int(row[1]) - previous_value
           previous_value = int(row[1])
           valuelist.append(delta_value)


        #find greatest increase for profits/losses + date for entire period
#        if profit_value > 0:
#           if profit_great_inc < profit_value:
#              profit_great_inc = profit_value
#              profit_great_inc_dt = str(row[0])

        if profit_great_inc < delta_value:
            profit_great_inc = delta_value
            profit_great_inc_dt = str(row[0])




        #find greatest decrease for profits/losses + date for entire period           
#        elif profit_value < 0:
        if profit_great_dec > delta_value:
            profit_great_dec = delta_value
            profit_great_dec_dt = str(row[0])

#calculate the average change for entire period
#avg_daily_total = avg_daily_accum / avg_daily_ctr
#print(f" ----- total average : {avg_daily_total}")
avg_profit_loss = float("{0:.2f}".format(sum(valuelist) / (period_ctr -1)))

#generate a final analysis and print it to the terminal
print("")
print("")
print("----------------------------------------------------")
print("            FINANCIAL ANALYSIS")
print("----------------------------------------------------")
print(f"  TOTAL MONTHS: {row_counter}")    
print(f"  TOTAL AMOUNT: ${profit_loss_accum}")
print(f"  AVERAGE CHANGE: ${avg_profit_loss}")
print(f"  GREATEST INCREASE IN PROFITS: {profit_great_inc_dt} ${profit_great_inc}")
print(f"  GREATEST DECREASE IN PROFITS: {profit_great_dec_dt} ${profit_great_dec}")    
print("")


# Specify the file to write to
output_path = os.path.join("out_pybank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and prepare fields to print
    csvwriter = csv.writer(csvfile)
    numrows = ["TOTAL MONTHS : " + str(row_counter)]
    profaccum = ["TOTAL AMOUNT : " + "$" + str(profit_loss_accum)]
    avgchange = ["AVERAGE CHANGE : " + "$" + str(avg_profit_loss)]
    greatprofinc = ["GREATEST PROFITS INCREASE : " + profit_great_inc_dt + " $" + str(profit_great_inc)]
    greatprofdec = ["GREATEST PROFITS DECREASE : " + profit_great_dec_dt + " $" + str(profit_great_dec)]

    # Write rows to output file
    csvwriter.writerow(["----------------------------------------------------"])
    csvwriter.writerow(["            FINANCIAL ANALYSIS                      "])
    csvwriter.writerow(["----------------------------------------------------"])
    csvwriter.writerow(numrows)    
    csvwriter.writerow(profaccum)
    csvwriter.writerow(avgchange)
    csvwriter.writerow(greatprofinc)
    csvwriter.writerow(greatprofdec)  