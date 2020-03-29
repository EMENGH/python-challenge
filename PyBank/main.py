import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')


#def sum_entries(budget_data):

#    budget_date = str(budget_data[0])
#    budget_prof_loss = int(budget_data[1])

row_counter = 0
profit_loss_accum = 0
profit_value = 0
profit_great_inc = 0
profit_great_dec = 0
profit_great_inc_dt = ''
profit_great_dec_dt = ''

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
       
    for row in csvreader:
        row_counter += 1
        profit_value = int(row[1])
        profit_loss_accum = (profit_loss_accum + profit_value)

        #find greatest increase for profits/losses + date for entire period
        if profit_value > 0:
           if profit_great_inc < profit_value:
              profit_great_inc = profit_value
              profit_great_inc_dt = str(row[0])

        #find greatest decrease for profits/losses + date for entire period           
        elif profit_value < 0:
           if profit_great_dec > profit_value:
              profit_great_dec = profit_value
              profit_great_dec_dt = str(row[0])

#calculate the average change for entire period
avg_profit_loss = float("{0:.2f}".format(profit_loss_accum / row_counter))

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


