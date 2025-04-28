import webbrowser
from datetime import datetime, timedelta
import json
import urllib.parse
import argparse

def format_time(time_str):
    """
    Formats time string to ensure hours are two digits.
    
    Args:
        time_str (str): Time in HH:MM format
        
    Returns:
        str: Time with hours padded to two digits
    """
    if ':' not in time_str:
        time_str = f"{time_str}:00"
    hours, minutes = time_str.split(':')
    return f"{int(hours):02d}:{minutes}"

def calculate_end_time(start_time):
    """
    Calculates end time as one hour after start time.
    
    Args:
        start_time (str): Start time in HH:MM format
        
    Returns:
        str: End time one hour later in HH:MM format
    """
    # Parse the start time
    if ':' not in start_time:
        start_hour = int(start_time)
        start_minute = 0
    else:
        start_hour, start_minute = map(int, start_time.split(':'))
    
    # Calculate end time
    end_hour = (start_hour + 1) % 24
    return f"{end_hour:02d}:{start_minute:02d}"

def open_tennis_reservation(date, start_time, end_time=None):
    """
    Opens the tennis reservation page for a specific date and time range.
    
    Args:
        date (str): Date in YYYY-MM-DD format
        start_time (str): Start time in HH:MM format (24-hour)
        end_time (str, optional): End time in HH:MM format (24-hour). If not provided,
                                will be set to one hour after start time.
    """
    # Format start time
    start_time = format_time(start_time)
    
    # Calculate or format end time
    if end_time is None:
        end_time = calculate_end_time(start_time)
    else:
        end_time = format_time(end_time)
    
    # Create the search parameters
    search_param = {
        "filter": {
            "isCollapsed": False,
            "value": {
                "startTime": f"{date}T{start_time}:00.535-04:00",
                "endTime": f"{date}T{end_time}:00.536-04:00",
                "dates": [f"{date}T00:00:00.000-04:00"],
                "facilityTypeIds": "175",
                "boroughIds": "7"
            }
        },
        "search": "tennis",
        "sortable": {
            "isOrderAsc": True,
            "column": "facility.name"
        }
    }
    
    # Convert to JSON and URL encode
    encoded_param = urllib.parse.quote(json.dumps(search_param))
    url = f"https://loisirs.montreal.ca/IC3/#/U6510/search/?searchParam={encoded_param}&bids=20,55&hasBoroughFilter=true"
    
    webbrowser.open(url)

def main():
    parser = argparse.ArgumentParser(description='Open tennis court reservation page for a specific date and time.')
    parser.add_argument('date', help='Date in YYYY-MM-DD format (required)')
    parser.add_argument('start_time', help='Start time in HH:MM format (24-hour) (required)')
    parser.add_argument('end_time', nargs='?', help='End time in HH:MM format (24-hour) (optional, defaults to one hour after start time)')
    
    args = parser.parse_args()
    open_tennis_reservation(args.date, args.start_time, args.end_time)

if __name__ == "__main__":
    main() 