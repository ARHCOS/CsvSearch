import subprocess
import sys
import os

def install_modules(modules):
    for module in modules:
        print(f"Installing : {module}...\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

modules_to_install = ['pandas', 'numpy']

current_folder = os.path.dirname(os.path.abspath(__file__))
script_folder = os.path.join(current_folder, 'scripts')
csv_folder_path = current_folder + "\\CSV"

if not os.path.exists(csv_folder_path):
    os.makedirs(csv_folder_path)
    print("Created the CSV folder\n")
else:
    print("The CSV folder already exists\n")

print("Installing modules...\n")

install_modules(modules_to_install)