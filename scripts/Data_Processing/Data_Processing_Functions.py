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


