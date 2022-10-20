import requests
import urllib3
import json
import pytest
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
        for i in range(1):
            print("+")
        print("[+] Status:",res.status_code,"User was created")
        # print("[+] User was created")
        print(res.json())    

        if "id" in res.json():
            id = res.json()['id']
            return id,res.status_code
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
        for i in range(1):
            print("+")
        print("[+] Status:",res.status_code)
        print("[+] Retrieved data of id:{}".format(id))
        print(json.dumps(res.json(), indent=4))
        return res.status_code


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
        for i in range(1):
            print("+")
        print("[+] Status:",res.status_code, "User was updated")
        print(res.json())
        return res.status_code    


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
        for i in range(1):
            print("+")
        print("[+] Status:",res.status_code, "User was deleted")
        return res.status_code


# if __name__ == '__main__':
    
#     data = {"name": "morpheus","job": "leader"}
    
#     try:
#         url = sys.argv[1].strip()
#     except IndexError:
#         print("[-] Use example: python3 %s 'url'" % sys.argv[0])
#         sys.exit(-1)
#     print("[+] API Test tool, create user: morpheus, retrieve user data, update then delete user")

#     # Create User
#     createuser = CreateUser(url,data)    
#     if createuser:
#         for i in range(2):
#             print("+")
#         id = createuser
#         print("[+] User id is {}".format(id))
#         retrieveuser = RetrieveUser(url,id)    
#     else:
#         print("[+] Creation Failed")
#         sys.exit(-1)

#     # Get User
#     print("[+] Try Fixed id = 2")
#     retrieveuser = RetrieveUser(url,2)    

#     # Update User
#     data={"name": "morpheus","job": "zion resident"}
#     updateuser = UpdateUser(url,data)


#     deleteuser = DeleteUser(url)



# -------------------------Test Report
test_url = "https://reqres.in/api/users"
test_data = {"email": "eve.holt@reqres.in","password": "pistol"}
test_new_data = {"name": "morpheus","job": "zion resident"}

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_createuser():
    test_id,test_status = CreateUser(test_url,test_data)
    print("Created Test User ID is: {}".format(test_id))
    assert len(test_id) != 0
    assert test_status==201

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_retrieveuser():
    test_status = RetrieveUser(test_url,2)
    assert test_status==200

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_updateuser():
    test_status = UpdateUser(test_url,test_new_data)
    assert test_status==200

@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
def test_deleteuser():
    test_status = DeleteUser(test_url)
    assert test_status==204