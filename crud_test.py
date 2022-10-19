from urllib import request
import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def CreateUser(url,data):
    try:
        res = requests.post(url, data=data, verify=False, timeout=5)
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
        print("[+] Status:",res.status_code)
        print("[+] User was created")
        print(res.json())    

        if "id" in res.json():
            id = res.json()['id']
            return id
    return False


def RetrieveUser(url,id):
    try:
        if id != 2:
            url = url +"/"+id
        else:
           url = url + "/2" 
        res = requests.get(url,timeout=5)
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
        print("[+] Retrieved id:{} data".format(id))
        print("[+] Status:",res.status_code)
        print(json.dumps(res.json(), indent=4))


def UpdateUser(url,data):
    try:
        res = requests.put(url+"/2", data=data, verify=False, timeout=5)
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
        print("[+] Status:",res.status_code, "User was updated")
        print(res.json())    


def DeleteUser(url):
    try:
        res = requests.delete(url+"/2", verify=False, timeout=5)
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
        print("[+] Status:",res.status_code, "User was deleted")


if __name__ == '__main__':
    
    data = {"name": "morpheus","job": "leader"}
    
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Use example: python3 %s 'url'" % sys.argv[0])
        sys.exit(-1)
    print("[+] API Test tool, create user: morpheus, retrieve user data, update then delete user")

    # Create User
    createuser = CreateUser(url,data)    
    if createuser:
        for i in range(2):
            print("+")
        id = createuser
        print("[+] User id is {}".format(id))
        retrieveuser = RetrieveUser(url,id)    
    else:
        print("[+] Creation Failed")
        sys.exit(-1)

    # Get User
    print("[+] Try Fixed id = 2")
    retrieveuser = RetrieveUser(url,2)    

    # Update User
    data={"name": "morpheus","job": "zion resident"}
    updateuser = UpdateUser(url,data)


    deleteuser = DeleteUser(url)
