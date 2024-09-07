import pandas as pd
import os

def merge_csv_files(input_folder, output_file):
    csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]
    merged_df = pd.concat([pd.read_csv(os.path.join(input_folder, f)) for f in csv_files])
    merged_df.to_csv(output_file, index=False)
    print(f"Merged file saved as: {output_file}")

input_folder = "downloads"

output_file = "merged_datablist.csv"

merge_csv_files(input_folder, output_file)