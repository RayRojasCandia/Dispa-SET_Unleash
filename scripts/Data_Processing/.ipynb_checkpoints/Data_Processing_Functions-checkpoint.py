#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:07:23 2024

@author: ray
"""
import os
import numpy as np
import pandas as pd
import requests

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





def update_technology_equivalents(clean_data_file_path, equivalent_technologies_file_path, not_defined_units_file_path):
    # Read the clean data file
    clean_data_df = pd.read_csv(clean_data_file_path)

    # Read the equivalent technologies file
    equivalent_technologies_df = pd.read_csv(equivalent_technologies_file_path)

    # Initialize a list to store unmatched rows
    unmatched_rows = []

    # Iterate over each row in the clean data file
    for index, row in clean_data_df.iterrows():
        technology = row['Technology']
        matched = False

        # Iterate over each column in the equivalent technologies file
        for col in range(1, 9):
            equivalent_technology = equivalent_technologies_df[f'Equivalent_Technology_{col}']
            dispaset_technology = equivalent_technologies_df['Dispaset_Technology']

            # Check if the technology exists in the equivalent technologies
            if technology in equivalent_technology.values:
                matched = True
                dispaset_technology_value = dispaset_technology[equivalent_technology == technology].values[0]
                clean_data_df.at[index, 'Technology'] = dispaset_technology_value
                break

        # If no match found, append the row to the unmatched rows list
        if not matched:
            unmatched_rows.append(row)

    # Convert unmatched rows list to DataFrame
    not_defined_units_df = pd.DataFrame(unmatched_rows)

    # Save the unmatched rows to the not defined units file
    not_defined_units_df.to_csv(not_defined_units_file_path, mode='a', header=False, index=False)

    # Remove unmatched rows from the clean data file
    clean_data_df = clean_data_df[~clean_data_df.index.isin(not_defined_units_df.index)]

    # Save the updated clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Technology equivalents updated successfully.")




def update_fuel_equivalents(clean_data_file_path, equivalent_fuels_file_path, not_defined_units_file_path):
    # Read the clean data file
    clean_data_df = pd.read_csv(clean_data_file_path)

    # Read the equivalent fuels file
    equivalent_fuels_df = pd.read_csv(equivalent_fuels_file_path)

    # Initialize a list to store unmatched rows
    unmatched_rows = []

    # Iterate over each row in the clean data file
    for index, row in clean_data_df.iterrows():
        fuel = row['Fuel']
        matched = False

        # Iterate over each column in the equivalent fuels file
        for col in range(1, 9):
            equivalent_fuel = equivalent_fuels_df[f'Equivalent_Fuel_{col}']
            dispaset_fuel = equivalent_fuels_df['Dispaset_Fuel']

            # Check if the fuel exists in the equivalent fuels
            if fuel in equivalent_fuel.values:
                matched = True
                dispaset_fuel_value = dispaset_fuel[equivalent_fuel == fuel].values[0]
                clean_data_df.at[index, 'Fuel'] = dispaset_fuel_value
                break

        # If no match found, append the row to the unmatched rows list
        if not matched:
            unmatched_rows.append(row)

    # Convert unmatched rows list to DataFrame
    not_defined_units_df = pd.DataFrame(unmatched_rows)

    # Save the unmatched rows to the not defined units file
    not_defined_units_df.to_csv(not_defined_units_file_path, mode='a', header=False, index=False)

    # Remove unmatched rows from the clean data file
    clean_data_df = clean_data_df[~clean_data_df.index.isin(not_defined_units_df.index)]

    # Save the updated clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Fuel equivalents updated successfully.")





def update_chp_types(clean_data_file_path, equivalent_chp_types_file_path, not_defined_units_file_path):
    # Read the clean data file
    clean_data_df = pd.read_csv(clean_data_file_path)

    # Read the equivalent CHP types file
    equivalent_chp_types_df = pd.read_csv(equivalent_chp_types_file_path)

    # Initialize a list to store unmatched rows
    unmatched_rows = []

    # Iterate over each row in the clean data file
    for index, row in clean_data_df.iterrows():
        chp_type = row['CHPType']
        chp_max_heat = row['CHPMaxHeat']

        # Check if CHPMaxHeat field is not empty
        if pd.notna(chp_max_heat):
            # Check if CHPType field is not empty
            if pd.notna(chp_type):
                matched = False
                # Iterate over each column in the equivalent CHP types file
                for col in range(1, 9):
                    equivalent_chp_type = equivalent_chp_types_df[f'Equivalent_CHPType_{col}']
                    dispaset_chp_type = equivalent_chp_types_df['Dispaset_CHPType']

                    # Check if the CHPType exists in the equivalent CHP types
                    if chp_type in equivalent_chp_type.values:
                        matched = True
                        dispaset_chp_type_value = dispaset_chp_type[equivalent_chp_type == chp_type].values[0]
                        clean_data_df.at[index, 'CHPType'] = dispaset_chp_type_value
                        break

                # If no match found, append the row to the unmatched rows list
                if not matched:
                    unmatched_rows.append(row)
            else:
                unmatched_rows.append(row)
        else:
            # Check if CHPType field is not empty
            if pd.notna(chp_type):
                matched = False
                # Iterate over each column in the equivalent CHP types file
                for col in range(1, 9):
                    equivalent_chp_type = equivalent_chp_types_df[f'Equivalent_CHPType_{col}']
                    dispaset_chp_type = equivalent_chp_types_df['Dispaset_CHPType']

                    # Check if the CHPType exists in the equivalent CHP types
                    if chp_type in equivalent_chp_type.values:
                        matched = True
                        dispaset_chp_type_value = dispaset_chp_type[equivalent_chp_type == chp_type].values[0]
                        clean_data_df.at[index, 'CHPType'] = dispaset_chp_type_value
                        break

                # If no match found, append the row to the unmatched rows list
                if not matched:
                    unmatched_rows.append(row)

    # Convert unmatched rows list to DataFrame
    not_defined_units_df = pd.DataFrame(unmatched_rows)

    # Save the unmatched rows to the not defined units file
    not_defined_units_df.to_csv(not_defined_units_file_path, mode='a', header=False, index=False)

    # Remove unmatched rows from the clean data file
    clean_data_df = clean_data_df[~clean_data_df.index.isin(not_defined_units_df.index)]

    # Save the updated clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("CHP types updated successfully.")




def remove_zero_power_capacity(clean_data_file_path, not_defined_units_file_path):
    # Read the clean data file
    clean_data_df = pd.read_csv(clean_data_file_path)

    # Initialize a list to store unmatched rows
    unmatched_rows = []

    # Iterate over each row in the clean data file
    for index, row in clean_data_df.iterrows():
        power_capacity = row['PowerCapacity']

        # Check if PowerCapacity field is empty or has a value of zero
        if pd.isnull(power_capacity) or power_capacity == 0:
            # Append the row to the unmatched rows list
            unmatched_rows.append(row)

    # Convert unmatched rows list to DataFrame
    not_defined_units_df = pd.DataFrame(unmatched_rows)

    # Save the unmatched rows to the not defined units file
    not_defined_units_df.to_csv(not_defined_units_file_path, mode='a', header=False, index=False)

    # Remove unmatched rows from the clean data file
    clean_data_df = clean_data_df[~clean_data_df.index.isin(not_defined_units_df.index)]

    # Save the updated clean data back to the clean data file
    clean_data_df.to_csv(clean_data_file_path, index=False)

    print("Zero power capacity rows removed successfully.")
    
    
    




def copy_column_values(first_file_path, second_file_paths, common_columns, column_to_copy):
    """
    Copy values from the specified column in the first file to the corresponding column in the second files
    when the corresponding column value is empty in the second files.

    Args:
    first_file_path (str): Path to the first CSV file.
    second_file_paths (list): List of paths to the second CSV files.
    common_columns (list): List of common column names used for filtering.
    column_to_copy (str): Name of the column whose values are to be copied.

    Returns:
    None
    """
    # Read first file into DataFrame
    first_df = pd.read_csv(first_file_path)

    # Iterate over second file paths
    for second_file_path in second_file_paths:
        # Read second file into DataFrame
        second_df = pd.read_csv(second_file_path)

        print(f"Copying {column_to_copy} values to {second_file_path}...")

        # Iterate over unique values of common columns in the second file
        for common_column in common_columns:
            for value in second_df[common_column].unique():
                # Filter rows in both files where common column matches
                first_filtered = first_df[first_df[common_column] == value]
                second_filtered = second_df[second_df[common_column] == value]

                # Iterate over rows in the second file
                for index, second_row in second_filtered.iterrows():
                    # Check if column value is empty or NaN in the second file
                    if pd.isnull(second_row[column_to_copy]):
                        # Find the row in the first file with the closest value (handling NA values)
                        closest_row_idx = (first_filtered[column_to_copy] - second_row[column_to_copy]).abs().argsort().values
                        closest_row_idx = closest_row_idx[np.isfinite(closest_row_idx)]  # Filter out NA values
                        if closest_row_idx.size > 0:
                            closest_row = first_filtered.iloc[closest_row_idx[0]]
                            # Copy column value from the first file to the second file
                            second_df.at[index, column_to_copy] = closest_row[column_to_copy]

        # Write updated DataFrame to the second file
        second_df.to_csv(second_file_path, index=False)

        print(f"{column_to_copy} values copied successfully.")
        
        




def fill_empty_values_with_specified(input_file_path, output_file_path, column, value):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
        return

    # Check if there are empty cells or cells with value 0 in the specified column
    empty_value_rows = df[df[column].isnull() | (df[column] == 0)]

    if not empty_value_rows.empty:
        # Create a new DataFrame with a row filled with the specified value for the selected column
        new_row = pd.DataFrame({col: [value] if col == column else [''] for col in df.columns})
        
        # Append the new row to the output file
        new_row.to_csv(output_file_path, mode='a', index=False, header=False)

        print(f"New row with '{column}' filled with '{value}' appended to '{output_file_path}'.")

        # Append the found rows to the output file
        empty_value_rows.to_csv(output_file_path, mode='a', index=False, header=False)

        print(f"Rows with empty '{column}' or value 0 appended to '{output_file_path}'.")

        # Drop rows with empty cells or cells with value 0 from the input DataFrame
        df = df.drop(empty_value_rows.index)

        # Write the updated DataFrame back to the original CSV file
        df.to_csv(input_file_path, index=False)

        print(f"Rows with empty '{column}' or value 0 removed from '{input_file_path}'.")

    else:
        print(f"No empty '{column}' or value 0 cells found in '{input_file_path}'.")





def copy_field_values(first_file_path, second_file_path, common_columns, column_to_copy):
    """
    Copies values from a specified column in the first file to the second file based on matching
    technology and fuel, filling missing values in the second file.

    Args:
        first_file_path (str): Path to the first CSV file.
        second_file_path (str): Path to the second CSV file.
        common_columns (list): List of column names present in both files.
        column_to_copy (str): Column name from the first file to copy values to the second file.
    """

    # Read CSV files into DataFrames
    first_df = pd.read_csv(first_file_path)
    second_df = pd.read_csv(second_file_path)

    print(f"Copying {column_to_copy} values from {first_file_path} to {second_file_path}...")

    # Iterate over unique values of "Technology" in the second file
    for technology in second_df['Technology'].unique():
        # Filter rows in both files where "Technology" matches
        first_filtered = first_df[first_df['Technology'] == technology]
        second_filtered = second_df[second_df['Technology'] == technology]

        # Iterate over unique values of "Fuel" in the second file
        for fuel in second_filtered['Fuel'].unique():
            # Filter rows with matching "Fuel" in both files
            first_fuel_filtered = first_filtered[first_filtered['Fuel'] == fuel]
            second_fuel_filtered = second_filtered[second_filtered['Fuel'] == fuel]

            # Iterate over rows in the second file
            for index, second_row in second_fuel_filtered.iterrows():
                # Check if value is empty in the second file's specified column
                if pd.isnull(second_row[column_to_copy]):
                    # Find the row in the first file with the closest "PowerCapacity" value
                    closest_row = first_fuel_filtered.iloc[(first_fuel_filtered['PowerCapacity'] - second_row['PowerCapacity']).abs().argsort()[:1]]

                    # Copy value from the first file to the second file
                    if not closest_row.empty:
                        second_df.at[index, column_to_copy] = closest_row[column_to_copy].values[0]

    # Write updated DataFrame to the second file
    second_df.to_csv(second_file_path, index=False)

    print(f"{column_to_copy} values copied successfully for {second_file_path}.")
    
    
    

"""
def copy_technical_values(first_file_path, target_files, common_columns, column_to_copy):

    Copies efficiency values (or any specified column) from the first file to a list of target files based on matching
    technology and fuel information. Fills missing values in target files.

    Args:
        first_file_path (str): Path to the first CSV file (source of efficiency values).
        target_files (list): List of paths to target CSV files.
        common_columns (list): List of column names common to all CSV files (excluding column_to_copy).
        column_to_copy (str): Column name to copy from the first file to target files.


    # Read the first file (source of efficiency values)
    first_df = pd.read_csv(first_file_path)

    for target_file in target_files:
        print(f"Processing target file: {target_file}")

        # Read the target file
        second_df = pd.read_csv(target_file)

        # Iterate over unique values of "Technology" in the target file
        for technology in second_df['Technology'].unique():
            # Filter rows in both files where "Technology" matches
            first_filtered = first_df[first_df['Technology'] == technology]
            second_filtered = second_df[second_df['Technology'] == technology]

            # Iterate over unique values of "Fuel" in the target file
            for fuel in second_filtered['Fuel'].unique():
                # Filter rows with matching "Fuel" in both files
                first_fuel_filtered = first_filtered[first_filtered['Fuel'] == fuel]
                second_fuel_filtered = second_filtered[second_filtered['Fuel'] == fuel]

                # Convert 'PowerCapacity' column to numeric
                first_fuel_filtered['PowerCapacity'] = pd.to_numeric(first_fuel_filtered['PowerCapacity'], errors='coerce')

                # Iterate over rows in the target file
                for index, second_row in second_fuel_filtered.iterrows():
                    # Check if the column_to_copy value is missing in the target file
                    if pd.isnull(second_row[column_to_copy]):
                        # Convert 'PowerCapacity' value to numeric
                        second_row['PowerCapacity'] = pd.to_numeric(second_row['PowerCapacity'], errors='coerce')

                        # Find the row in the first file with the closest "PowerCapacity" value
                        closest_row = first_fuel_filtered.iloc[(first_fuel_filtered['PowerCapacity'] - second_row['PowerCapacity']).abs().argsort()[:1]]

                        # Copy the column_to_copy value from the first file to the target file
                        if not closest_row.empty:
                            second_df.at[index, column_to_copy] = closest_row[column_to_copy].values[0]

        # Write updated DataFrame to the target file
        second_df.to_csv(target_file, index=False)

    print(f"{column_to_copy} Field values copied successfully.")
