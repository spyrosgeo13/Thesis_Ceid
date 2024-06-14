import csv
from scipy.stats import kurtosis, skew
import sys
import numpy as np

def calculate_kurtosis(subarray):
    if len(subarray) > 1:
        return kurtosis(subarray)
    else:
        return float('nan')

def calculate_skewness(subarray):
    if len(subarray) > 1:
        return skew(subarray)
    else:
        return float('nan')

def update_csv_with_statistics(existing_csv, updated_csv, original_array_size):
    with open(existing_csv, mode='r', newline='') as infile, open(updated_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header and write it to the new file with additional kurtosis and skewness columns
        headers = next(reader)
        new_headers = headers + [
            'Kurtosis First Subarray', 'Kurtosis Second Subarray', 'Kurtosis Third Subarray',
            'Skewness First Subarray', 'Skewness Second Subarray', 'Skewness Third Subarray'
        ]
        writer.writerow(new_headers)

        # Process each row
        for row in reader:
            plithos_stoixeion_katanomis = int(row[0])
            xronos_katanomis = float(row[1])
            subarray_sizes = [int(row[2]), int(row[3]), int(row[4])]

            # Create the original array based on the size provided in the row
            original_array = list(range(plithos_stoixeion_katanomis))

            # Construct subarrays based on the given sizes
            subarrays = []
            current_array = original_array
            for size in subarray_sizes:
                subarray = current_array[:size]
                subarrays.append(subarray)
                current_array = current_array[size:]

            # Debugging print statements to understand the subarrays
            print(f"Original array size: {plithos_stoixeion_katanomis}")
            for i, subarray in enumerate(subarrays, 1):
                print(f"Subarray {i} (size {len(subarray)}): Mean = {np.mean(subarray)}, Variance = {np.var(subarray)}, Values = {subarray[:10]}...")

            # Calculate kurtosis and skewness for each subarray
            kurtosis_values = [calculate_kurtosis(subarray) for subarray in subarrays]
            skewness_values = [calculate_skewness(subarray) for subarray in subarrays]

            # Debugging print statements to understand the results
            print(f"Kurtosis values: {kurtosis_values}")
            print(f"Skewness values: {skewness_values}")

            # Append kurtosis and skewness values to the row
            new_row = row + kurtosis_values + skewness_values
            writer.writerow(new_row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python kurtosis_skew_calculation.py <input_csv> <output_csv> <original_array_size>")
        sys.exit(1)
    
    existing_csv = sys.argv[1]
    updated_csv = sys.argv[2]
    original_array_size = int(sys.argv[3])

    update_csv_with_statistics(existing_csv, updated_csv, original_array_size)
