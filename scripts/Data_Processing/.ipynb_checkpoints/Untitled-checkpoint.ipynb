{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b708b1bd-7ff2-4c05-beb1-1af0b8ec2fdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def copy_power_plants_data(raw_data_file_path, clean_data_file_path, equivalent_headers_file_path):\n",
    "    \"\"\"\n",
    "    Copies specified columns from a raw power plants data file to a clean data file,\n",
    "    using a mapping of equivalent headers.\n",
    "\n",
    "    Args:\n",
    "        raw_data_file_path (str): Path to the raw data file.\n",
    "        clean_data_file_path (str): Path to the clean data file.\n",
    "        equivalent_headers_file_path (str): Path to the equivalent headers CSV file.\n",
    "    \"\"\"\n",
    "\n",
    "    # Read the headers from the raw data file\n",
    "    raw_data_headers = pd.read_csv(raw_data_file_path, nrows=0).columns.tolist()\n",
    "\n",
    "    # Read the equivalent headers file\n",
    "    equivalent_headers_df = pd.read_csv(equivalent_headers_file_path)\n",
    "\n",
    "    # Create a mapping of equivalent headers to dispaset headers\n",
    "    equivalent_to_dispaset_mapping = {\n",
    "        eq_header: disp_header\n",
    "        for index, row in equivalent_headers_df.iterrows()\n",
    "        for eq_header, disp_header in zip(\n",
    "            row['Equivalent_Headers'].split(','), row['Dispaset_Headers'].split(',')\n",
    "        )\n",
    "    }\n",
    "\n",
    "    # Read the existing headers from the clean data file\n",
    "    existing_headers_df = pd.read_csv(clean_data_file_path, nrows=0)\n",
    "    existing_headers = existing_headers_df.columns.tolist()\n",
    "\n",
    "    # Read the raw data file\n",
    "    raw_data_df = pd.read_csv(raw_data_file_path)\n",
    "\n",
    "    # Create a new DataFrame to store the copied columns\n",
    "    clean_data_df = pd.DataFrame()\n",
    "\n",
    "    # Copy the relevant columns\n",
    "    for existing_header in existing_headers:\n",
    "        if existing_header in equivalent_to_dispaset_mapping.values():\n",
    "            for equivalent_header in equivalent_to_dispaset_mapping:  # Find matching equivalent header\n",
    "                if equivalent_header in raw_data_df.columns:\n",
    "                    clean_data_df[existing_header] = raw_data_df[equivalent_header]\n",
    "                    break\n",
    "        else:\n",
    "            clean_data_df[existing_header] = None  # Copy as is if no equivalent\n",
    "\n",
    "    # Write the clean data to the file\n",
    "    clean_data_df.to_csv(clean_data_file_path, index=False)\n",
    "\n",
    "    print(\"Columns copied successfully.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
