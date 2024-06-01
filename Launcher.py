import os
import subprocess

# Paths to the game and the mod
mhw_path = r"input path here"
hunterpie_path = r"input path here"

def launch(mhw_path, hunterpie_path):
    if os.path.exists(mhw_path):
        if os.path.exists(hunterpie_path):
            # Launch HunterPie first
            subprocess.Popen([hunterpie_path])
            print(f"HunterPie launched from {hunterpie_path}.")
            
            # Launch Monster Hunter World
            subprocess.Popen([mhw_path])
            print(f"Monster Hunter World launched from {mhw_path}.")
        else:
            print(f"HunterPie path {hunterpie_path} does not exist.")
    else:
        print(f"Monster Hunter World path {mhw_path} not found.")

if __name__ == "__main__":
    # Launch both applications
    launch(mhw_path, hunterpie_path)
