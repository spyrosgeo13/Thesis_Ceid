import csv
from scipy.stats import kurtosis, skew
import sys

def update_csv_with_statistics(existing_csv, updated_csv, main_array_size):
    with open(existing_csv, mode='r', newline='') as infile, open(updated_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header and write it to the new file with additional kurtosis and skewness columns
        headers = next(reader)
        new_headers = headers + [
            'Kurtosis Subarray Positions', 'Skewness Subarray Positions'
        ]
        writer.writerow(new_headers)

        # Process each row
        for row in reader:
            ipodianisma1 = int(row[2])
            ipodianisma2 = int(row[3])
            ipodianisma3 = int(row[4])

            # Calculate the sizes of the subarrays
            subarray1_size = main_array_size - ipodianisma1
            subarray2_size = ipodianisma1 - ipodianisma2
            subarray3_size = ipodianisma2 - ipodianisma3

            # Calculate the starting and ending positions of each subarray
            subarray1_start = 0
            subarray1_end = subarray1_size

            subarray2_start = subarray1_end
            subarray2_end = subarray2_start + subarray2_size

            subarray3_start = subarray2_end
            subarray3_end = subarray3_start + subarray3_size

            # Normalize the positions to a 0-1 scale
            positions = [
                subarray1_start / main_array_size, subarray1_end / main_array_size,
                subarray2_start / main_array_size, subarray2_end / main_array_size,
                subarray3_start / main_array_size, subarray3_end / main_array_size
            ]

            # Calculate kurtosis and skewness for the positions
            kurtosis_value = kurtosis(positions)
            skewness_value = skew(positions)

            # Debugging print statements to understand the results
            print(f"Positions: {positions}")
            print(f"Kurtosis: {kurtosis_value}")
            print(f"Skewness: {skewness_value}")

            # Append kurtosis and skewness values to the row
            new_row = row + [kurtosis_value, skewness_value]
            writer.writerow(new_row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python kurtosis_skew_calculation.py <input_csv> <output_csv> <main_array_size>")
        sys.exit(1)
    
    existing_csv = sys.argv[1]
    updated_csv = sys.argv[2]
    main_array_size = int(sys.argv[3])

    update_csv_with_statistics(existing_csv, updated_csv, main_array_size)

"""KΟι στήλες αυτές θα περιέχουν τις τιμές κυρτότητας και ασυμμετρίας βασισμένες στις κανονικοποιημένες θέσεις των υποσυνόλων μέσα στον κύριο πίνακα. 
Αυτό παρέχει ένα μέτρο του πόσο αριστερά ή δεξιά χωρίζεται κάθε υποσύνολο."""