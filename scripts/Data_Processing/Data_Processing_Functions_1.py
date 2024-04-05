#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:07:23 2024

@author: ray
"""

import pandas as pd

def copy_columns_to_clean_data(raw_data_file_path, clean_data_file_path, equivalent_headers_file_path):
    # Read the raw data file headers
    raw_data_headers = pd.read_csv(raw_data_file_path, nrows=0).columns.tolist()
    
    # Read the equivalent headers file
    equivalent_headers_df = pd.read_csv(equivalent_headers_file_path)

    # Read the clean data file (empty for now)
    clean_data_df = pd.DataFrame(columns=raw_data_headers)

    # Iterate over each header of the first file
    for header in raw_data_headers:
        # Flag to check if the header is found in any equivalent header column
        header_found = False
        # Iterate over each equivalent header column
        for col in range(1, 9):
            equivalent_headers_col = f'Equivalent_Headers_{col}'
            # Check if the header is found in the current equivalent header column
            if header in equivalent_headers_df[equivalent_headers_col].values:
                # Get the corresponding dispaset header
                dispaset_header = equivalent_headers_df.loc[equivalent_headers_df[equivalent_headers_col] == header, 'Dispaset_Headers'].values[0]
                # Copy the column to the clean data file
                clean_data_df[dispaset_header] = pd.read_csv(raw_data_file_path)[header]
                # Set the flag to True indicating header is found
                header_found = True
                # Break the loop as header is found
                break
        # If the header is not found in any equivalent header column, continue to the next header
        if not header_found:
            continue

    # Write clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Columns copied successfully.")
