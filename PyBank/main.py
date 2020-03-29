import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')


#def sum_entries(budget_data):

#    budget_date = str(budget_data[0])
#    budget_prof_loss = int(budget_data[1])

row_counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#    print(csvreader)

    csv_header = next(csvreader)

#    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        row_counter += 1
``
    print(row_counter)