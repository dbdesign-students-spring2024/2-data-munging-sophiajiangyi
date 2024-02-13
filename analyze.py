# Place code below to do the analysis part of the assignment.
import csv
input_file = "data/clean_data.csv"

decades_sum = {}
decades_valid_years = {}

with open(input_file, 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=' ')

    for row in data:
        year = int(row[0])
        decade = (year // 10) * 10  # Determine the decade for the row
        
        # Check if the row contains missing data
        if '*' in row:
            continue  # Skip this row
        
        # Calculate the yearly average, excluding the year column and any missing data
        try:
            temperatures = [float(temp) for temp in row[1:] if temp != '*']
            if temperatures:  
                yearly_average = sum(temperatures) / len(temperatures)
                
                # Initialize the decade in dictionaries if not already present
                if decade not in decades_sum:
                    decades_sum[decade] = 0
                    decades_valid_years[decade] = 0
                
                # Update the sums and counts
                decades_sum[decade] += yearly_average
                decades_valid_years[decade] += 1
        except ValueError:
            continue

# Calculate and print the average temperature for each decade
print("The temperature anomaly for the decades: ")
for decade in sorted(decades_sum.keys()):
    if decades_valid_years[decade] > 0:
        decade_average = decades_sum[decade] / decades_valid_years[decade]
        print(f"{decade}-{decade+9}: {decade_average:.1f}")
    else:
        print(f"{decade}-{decade+9}: No valid data")