"""    

    
    
    
    


def copy_technical_values(first_file_path, target_files, common_columns, column_to_copy):
    """
    Copies efficiency values (or any specified column) from the first file to a list of target files based on matching
    technology and fuel information. Fills missing values in target files.

    Args:
        first_file_path (str): Path to the first CSV file (source of efficiency values).
        target_files (list): List of paths to target CSV files.
        common_columns (list): List of column names common to all CSV files (excluding column_to_copy).
        column_to_copy (str): Column name to copy from the first file to target files.
    """

    # Read the first file (source of efficiency values)
    first_df = pd.read_csv(first_file_path)

    for target_file in target_files:
        print(f"Processing target file: {target_file}")

        # Read the target file
        second_df = pd.read_csv(target_file)

        # Iterate over unique values of "Technology" in the target file
        for technology in second_df['Technology'].unique():
            # Filter rows in both files where "Technology" matches
            first_filtered = first_df[first_df['Technology'] == technology]
            second_filtered = second_df[second_df['Technology'] == technology]

            # Iterate over unique values of "Fuel" in the target file
            for fuel in second_filtered['Fuel'].unique():
                # Filter rows with matching "Fuel" in both files
                first_fuel_filtered = first_filtered[first_filtered['Fuel'] == fuel]
                second_fuel_filtered = second_filtered[second_filtered['Fuel'] == fuel]

                # Convert 'PowerCapacity' column to numeric
                first_fuel_filtered['PowerCapacity'] = pd.to_numeric(first_fuel_filtered['PowerCapacity'], errors='coerce')

                # Iterate over rows in the target file
                for index, second_row in second_fuel_filtered.iterrows():
                    # Check if the column_to_copy value is missing in the target file
                    if pd.isnull(second_row[column_to_copy]):
                        # Convert 'PowerCapacity' value to numeric
                        second_row_power_capacity = pd.to_numeric(second_row['PowerCapacity'], errors='coerce')

                        # Find the row in the first file with the closest "PowerCapacity" value
                        closest_row = first_fuel_filtered.iloc[(first_fuel_filtered['PowerCapacity'] - second_row_power_capacity).abs().argsort()[:1]]

                        # Copy the column_to_copy value from the first file to the target file
                        if not closest_row.empty:
                            second_df.at[index, column_to_copy] = float(closest_row[column_to_copy].values[0])

        # Write updated DataFrame to the target file
        second_df.to_csv(target_file, index=False)

    print(f"{column_to_copy} Field values copied successfully.")


def generate_links_and_write_to_files(links, file_paths):
    for link, file_path in zip(links, file_paths):
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            links = data["data"]["links"]
            with open(file_path, "w") as f:
                for generated_link in links:
                    f.write(generated_link + "\n")
            print(f"Generated links written to {file_path}")
        else:
            print(f"Failed to fetch data from {link}")

# Example usage:
#links = ["https://example.com/link1", "https://example.com/link2", "https://example.com/link3"]
#file_paths = ["file1.txt", "file2.txt", "file3.txt"]

generate_links_and_write_to_files(links, file_paths)



