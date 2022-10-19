from urllib import request
import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def Register(url,data):
    try:
        res = requests.post(url+"/api/register", data=data, verify=False, timeout=5)
        res.raise_for_status()
    except requests.exceptions.Timeout as errt:
        print("[-]",errt)
    except requests.exceptions.HTTPError as errh:
        print("[-]",errh)
    except requests.exceptions.ConnectionError as errc:
        print("[-]",errc)
    except requests.exceptions.RequestException as err:
        print("[-]",err)
    else:
        for i in range(2):
            print("+")
        print("[+] Status:",res.status_code, "User was Registered")
        print(res.json())    

        if "token" in res.json():
            token = res.json()['token']
            return token
    return False


def Login(url,data):
    try:
        res = requests.post(url+"/api/login", data=data, verify=False, timeout=5)
        res.raise_for_status()
    except requests.exceptions.Timeout as errt:
        print("[-]",errt)
    except requests.exceptions.HTTPError as errh:
        print("[-]",errh)
    except requests.exceptions.ConnectionError as errc:
        print("[-]",errc)
    except requests.exceptions.RequestException as err:
        print("[-]",err)
    else:
        for i in range(2):
            print("+")
        print("[+] Status:",res.status_code, "Success LogIn")
        print(res.json())    

        if "token" in res.json():
            token = res.json()['token']
            return token
    return False



if __name__ == '__main__':
    
    data = {"email": "eve.holt@reqres.in","password": "pistol"}
    
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Use example: python3 %s 'url'" % sys.argv[0])
        sys.exit(-1)
    print("[+] API Test for Register & Login")

    # Register
    register = Register(url,data)    
    if register:
        token = register
        print("[+] Register Token is {}".format(token))    
    else:
        print("[+] Register Failed")
        sys.exit(-1)

    # Login
    login = Login(url,data)    
    if login:
        token = login
        print("[+] Login Token is {}".format(token))    
    else:
        print("[+] Login Failed")
        sys.exit(-1)
