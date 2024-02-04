#The One That Actually Calculates It
import csv

def calculate_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['GOOD_THINGS', 'BAD_THINGS', 'FARNSWORTH_INDEX']

        with open(output_file, 'w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                ip = float(row['IP'])
                so = float(row['SO'])
                r = float(row['R'])
                hr = float(row['HR'])
                bb = float(row['BB'])
                hbp = float(row['HBP'])
                bk = float(row['BK'])
                wp = float(row['WP'])

                good_things = (so / ip) * 100 # this is converting what percentage of times a good thing will happen
                bad_things = ((r + hr + bb + hbp + bk + wp) / ip) * 100 # also converting to a percentage of how often a bad thing will happen
                farnsworth_index = ( good_things / bad_things ) * 100 # and converting to a percentage

                row['GOOD_THINGS'] = good_things
                row['BAD_THINGS'] = bad_things
                row['FARNSWORTH_INDEX'] = farnsworth_index

                writer.writerow(row)

    print("CSV calculation completed successfully!")

# Usage example
calculate_csv('Yanks2022PROC.csv', 'Yanks2022CALC.csv')