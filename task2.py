#Task-2 Scripting
# With the same attachment, use each worksheet as a CSV file and write a script (Bash or Python) that generates the same report. Data is to be read from the CSV files not from a database.


# SOLUTION:

import csv

def generate_report(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    data.sort(key=lambda x: float(x['Salary']), reverse=True)
    report = data[:3]

    print("DEPT_NAME")
    print("AVG_MONTHLY_SALARY (USD)")
    for row in report:
        print(row['NAME'])
        print(row['Salary'])

# Usage
generate_report('department.csv')
