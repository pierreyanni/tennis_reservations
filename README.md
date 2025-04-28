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
- WSL (Windows Subsystem for Linux)

### Setup

1. Install Python dependencies in WSL:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

2. Clone or download this repository to your WSL home directory:
```bash
git clone <repository-url> ~/projects/tennis_reservations
```

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

### Windows Shortcut Setup

1. Right-click on your Windows desktop
2. Select "New" > "Shortcut"
3. In the location field, paste:
```
C:\Windows\System32\wsl.exe python3 /home/pyanni/projects/tennis_reservations/tennis_gui.py
```
4. Click "Next"
5. Name it "Tennis Reservation"
6. Click "Finish"
7. (Optional) Right-click the shortcut, select "Properties" > "Change Icon" to add a custom icon

### Using the Windows Shortcut

1. Double-click the "Tennis Reservation" shortcut on your desktop
2. The GUI application will open in WSL
3. Fill in your desired date and time
4. Click "Open Reservation Page"

## Project Structure

- `tennis_gui.py` - GUI application
- `open_tennis_url.py` - Command-line interface
- `README.md` - Documentation

## Troubleshooting

### Common Issues

1. **Tkinter not found**
   - Solution: Install python3-tk package in WSL
   ```bash
   sudo apt-get install python3-tk
   ```

2. **WSL path issues**
   - Make sure the repository is in the correct WSL directory
   - Update the shortcut path if you moved the repository

3. **Shortcut not working**
   - Verify the WSL path in the shortcut properties
   - Make sure WSL is properly installed and configured

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
