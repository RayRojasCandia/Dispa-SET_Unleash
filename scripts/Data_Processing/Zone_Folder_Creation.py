#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def create_folder(zone_folder_name, power_plants_folder_path):
    """
    Function to create a folder with the specified name at the specified path.
    
    Parameters:
    - zone_folder_name: Name of the folder to be created (string)
    - power_plants_folder_path: Path where the folder will be created (string)
    
    Returns:
    - zone_folder_path: Full path of the created folder (string)
    """
    # Combine folder name and path
    zone_folder_path = os.path.join(power_plants_folder_path, zone_folder_name)
    
    # Create the folder
    os.makedirs(zone_folder_path, exist_ok=True)
    
    # Print confirmation message
    print(f"Folder '{zone_folder_name}' created at: {zone_folder_path}")
    
    return zone_folder_path

# Main entry point
if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python folder_creator.py <folder_name> <folder_path>")
        sys.exit(1)
    
    # Extract folder name and path from command-line arguments
    zone_folder_name = sys.argv[1]
    power_plants_folder_path = sys.argv[2]
    
    # Call the create_folder function
    zone_folder_path = create_folder(zone_folder_name, power_plants_folder_path)
    
    # Output the created zone folder path
    print(f"Zone folder path: {zone_folder_path}")



