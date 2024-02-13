# Place code below to do the munging part of this assignment.
input_file = "data/nasa_data.txt"
output_file = "data/clean_data.csv"

last_year_line = None
first_year_found = False
first_title = True 

# Find num of the last line that start with "Year"
with open(input_file, 'r', encoding="utf-8") as input:
    for num, line in enumerate(input, start=1):
        if line.startswith("Year"):
            last_year_line = num

# Pass data into output file from the first "Year" to the last to clean notes
if last_year_line is not None:
    with open(input_file, 'r', encoding="utf-8") as input, open(output_file, 'w', encoding="utf-8") as output: 
        for num, line in enumerate(input, start=1):
            if line.startswith("Year") and num <= last_year_line:
                output.write(line)
                first_year_found = True
            elif first_year_found and num <= last_year_line:
                output.write(line)

# Clear all duplicated headers & blank line
with open(output_file, 'r', encoding="utf-8") as input:
    lines = input.readlines()

with open(output_file, 'w', encoding="utf-8") as output:
    for line in lines:
        if line.strip():  
            if line.startswith("Year"):
                if first_title:
                    output.write(line)
                    first_title = False  
            else:
                output.write(line)

# Standardize seperators
with open(output_file, 'r', encoding="utf-8") as input:
    lines = [line.split() for line in input]
    standardized_lines = [' '.join(columns) + '\n' for columns in lines]
        
with open(output_file, 'w', encoding="utf-8") as output:
    output.writelines(standardized_lines)

# Keep only monthly data for further calculation
with open(output_file, 'r', encoding="utf-8") as input:
    lines = input.readlines()
    processed_lines = [' '.join(line.strip().split(' ')[:13]) + '\n' for line in lines]

with open(output_file, 'w', encoding='utf-8') as output:
    output.writelines(processed_lines)

# Convert temperature anomalies to Farenheit
with open(output_file, 'r', encoding="utf-8") as input:
    lines = [line.strip().split() for line in input.readlines()]
    faren_data = [' '.join([row[0]] + [format(float(column) * 1.8 / 100, '.1f') for column in row[1:]]) + '\n' for row in lines[1:]]

with open(output_file, 'w', encoding="utf-8") as output_file:
    output_file.writelines(faren_data)


