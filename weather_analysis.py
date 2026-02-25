import csv
import statistics
from datetime import datetime

def read_weather_data(filename):
    """Read weather data from CSV file and return lists of dates, temperatures, humidity, and AQI."""
    dates = []
    temperatures = []
    humidity = []
    aqi = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row['Date'])
            temperatures.append(float(row['Temperature (°C)']))
            humidity.append(int(row['Humidity (%)']))
            aqi.append(int(row['AQI']))
    
    return dates, temperatures, humidity, aqi

def calculate_average(values):
    """Calculate the average of a list of values."""
    return sum(values) / len(values)

def calculate_median(values):
    """Calculate the median of a list of values using statistics module."""
    return statistics.median(values)

def analyze_weather_data(filename):
    """Main function to analyze weather data and display results."""
    results = []
    
    # Read data from CSV
    dates, temperatures, humidity, aqi = read_weather_data(filename)
    
    # Add header to results
    results.append("Weather Data Analysis for Gandhinagar")
    results.append("=" * 40)
    
    # Display raw data
    results.append("\nRaw Weather Data:")
    results.append(f"{'Date':<12} {'Temp (°C)':<10} {'Humidity (%)':<12} {'AQI':<6}")
    results.append("-" * 45)
    for i in range(len(dates)):
        results.append(f"{dates[i]:<12} {temperatures[i]:<10.1f} {humidity[i]:<12} {aqi[i]:<6}")
    
    # Calculate and display statistics
    results.append(f"\nStatistics for the last {len(dates)} days:")
    results.append("-" * 30)
    
    # Temperature statistics
    avg_temp = calculate_average(temperatures)
    median_temp = calculate_median(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    
    results.append(f"\nTemperature (°C):")
    results.append(f"  Average: {avg_temp:.2f}")
    results.append(f"  Median:  {median_temp:.2f}")
    results.append(f"  Minimum: {min_temp:.1f}")
    results.append(f"  Maximum: {max_temp:.1f}")
    
    # Humidity statistics
    avg_humidity = calculate_average(humidity)
    median_humidity = calculate_median(humidity)
    min_humidity = min(humidity)
    max_humidity = max(humidity)
    
    results.append(f"\nHumidity (%):")
    results.append(f"  Average: {avg_humidity:.2f}")
    results.append(f"  Median:  {median_humidity:.2f}")
    results.append(f"  Minimum: {min_humidity}")
    results.append(f"  Maximum: {max_humidity}")
    
    # AQI statistics
    avg_aqi = calculate_average(aqi)
    median_aqi = calculate_median(aqi)
    min_aqi = min(aqi)
    max_aqi = max(aqi)
    
    results.append(f"\nAir Quality Index (AQI):")
    results.append(f"  Average: {avg_aqi:.2f}")
    results.append(f"  Median:  {median_aqi:.2f}")
    results.append(f"  Minimum: {min_aqi}")
    results.append(f"  Maximum: {max_aqi}")
    
    # Save results to file
    save_results_to_file(results)
    
    # Also print to console
    print("\n".join(results))
    
    return results

def save_results_to_file(results):
    """Save analysis results to a text file."""
    filename = "weather_analysis_results.txt"
    with open(filename, 'w') as file:
        file.write("\n".join(results))
    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    csv_file = "gandhinagar_weather.csv"
    analyze_weather_data(csv_file)
