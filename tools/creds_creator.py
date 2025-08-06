import requests
import zlib
import base64
import os

try:
    if not os.path.exists("creds.sav"):
        username = input("[Credential Server Creator]\nEnter username: ")
        password = input("Enter password: ")
        key = input("Enter API key: ")
    else:
        option = input("The file 'creds.sav' was found containing credentials (to be stored). Use them (y/n)? ").lower()
        if option == "y" or "yes" in option:
            exec(open("creds.sav","r").read())
        else:
            os.system("cls")
            username = input("[Credential Server Creator]\nEnter username: ")
            password = input("Enter password: ")
            key = input("Enter API key: ")

    print("\nNearly there! Now, enter the credentials for the account you are saving the server to.")
    username_1 = input("Enter username: ")
    password_1 = input("Enter password: ")
    key_1 = input("Enter API key: ")
    compress = f"key,username,password = '{key}','{username}','{password}'"
    compress = eval('b"'+compress+'"')
    compress = zlib.compress(compress)

    login_data = {
        'api_dev_key': key_1,
        'api_user_name': username_1,
        'api_user_password': password_1
    }
    data = {
        'api_option': 'paste',
        'api_dev_key': key_1,
        'api_paste_code': str(compress),
        'api_paste_name': "KYLGR-CREDS",
        'api_paste_expire_date': 'N',
        'api_user_key': None,
        'api_paste_private': '1'
    }

    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    data['api_user_key'] = login.text
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    print(f"\nStatus Code: {r.status_code}")
except Exception as e:
    os.system("cls")
    input(f"ERROR: {e} ")
    exit()

input("\nServer successfully created! ")
