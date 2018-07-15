# Import OS library
import os

# Get the filename to read data from: path where the program resides
filename = os.path.join(os.path.dirname(__file__), 'raw_data', 'paragraph_1.txt')

# Variable to hold value
total_words = 0
total_sentence = 0
total_letter_count = 0

# Open the budget_data.csv file using csv.DictReader
infile = open(filename, 'r')

# loop over each line in the file
for line in infile:

    # Get all the sentences by split the line on .
    sentences = line.split('.')

    # loop over all the sentences
    for each_sentence in sentences:

        # remove spaces before and after
        each_sentence = each_sentence.strip()

        # Get all the words split by space
        all_words = each_sentence.split(' ')

        if len(all_words) == 1:
            continue

        # increment the total_sentence counter
        total_sentence += 1

        # loop over all the words
        for each_word in all_words:

            # Increment the word counter
            total_words += 1

            # total letter counter
            total_letter_count += len(each_word)

# Close the file
infile.close()

average_letter_count = total_letter_count/total_words
average_sentence_length = total_words/total_sentence

# Print the summary of Paragraph
print(f'Paragraph Analysis')
print(f'--------------------------')
print(f'Approximate Word Count: {total_words}')
print(f'Approximate Sentence Count: {total_sentence}')
print(f'Average Letter Count: {average_letter_count}')
print(f'Average Sentence Length: {average_sentence_length}')
