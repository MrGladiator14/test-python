import csv
import statistics
from datetime import datetime

def read_weather_data(filename):
    """Read weather data from CSV file and return lists of dates, temperatures, and humidity."""
    dates = []
    temperatures = []
    humidity = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row['Date'])
            temperatures.append(float(row['Temperature (°C)']))
            humidity.append(int(row['Humidity (%)']))
    
    return dates, temperatures, humidity

def calculate_average(values):
    """Calculate the average of a list of values."""
    return sum(values) / len(values)

def calculate_median(values):
    """Calculate the median of a list of values using statistics module."""
    return statistics.median(values)

def analyze_weather_data(filename):
    """Main function to analyze weather data and display results."""
    print("Weather Data Analysis for Gandhinagar")
    print("=" * 40)
    
    # Read data from CSV
    dates, temperatures, humidity = read_weather_data(filename)
    
    # Display raw data
    print("\nRaw Weather Data:")
    print(f"{'Date':<12} {'Temp (°C)':<10} {'Humidity (%)':<12}")
    print("-" * 35)
    for i in range(len(dates)):
        print(f"{dates[i]:<12} {temperatures[i]:<10.1f} {humidity[i]:<12}")
    
    # Calculate and display statistics
    print(f"\nStatistics for the last {len(dates)} days:")
    print("-" * 30)
    
    # Temperature statistics
    avg_temp = calculate_average(temperatures)
    median_temp = calculate_median(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    
    print(f"\nTemperature (°C):")
    print(f"  Average: {avg_temp:.2f}")
    print(f"  Median:  {median_temp:.2f}")
    print(f"  Minimum: {min_temp:.1f}")
    print(f"  Maximum: {max_temp:.1f}")
    
    # Humidity statistics
    avg_humidity = calculate_average(humidity)
    median_humidity = calculate_median(humidity)
    min_humidity = min(humidity)
    max_humidity = max(humidity)
    
    print(f"\nHumidity (%):")
    print(f"  Average: {avg_humidity:.2f}")
    print(f"  Median:  {median_humidity:.2f}")
    print(f"  Minimum: {min_humidity}")
    print(f"  Maximum: {max_humidity}")

if __name__ == "__main__":
    csv_file = "gandhinagar_weather.csv"
    analyze_weather_data(csv_file)
