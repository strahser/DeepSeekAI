import subprocess
import sys

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Installation complete. Press Enter to continue...")
    input()
except subprocess.CalledProcessError:
    print("Error installing dependencies. Please install them manually.")
    input()
except FileNotFoundError:
    print("Error: requirements.txt not found.  Please make sure it's in the same directory.")
    input()