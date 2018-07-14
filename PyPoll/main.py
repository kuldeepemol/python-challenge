# Import CSV and OS library to read and write CSV
import csv
import os

# Get the filename to read data from: path where the program resides
filename = os.path.join(os.path.dirname(__file__), 'election_data.csv')

# Variable to hold value
total_vote = 0
voters_summary = dict()

# Open the budget_data.csv file using csv.DictReader
with open(filename, 'r') as csvfile:

    election_reader = csv.reader(csvfile, delimiter=',')

    # read the header
    header = next(csvfile)

    # Loop over all the rows in the CSV file
    for row in election_reader:

        # increment the row count
        total_vote += 1

        # Get the voter name from 2 row/col
        voter_name = row[2]

        # Check if this voter is in the dictionary
        # then increment the value by 1
        if voter_name in voters_summary:
            voters_summary[voter_name] += 1
        else:
            # create new key in the dictionary and assign the value 1
            voters_summary[voter_name] = 1

# Variables to hold message
title = 'Election Results'
separator = '-' * 30
total_vote_msg = 'Total Votes: ' + str(total_vote)
final_winner = ''
final_winner_total = 0
each_voter_msg = ''

# Loop over all the items in the dictionary
for k, v in voters_summary.items():

    # Calculate the percentage for each voter
    vote_percent = (v / total_vote ) * 100

    # Create a message for each voter
    each_voter_msg += k + ': ' + str(round(vote_percent, 3)) + '% (' + str(v) + ')\n'

    # Find the voter with the highest votes
    if v > final_winner_total:
        final_winner = k
        final_winner_total = v

# print the  messages
final_winner_msg = 'Winner: ' + final_winner

# Get the filename to write
filename = os.path.join(os.path.dirname(__file__), 'election_summary.txt')

# Open a file to write the Election Summary
election_summary_writer = open(filename, 'w', newline="\n")

# Write the summary to the text file
election_summary_writer.write(title + '\n')
election_summary_writer.write(separator + '\n')
election_summary_writer.write(total_vote_msg + '\n')
election_summary_writer.write(separator + '\n')
election_summary_writer.write(each_voter_msg)
election_summary_writer.write(separator + '\n')
election_summary_writer.write(final_winner_msg + '\n')
election_summary_writer.write(separator)

# close the file writer
election_summary_writer.close()

# Print the summary to the terminal
print(title)
print(separator)
print(total_vote_msg)
print(separator)
print(each_voter_msg)
print(separator)
print(final_winner_msg)
print(separator)
