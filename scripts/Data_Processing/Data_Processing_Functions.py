#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:07:23 2024

@author: ray
"""

import pandas as pd

#raw_data_file_path =  '/home/ray/Dispa-SET_Unleash/RawData/PowerPlants/BE/5'
#clean_data_file_path = '/home/ray/Dispa-SET_Unleash/RawData/PowerPlants/BE/2020.csv'
#equivalent_headers_file_path = '/home/ray/Dispa-SET_Unleash/RawData/PowerPlants/power_plants_clean_data_equivalent_headers.csv'



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

    # Read the clean data file
    clean_data_df = pd.read_csv(clean_data_file_path)

    # Read the raw data file headers
    raw_data_headers = pd.read_csv(raw_data_file_path, nrows=0).columns.tolist()

    # Read the raw data file
    raw_data_df = pd.read_csv(raw_data_file_path, usecols=[col for col in raw_data_headers if col in equivalent_mapping])

    # Map equivalent headers to DispaSET headers and copy data
    for header in raw_data_df.columns:
        if header in equivalent_mapping:
            dispaset_header = equivalent_mapping[header]
            clean_data_df[dispaset_header] = raw_data_df[header]

    # Write clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Columns copied successfully.")





def fill_unit_field(clean_data_file_path):
    # Read the CSV file
    df = pd.read_csv(clean_data_file_path)

    # Iterate over each row
    for index, row in df.iterrows():
        # Check if the Unit field is empty
        if pd.isnull(row['Unit']):
            # Fill the field with the specified format
            unit_value = f"{row['Lat']}-{row['Lon']}-{row['Zone']}"
            df.at[index, 'Unit'] = unit_value

    # Save the DataFrame back to the CSV file
    df.to_csv(clean_data_file_path, index=False)
    print("Unit field filled successfully.")





def fill_nunits_column(clean_data_file_path):
    """
    Fill the 'Nunits' column in the specified CSV file with either 1 or a valid integer value.

    Args:
    clean_data_file_path (str): The file path of the CSV file.

    Returns:
    None
    """
    # Read the CSV file
    df = pd.read_csv(clean_data_file_path)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Check if Nunits field is empty or not a valid integer
        nunits_value = row['Nunits']
        if pd.isna(nunits_value) or not str(nunits_value).isdigit():
            # If empty or not a valid integer, fill with 1
            df.at[index, 'Nunits'] = 1
        else:
            # If a valid integer, convert it to int
            df.at[index, 'Nunits'] = int(nunits_value)

    # Save the DataFrame back to the CSV file
    df.to_csv(clean_data_file_path, index=False)

    print("Nunits column processed successfully.")





def move_rows_with_empty_zone(clean_data_file_paths, all_data_file_paths):
    for clean_data_file, all_data_file in zip(clean_data_file_paths, all_data_file_paths):
        # Read the clean data file
        clean_data_df = pd.read_csv(clean_data_file)

        # Check and move rows with empty 'Zone'
        empty_zone_rows = clean_data_df[clean_data_df['Zone'].isnull()]
        if not empty_zone_rows.empty:
            # Append rows to the 'all_data' file
            empty_zone_rows.to_csv(all_data_file, mode='a', header=False, index=False)
            # Drop rows with empty 'Zone' from the clean data file
            clean_data_df = clean_data_df.dropna(subset=['Zone'])

        # Save the updated clean data file
        clean_data_df.to_csv(clean_data_file, index=False)

        print(f"Processed {clean_data_file}")

