import subprocess
import sys
import os

def install_modules(modules):
    for module in modules:
        print(f"Installing : {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

modules_to_install = ['pandas', 'numpy']

current_folder = os.path.dirname(os.path.abspath(__file__))
script_folder = os.path.join(current_folder, 'scripts')

install_modules(modules_to_install)