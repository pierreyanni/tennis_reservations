import tkinter as tk
from tkinter import ttk
from datetime import datetime
import webbrowser
import json
import urllib.parse
from open_tennis_url import format_time, calculate_end_time

class TennisReservationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tennis Court Reservation")
        self.root.geometry("400x300")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Date selection
        ttk.Label(main_frame, text="Date:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(main_frame)
        self.date_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        # Start time selection
        ttk.Label(main_frame, text="Start Time:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.start_time_entry = ttk.Entry(main_frame)
        self.start_time_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.start_time_entry.insert(0, "9")
        
        # End time selection (optional)
        ttk.Label(main_frame, text="End Time (optional):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.end_time_entry = ttk.Entry(main_frame)
        self.end_time_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Submit button
        self.submit_button = ttk.Button(main_frame, text="Open Reservation Page", command=self.open_reservation)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=4, column=0, columnspan=2)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def open_reservation(self):
        try:
            date = self.date_entry.get()
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get() if self.end_time_entry.get() else None
            
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
            self.status_label.config(text="Opening reservation page...")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = TennisReservationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 