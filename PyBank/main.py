# Import CSV and OS library to read and write CSV
import csv
import os

# Get the filename to read data from: path where the program resides
filename = os.path.join(os.path.dirname(__file__), 'budget_data.csv')

# Variable to hold value
total_rows = 0
total_amount = 0
previous_amount = 0
total_change_amount = 0
greatest_increase_amount_value = 0
greatest_increase_amount_date = ""
greatest_decrease_amount_value = 0
greatest_decrease_amount_date = ""

# Open the budget_data.csv file using csv.DictReader
with open(filename, 'r') as csvfile:

    budget_reader = csv.reader(csvfile, delimiter=',')

    # Get the header from the file
    header = next(budget_reader)

    # Loop over all the rows in the CSV file
    for row in budget_reader:

        # increment the row count
        total_rows += 1

        # amount value from row[1]
        amount = int(row[1])

        # total amount is calculated using summation
        total_amount += amount

        # if row count is greater than 1, we calculate the change_amount
        if total_rows > 1:

            # change_amount is calculated using previous value
            change_amount = amount - previous_amount

            # Summation of the change amount
            total_change_amount += change_amount

            # Keep track of Greatest Increase in change
            if change_amount > greatest_increase_amount_value:
                greatest_increase_amount_value = change_amount
                greatest_increase_amount_date = row[0]

            # Keep track of Greatest Decrease in change
            if change_amount < greatest_decrease_amount_value:
                greatest_decrease_amount_value = change_amount
                greatest_decrease_amount_date = row[0]

        else:
            change_amount = 0

        # Assign the current amount to previous amount to calculate the change
        previous_amount = amount

# Variables to store print messages
title = "Financial Analysis"
separator = "-" * 30

total_months_msg = 'Total Months: ' + str(total_rows)

total_amount_msg = 'Total Amount: $ ' + str(total_amount)

# Calculate the Average change between the each months for the whole period
average_change = total_change_amount/(total_rows - 1)

average_change_msg = 'Average Change: $ ' + str(round(average_change, 2))

greatest_increase_amount_msg = 'Greatest Increase in Profits: '\
                               + str(greatest_increase_amount_date)\
                               + ' ($ ' + str(greatest_increase_amount_value) + ')'

greatest_decrease_amount_msg = 'Greatest Decrease in Profits: '\
                               + str(greatest_decrease_amount_date)\
                               + ' ($ ' + str(greatest_decrease_amount_value) + ')'

# Get the filename to write
filename = os.path.join(os.path.dirname(__file__), 'budget_summary.txt')

# Write the summary to the text file
with open(filename, 'w') as textfile:

    budget_summary_writer = csv.writer(textfile)

    # Write all the rows
    budget_summary_writer.writerow([title])
    budget_summary_writer.writerow([separator])
    budget_summary_writer.writerow([total_months_msg])
    budget_summary_writer.writerow([total_amount_msg])
    budget_summary_writer.writerow([average_change_msg])
    budget_summary_writer.writerow([greatest_increase_amount_msg])
    budget_summary_writer.writerow([greatest_decrease_amount_msg])

# Print the summary to the terminal
print(title)
print(separator)
print(total_months_msg)
print(total_amount_msg)
print(average_change_msg)
print(greatest_increase_amount_msg)
print(greatest_decrease_amount_msg)