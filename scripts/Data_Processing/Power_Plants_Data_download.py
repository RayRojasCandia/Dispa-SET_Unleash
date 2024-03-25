#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import requests
import sys

def download_file(url, folder_path, file_name):
    """
    Downloads a file from the given URL and saves it to the specified folder path with the given filename and extension.
    
    Parameters:
    - url: The URL to download the file from (string)
    - folder_path: The path of the folder where the file will be saved (string)
    - file_name: The name of the file (string)
    
    Returns:
    - downloaded_file_path: The full path of the downloaded file (string)
    """
    downloaded_file_path = os.path.join(folder_path, file_name)
    response = requests.get(url)
    if response.status_code == 200:
        with open(downloaded_file_path, 'wb') as f:
            f.write(response.content)
        return downloaded_file_path
    else:
        print(f"Error downloading file: {response.status_code}")
        return None

def write_to_csv(csv_file_path, file_name, link_source):
    """
    Writes filename and link source to a CSV file.
    
    Parameters:
    - csv_file_path: The path of the CSV file (string)
    - file_name: The name of the file (string)
    - link_source: The source link of the file (string)
    """
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_name", "link_source"])
        writer.writerow([file_name, link_source])
    print(f"CSV file '{csv_file_path}' created with the download link")

# Input variables from command line arguments
power_plants_file_name = sys.argv[1]
download_link = sys.argv[2]
zone_folder_name = sys.argv[3]
zone_folder_path = sys.argv[4]

# Create folder if it doesn't exist
if not os.path.exists(zone_folder_path):
    os.makedirs(zone_folder_path)

# Download the file
downloaded_file_path = download_file(download_link, zone_folder_path, power_plants_file_name)

# Write filename and link to CSV
csv_file_path = os.path.join(zone_folder_path, f"{zone_folder_name}_sources.csv")
write_to_csv(csv_file_path, power_plants_file_name, download_link)

print(f"File '{power_plants_file_name}' downloaded and saved at: {downloaded_file_path}")
