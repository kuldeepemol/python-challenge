# Import CSV, OS and custom state abbreviation module
import csv
import os
from state_abbreviation import us_state_abbrev

# Get the filename to read data from: path where the program resides
file_read_name = os.path.join(os.path.dirname(__file__), 'employee_data.csv')
file_write_name = os.path.join(os.path.dirname(__file__), 'new_format_employee_data.csv')

# Open the budget_data.csv file using csv.DictReader
with open(file_read_name, 'r') as csvfile, \
    open(file_write_name, 'w', newline='') as outfile:

    employee_reader = csv.reader(csvfile, delimiter=',')
    new_format_writer = csv.writer(outfile)

    # Get the header from the file
    header = next(employee_reader)

    # Write the header to new file
    new_format_writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Loop over all the rows in the CSV file
    for row in employee_reader:

        emp_id, name, dob, ssn, state = row

        # Get first_name, last_name by splitting name on space
        first_name, last_name = name.split(' ')

        # Split DOB on - to get year, month and dat
        year, month, date = dob.split('-')

        # new format MM/DD/YYYY
        new_dob_format = month + '/' + date + '/' + year

        # split SSN by - to get 3 new variables
        ssn1, ssn2, ssn3 = ssn.split('-')

        # new SSN format
        new_ssn_format = '***-**-' + ssn3

        # using state abbreviation dictionary to get two letter code
        state_code = us_state_abbrev[state]

        # Write the the row data in new format
        new_format_writer.writerow([emp_id, first_name, last_name, new_dob_format, new_ssn_format, state_code])