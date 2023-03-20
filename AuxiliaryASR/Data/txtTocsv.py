import csv

# Open the input and output files
with open('ASR_Train_data_test_kaggle.txt', 'r') as txt_file, open('csvFile.csv', 'w', newline='') as csv_file:

    # Set up the CSV writer
    csv_writer = csv.writer(csv_file)

    # Loop over each line in the text file
    for line in txt_file:

        # Split the line on the "|" character
        fields = line.strip().split('|')

        # Write the fields to the CSV file
        csv_writer.writerow(fields)
