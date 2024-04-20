import argparse
import csv
import sys


def merge_csv(csv_file1, csv_file2, output_file):
    # create a dictionary
    merged_data = {}

    # open first file to read
    with open(csv_file1, 'r') as file:
        # utilizing the DictReader method it reads the keys and field names taken from the header and rows
        reader = csv.DictReader(file)
        # create a key using their name and pass in the headers followed by rows
        for row in reader:
            merged_data[row['Name']] = row

    # open second file to read and append it into merged_data
    with open(csv_file2, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            merged_data[row['Name']] = row

    # open the csv file to output in write mode
    with open(output_file, 'w', newline='') as csvfile:
        # add header 'fieldnames'
        fieldnames = ['Name', 'Midterm', 'Lab', 'Final']
        # the DictWriter method automatically gives rows a ',' if row is empty
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()

        # write each header and row in the csv output file
        for row in merged_data.values():
            thewriter.writerow(row)


# using argparse to pass the files through terminal
parser = argparse.ArgumentParser()
parser.add_argument('--file1', dest='csv_input1', help='pass in first csv file')
parser.add_argument('--file2', dest='csv_input2', help='pass in second csv file')
args = parser.parse_args()

# if both files weren't passed throw an error and exit
if args.csv_input1 and args.csv_input2 is None:
    print('select 2 csv files')
    sys.exit()

# call my method that takes in both files and file to be output
merge_csv(args.csv_input1, args.csv_input2, 'merged_students.csv')
