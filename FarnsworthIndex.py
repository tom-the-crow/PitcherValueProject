import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = ['Name', 'Handed', 'IP', 'SO', 'R', 'HR', 'BB', 'HBP', 'BK', 'WP']

        with open(output_file, 'w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                name = row['Name']
                handed = 'LEFT' if '*' in name else 'RIGHT'
                name = name.replace('*', '') #this is just cleanup to remove the asterisk, it's bugging me

                processed_row = {
                    'Name': name,
                    'Handed': handed,
                    'IP': row['IP'],
                    'SO': row['SO'],
                    'R': row['R'],
                    'HR': row['HR'],
                    'BB': row['BB'],
                    'HBP': row['HBP'],
                    'BK': row['BK'],
                    'WP': row['WP']
                }

                writer.writerow(processed_row)

    print("CSV processing completed successfully!")

# Usage example
process_csv('Yanks2022RAW.csv', 'Yanks2022PROC.csv')



