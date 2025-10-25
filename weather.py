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

    temp_in_celsius = round((float(temp_in_fahrenheit) - 32) * 5 / 9, 1)
    return temp_in_celsius




def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    float_data = [float(value) for value in weather_data]
    len_data = len(float_data)
    mean = float(sum(float_data)) / float(len_data)
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
            if len(row) > 0:
                    date = row[0]
                    min_temp = int(row[1])
                    max_temp = int(row[2])
                    data.append([date, min_temp, max_temp])

    return data





def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    float_data = [float(value) for value in weather_data]
    min_value = min(float_data)

    min_index = None
    for index, x in enumerate(float_data):
        if x == min_value:
            min_index = index

    return (float(min_value), min_index)
    



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    float_data = [float(value) for value in weather_data]
    
    max_value = max(float_data)

    max_index = None
    for index, x in enumerate(float_data):
        if x == max_value:
            max_index = index

    return (float(max_value), max_index)



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    num_days = len(weather_data)

    min_temps = [day[1] for day in weather_data]    
    max_temps = [day[2] for day in weather_data]

    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    min_temp_c = convert_f_to_c(min_temp)
    max_temp_c = convert_f_to_c(max_temp)

    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])

    avg_low = calculate_mean(min_temps)
    avg_high = calculate_mean(max_temps)

    avg_low_c = convert_f_to_c(avg_low)
    avg_high_c = convert_f_to_c(avg_high)

    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {max_date}.\n"
        f"  The average low this week is {format_temperature(avg_low_c)}.\n"
        f"  The average high this week is {format_temperature(avg_high_c)}.\n"
    )

    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for day in weather_data:
        date = convert_date(day[0])
        min_temp = convert_f_to_c(day[1])
        max_temp = convert_f_to_c(day[2])

        summary += (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {format_temperature(min_temp)}\n"
            f"  Maximum Temperature: {format_temperature(max_temp)}\n"
            "\n"
        )
   
    return summary
