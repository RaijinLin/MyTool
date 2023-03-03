import csv
import sys
from more_itertools import unique_everseen

# Get the input CSV filename from the command line arguments
# input_filename = sys.argv[1]
input_filename = 'Work/Beta/one.csv'
# Open the CSV file for reading and the TXT file for writing
with open(input_filename, 'r') as csv_file, open('Work/Beta/output.txt', 'w') as txt_file:
    reader = csv.reader(csv_file)

    # Skip the first row
    next(reader)

    # Get the values of the third and fourth column and remove duplicates
    values = unique_everseen((row[2], row[3]) for row in reader)

    # Write the unique values to the output file
    for value in values:
        txt_file.write('{}\n'.format(value[0]))
        txt_file.write('{}\n'.format(value[1]))

# Open the output file for reading and writing
with open('Work/Beta/output.txt', 'r+') as f:
    # Read the lines of the file and remove duplicates
    lines = list(unique_everseen(f))

    # Truncate the file to remove its previous contents
    f.seek(0)
    f.truncate()

    # Write the unique lines that don't start with '192.168' or '172.16' back to the file
    for line in lines:
        if not line.startswith('192.168') or not line.startswith('172.16'):
            f.write(line)
