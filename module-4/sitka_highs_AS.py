# sitka_highs_AS
# Asher Smithson
# December 19, 2024
# Assignment: M4.2 High/Low Temperatures

# Purpose: This program allows the user to visualize daily high or low temperatures
# from a weather dataset and loops until the user decides to exit.

import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

def load_weather_data(filename):
    """
    Reads the CSV file and extracts dates, high temperatures, and low temperatures.

    Args:
        filename (str): The path to the CSV file containing weather data.

    Returns:
        tuple: Three lists containing dates, high temperatures, and low temperatures.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        header_row = next(reader)  # Skip the header row

        # Initialize lists for dates, highs, and lows
        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)

    return dates, highs, lows

def plot_temperatures(dates, temperatures, title, color):
    """
    Plots the temperatures on a graph.

    Args:
        dates (list): List of datetime objects representing the dates.
        temperatures (list): List of temperature values corresponding to the dates.
        title (str): The title of the graph.
        color (str): The color of the plot line.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, temperatures, color=color)
    ax.set_title(title, fontsize=24)
    ax.set_xlabel('Date', fontsize=16)
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    fig.autofmt_xdate()
    plt.show()

def main():
    """
    Main function to run the weather data visualization program.
    Provides a menu for the user to choose between viewing high temperatures,
    low temperatures, or exiting the program.
    """
    print("\nWeather Data Visualization Program")
    print("Menu Options:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = load_weather_data(filename)

    while True:
        # Get user input
        choice = input("\nEnter your choice (1 for Highs, 2 for Lows, 3 to Exit): ").strip()

        if choice == '1':
            print("\nDisplaying High Temperatures...")
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            print("\nDisplaying Low Temperatures...")
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("\nThank you for using the Weather Data Visualization Program!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()
    
# References: 
# csv — CSV File Reading and Writing. (2024). Python Documentation. 
# https://docs.python.org/3/library/csv.html?utm_source=chatgpt.com 
# matplotlib. (2012). Quick start guide — Matplotlib 3.10.0 documentation. 
# https://matplotlib.org/stable/users/explain/quick_start.html 
# Plotly. (2024). https://plotly.com/python/ 
# seaborn. (2024). The seaborn.objects interface — seaborn 0.13.2 documentation. 
# https://seaborn.pydata.org/tutorial/objects_interface.html