import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"




def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")




def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    return round((temp_in_fahrenheit - 32) * 5 / 9, 1)




def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    import statistics

    #mean = float(statistics.mean(weather_data))
    mean = sum(weather_data) / len(weather_data)
    return mean




def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, encoding="utf-8") as csv_data:
        reader = csv.reader(csv_data)
        next(reader)

        for row in reader:
            if len(row) >= 3:
                try:
                    date = row[0]
                    min_temp = int(row[1])
                    max_temp = int(row[2])
                    data.append([date, min_temp, max_temp])
                except ValueError:
                    continue

    return data





def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    min_value = min(weather_data)

    min_index = len(weather_data) - 1 - weather_data[::-1].index(min_value)

    return (float(min_value), min_index)




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    max_value = max(weather_data)

    max_index = len(weather_data) - 1 - weather_data[::-1].index(max_value)

    return (float(max_value), max_index)




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary = []

    for data_point in weather_data:
        str_items = []
        for item in data_point:
            str_items.append(str(item))
        summary.append(" , ".join(str_items))

    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = []

    for data_point in weather_data:
        str_items = []
        for item in data_point:
            str_items.append(str(item))
        summary.append(" , ".join(str_items))

    return summary
