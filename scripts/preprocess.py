import sys
import pandas as pd
import os

# Read command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the dataset
df = pd.read_csv(input_file)

# Example preprocessing (adjust as needed)
df = df.dropna()            # drop missing values
df = df.drop_duplicates()   # drop duplicates

# Ensure the output folder exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the cleaned dataset
df.to_csv(output_file, index=False)

print(f"✅ Preprocessing complete. File saved at: {output_file}")
