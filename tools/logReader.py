import os
import time

# Flags are a quality-of-life update to the log reader.
# For example, you can hide or blur certain distracting keys using faintKeys or hideKeys!
# You can also filter out (most) game keys using the hideWASD flag.
class flags:
    hideWASD = True

    boldKeys = False
    faintKeys = True
    hideKeys = False
    keyList = [
        "backspace",
        "space",
        "delete",
        "shift",
        "media_volume_mute",
        "media_volume_up",
        "media_volume_down",
        "left",
        "right",
        "up",
        "down",
        "ctrl_l",
        "ctrl_r",
        "tab",
        "insert"
    ]

os.system("cls")
if not os.path.exists("ids"):
    input("ERROR: No logs saved. ")
    exit()

while True:
    print("[Choose ID]")
    for i in os.listdir("./ids/"):
        print(f"  - [{os.listdir('./ids/').index(i)+1}] {i}")
    try:
        id = os.listdir("./ids/")[int(input("> "))-1]
        os.system("cls")
    except:
        input("\nERROR: ID not found. ")
        os.system("cls")
        exec(open("logReader.py","r").read())
    
    print("[Choose Date]")
    for i in os.listdir(f"./ids/{id}"):
        print("  - ["+str(os.listdir(f'./ids/{id}').index(i)+1)+f"] {i.replace('-','/')}")
    try:
        date = os.listdir(f"./ids/{id}")[int(input("> "))-1]
        os.system("cls")
    except:
        input("\nERROR: Date not found. ")
        os.system("cls")
        exec(open("logReader.py","r").read())

    print("[Choose Time]")
    for i in os.listdir(f"./ids/{id}/{date}"):
        print("  - ["+str(os.listdir(f'./ids/{id}/{date}').index(i)+1)+f"] {i.replace('.log','').replace('-',':')}")
    try:
        time = os.listdir(f"./ids/{id}/{date}")[int(input("> "))-1]
        os.system("cls")
    except:
        input("\nERROR: Time not found. ")
        os.system("cls")
        exec(open("logReader.py","r").read())
    
    print("[Log]")
    log = open(f"./ids/{id}/{date}/{time}","r").read()
    if flags.boldKeys == True:
        for i in flags.keyList:
            log = log.replace(i,f"\033[4m{i}\033[0m")
    if flags.faintKeys == True:
        for i in flags.keyList:
            log = log.replace(i,f"\033[2m{i}\033[0m")
    if flags.hideKeys == True:
        for i in flags.keyList:
            log = log.replace(i,"").replace("  "," ")
    if flags.hideWASD == True:
        log = log.replace("ww","").replace("aa","").replace("ss","").replace("dd","").replace("WW","").replace("AA","").replace("SS","").replace("DD","").replace("  "," ")
    print(log)
    input("\nPress ENTER to read another log. ")
    os.system("cls")