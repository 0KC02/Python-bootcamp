import os
import sys
import webbrowser
import subprocess

# List of files to open
files = [r'C:\path\to\file1.txt', r'C:\path\to\file2.pdf']

# List of applications to open (specify full paths if needed)
apps = [r'notepad.exe', r'calc.exe']  # Notepad and Calculator

# List of URLs to open in the browser
urls = ['https://www.google.com', 'https://www.github.com']

def open_things():
    """
    Opens all specified files, applications, and URLs.
    """
    print("Opening files...")
    for file_path in files:
        if os.path.exists(file_path):
            print(f"Opening {file_path}...")
            os.startfile(file_path)  # Open file with default application
        else:
            print(f"File not found: {file_path}")

    print("\nOpening applications...")
    for app in apps:
        print(f"Launching {app}...")
        subprocess.Popen(app, shell=True)  # Launch application

    print("\nOpening URLs...")
    for url in urls:
        print(f"Opening {url}...")
        webbrowser.open(url)

def close_things():
    """
    Closes all specified applications and the browser.
    """
    print("\nClosing applications...")
    for app in apps:
        app_name = os.path.basename(app)  # Extract executable name
        print(f"Closing {app_name}...")
        os.system(f"taskkill /IM {app_name} /F")  # Force close application

    print("\nClosing browser...")
    os.system("taskkill /IM chrome.exe /F")  # Close Chrome browser

# Main execution block
if len(sys.argv) != 2:
    print('Usage: python workspace_manager.py <start|end>')
    sys.exit(1)

command = sys.argv[1].lower()

if command == 'start':
    open_things()
elif command == 'end':
    close_things()
else:
    print('Invalid command. Please use "start" or "end".')
