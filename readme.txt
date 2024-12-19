# Station Uptime Calculation Program

This folder contains a program to calculate station uptime from the input text files provided.

## Files Overview

- **station_uptime.py**: Contains the main logic for calculating station uptime.
  - **parse_input()**: Separates data from the input file for calculation.
  - **calculate_uptime()**: Calculates the uptime percentage based on the input data.

## Usage

1. Ensure you have the input files (e.g., `input_1.txt`) in the same directory.
2. If you want to add an input file, simply place it in the folder.
3. In the `station_uptime.py` file, modify the `file_path` variable to the name of the new input file (e.g., `"input_2.txt"`).
4. Run `station_uptime.py` to calculate the station uptime based on the input data.
5. The output will be printed on the console with the station IDs and their respective uptime percentages.

## Example Input

- **input_1.txt**: Contains two sections: `[Stations]` and `[Charger Availability Reports]`.
  - `[Stations]` lists the stations with their associated chargers.
  - `[Charger Availability Reports]` contains the availability data for each charger.

## Example Output

- The program calculates the uptime for each station based on the charger availability and prints the result.

