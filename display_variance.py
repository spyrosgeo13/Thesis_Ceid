import pandas as pd

# Load the CSV file containing the variances
variance_results_file = r'C:\Users\spyro\OneDrive\Python_Projects\Thesis_code\csvfiles\poisson_files\variance_results.csv'  # Replace with your actual file path
variance_results_df = pd.read_csv(variance_results_file)

# Format the DataFrame as a table
formatted_table = variance_results_df.style.hide_index().set_caption("Variance of Times in CSV Files")

# Display the formatted table
formatted_table_html = formatted_table.render()
with open('formatted_table.html', 'w') as f:
    f.write(formatted_table_html)


