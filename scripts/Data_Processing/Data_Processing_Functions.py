#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:11:25 2024

@author: ray
"""

# data_processing.py

import pandas as pd

def copy_columns_to_clean_data(raw_data_file_path, clean_data_file_path, equivalent_headers_file_path):
    # Read the equivalent headers file
    equivalent_headers_df = pd.read_csv(equivalent_headers_file_path)

    # Create a dictionary mapping equivalent headers to DispaSET headers
    equivalent_mapping = {}
    for index, row in equivalent_headers_df.iterrows():
        dispaset_header = row['Dispaset_Headers']
        # Iterate over the columns Equivalent_Headers_1 to Equivalent_Headers_8
        for col in range(1, 9):
            equivalent_header = row[f'Equivalent_Headers_{col}']
            # Check if the equivalent header exists and is not NaN
            if pd.notna(equivalent_header):
                equivalent_mapping[equivalent_header] = dispaset_header

    # Read the raw data file
    raw_data_df = pd.read_csv(raw_data_file_path)

    # Initialize the clean data DataFrame
    clean_data_df = pd.DataFrame()

    # Copy columns from raw data to clean data based on equivalent mapping
    for header in raw_data_df.columns:
        if header in equivalent_mapping:
            dispaset_header = equivalent_mapping[header]
            clean_data_df[dispaset_header] = raw_data_df[header]

    # Write clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Columns copied successfully.")
