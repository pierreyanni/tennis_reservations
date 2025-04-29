# Tennis Court Reservation Helper

A simple application to quickly open the Montreal tennis court reservation page with pre-filled date and time parameters.

## Features

- GUI interface for easy date and time selection
- Command-line interface for quick access
- Automatic end time calculation (1 hour after start time)
- Windows shortcut support

## Getting Started

### Prerequisites

- Windows 10 or 11
- WSL (Windows Subsystem for Linux) installed
- Python 3.x installed in WSL

### Installation from GitHub

1. **Install WSL (if not already installed)**
   - Open PowerShell as Administrator and run:
   ```powershell
   wsl --install
   ```
   - Restart your computer when prompted

2. **Clone the repository**
   - Open WSL terminal
   - Navigate to your desired directory:
   ```bash
   cd ~/projects
   ```
   - Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tennis-reservations.git
   cd tennis-reservations
   ```

3. **Set up Python virtual environment**
   ```bash
   # Install virtualenv if not already installed
   sudo apt-get install python3-venv

   # Create and activate virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install Python dependencies
   sudo apt-get install python3-tk
   ```

4. **Create Windows shortcut**
   - Right-click on your Windows desktop
   - Select "New" > "Shortcut"
   - In the location field, paste (adjust the path to match your WSL username):
   ```
   C:\Windows\System32\wsl.exe bash -c "cd /home/YOUR_WSL_USERNAME/projects/tennis-reservations && source venv/bin/activate && python3 tennis_gui.py"
   ```
   - Click "Next"
   - Name it "Tennis Reservation"
   - Click "Finish"

### Verifying Installation

1. Double-click the "Tennis Reservation" shortcut on your desktop
2. The GUI should open with:
   - Today's date pre-filled
   - Start time field (default: 9)
   - Optional end time field
3. Try entering a date and time to verify it opens the reservation page

## Usage

### GUI Application

1. Run the GUI application:
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
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
# Make sure you're in the virtual environment
source venv/bin/activate
python3 open_tennis_url.py 2024-03-21 9 10
```

Arguments:
1. Date (YYYY-MM-DD)
2. Start time (can be just the hour or HH:MM)
3. End time (optional, defaults to 1 hour after start time)

## Troubleshooting

### Common Issues

1. **WSL not installed**
   - Follow the WSL installation steps above
   - Make sure to restart your computer after installation

2. **Virtual environment issues**
   - Make sure you've activated the virtual environment before running the script
   - If you get "command not found" errors, try reactivating the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. **Tkinter not found**
   - Solution: Install python3-tk package in WSL
   ```bash
   sudo apt-get install python3-tk
   ```

4. **Shortcut not working**
   - Verify the WSL path in the shortcut properties matches your setup
   - Make sure you used the correct WSL username in the path
   - Check that WSL is properly installed and configured
   - Ensure the virtual environment is properly set up

5. **Repository not found**
   - Make sure you have the correct repository URL
   - Verify your internet connection
   - Check that you have permission to access the repository

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
