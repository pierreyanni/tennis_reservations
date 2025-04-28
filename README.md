# Tennis Court Reservation Helper

A simple application to quickly open the Montreal tennis court reservation page with pre-filled date and time parameters.

## Features

- GUI interface for easy date and time selection
- Command-line interface for quick access
- Automatic end time calculation (1 hour after start time)
- Windows shortcut support

## Installation

### Prerequisites

- Python 3.x
- tkinter (Python GUI library)
- WSL (Windows Subsystem for Linux) if using Windows

### Setup

1. Install Python dependencies:
```bash
# On Ubuntu/WSL:
sudo apt-get update
sudo apt-get install python3-tk
```

2. Clone or download this repository

## Usage

### GUI Application

1. Run the GUI application:
```bash
python3 tennis_gui.py
```

2. Fill in the fields:
   - Date (YYYY-MM-DD format)
   - Start Time (can be just the hour or HH:MM)
   - End Time (optional, defaults to 1 hour after start time)

3. Click "Open Reservation Page" to open the reservation website

### Command Line

You can also use the command-line version:

```bash
python3 open_tennis_url.py 2024-03-21 9 10
```

Arguments:
1. Date (YYYY-MM-DD)
2. Start time (can be just the hour or HH:MM)
3. End time (optional, defaults to 1 hour after start time)

### Windows Shortcut

1. Create a shortcut on your desktop
2. Set the target to:
```
C:\Windows\System32\wsl.exe python3 /home/pyanni/projects/tennis_reservations/tennis_gui.py
```

## Project Structure

- `tennis_gui.py` - GUI application
- `open_tennis_url.py` - Command-line interface
- `tennis_reservation.sh` - Shell script for Linux/WSL
- `tennis_reservation.bat` - Batch file for Windows

## Troubleshooting

### Common Issues

1. **Tkinter not found**
   - Solution: Install python3-tk package
   ```bash
   sudo apt-get install python3-tk
   ```

2. **WSL path issues**
   - Make sure to use the correct path to your Python files in WSL

3. **Permission denied**
   - Run scripts with appropriate permissions
   ```bash
   chmod +x tennis_reservation.sh
   ```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
