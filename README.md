# Weather Analysis

A Python project for analyzing weather data from Gandhinagar.

## Features

- Reads weather data from CSV files (Date, Temperature, Humidity, AQI)
- Calculates comprehensive statistics for temperature, humidity, and air quality index
- Displays raw weather data in formatted table
- Computes average, median, minimum, and maximum values for all metrics
- Saves analysis results to `weather_analysis_results.txt`
- Prints results to console

## Functions

### Core Functions
- `read_weather_data(filename)`: Reads CSV data and returns lists of dates, temperatures, humidity, and AQI
- `calculate_average(values)`: Calculates average of a list of values
- `calculate_median(values)`: Calculates median using statistics module
- `analyze_weather_data(filename)`: Main analysis function that processes data and generates statistics
- `save_results_to_file(results)`: Saves analysis results to text file

## Usage

Run the weather analysis:
```bash
python weather_analysis.py
```

Run the main script:
```bash
python main.py
```

## Input Data Format

The script expects a CSV file with the following columns:
- `Date`: Date string
- `Temperature (°C)`: Temperature in Celsius
- `Humidity (%)`: Humidity percentage
- `AQI`: Air Quality Index

## Output

The analysis generates:
- Console output with formatted weather data and statistics
- `weather_analysis_results.txt` file with complete analysis results
