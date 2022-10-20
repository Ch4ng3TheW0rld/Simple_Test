from urllib import request
import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import json
import pytest
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
            return token,res.status_code
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
            return token,res.status_code
    return False



#--------------------Review Data
# if __name__ == '__main__':
    
#     data = {"email": "eve.holt@reqres.in","password": "pistol"}
    
#     try:
#         url = sys.argv[1].strip()
#     except IndexError:
#         print("[-] Use example: python3 %s 'url'" % sys.argv[0])
#         sys.exit(-1)
#     print("[+] API Test for Register & Login")

#     # Register
#     register_token,status = Register(url,data)    
#     if register_token:
#         print("[+] Register Token is {}".format(register_token))    
#     else:
#         print("[+] Register Failed")
#         sys.exit(-1)

#     # Login
#     login_token,status = Login(url,data)    
#     if login_token:
#         # token = login
#         print("[+] Login Token is {}".format(login_token))    
#     else:
#         print("[+] Login Failed")
#         sys.exit(-1)



# -------------------------Test Report
test_url = "https://reqres.in"
test_data = {"email": "eve.holt@reqres.in","password": "pistol"}

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_Register():
    test_token,test_status = Register(test_url,test_data)
    print("Test Registered Token is: {}".format(test_token))
    assert len(test_token) != 0
    assert test_status==200

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_Login():
    test_token,test_status = Login(test_url,test_data)
    print("Test Login Token is: {}".format(test_token))
    assert len(test_token) != 0
    assert test_status==200