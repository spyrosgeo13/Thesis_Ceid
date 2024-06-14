import os
import pandas as pd
import numpy as np

# Define the folder containing the CSV files
folder_path = r'C:\Users\spyro\OneDrive\Python_Projects\Thesis_code\csvfiles\poisson_files'

# Initialize a list to store the results
results = []

# List all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Load the CSV file into a DataFrame
        try:
            df = pd.read_csv(file_path)
            
            # Check if the column exists in the DataFrame
            if 'xronos katanomis' in df.columns:
                # Extract the column containing the times
                times = df['xronos katanomis']
                
                # Calculate the variance
                variance = np.var(times)
                
                # Append the results to the list
                results.append({'File Name': file_name, 'Variance': variance})
            else:
                print(f"Column 'xronos katanomis' not found in {file_name}. Skipping...")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Display the results
print(results_df)

# Optionally, save the results to a new CSV file
output_file_path = os.path.join(folder_path, 'variance_results.csv')
results_df.to_csv(output_file_path, index=False)
