import subprocess
from ahk import AHK

# Replace 'your_script.ahk' with the actual path to your AHK script
ahk_script_path = r'C:\Users\tcamp\Desktop\WildHorseIslands\ScrollMouse.ahk'

# Replace the path with the actual path to AutoHotKey v2 executable
autohotkey_path = r'C:\Users\tcamp\AppData\Local\Programs\AutoHotkey\v2\AutoHotKey64.exe'

ahk_file = AHK(executable_path = autohotkey_path)

# Use subprocess to run the AHK script
subprocess.run([autohotkey_path, ahk_script_path], cwd=r'C:\Users\tcamp\Desktop\WildHorseIslands')
