from asyncio import QueueEmpty
from datetime import date
import mailbox
from re import A
import socket
from types import CoroutineType
from urllib import response
from getmac import get_mac_address as gma

import json 
import requests 



company_name=''
phone_number=''
email=''
er=''

def add_data():
    global mac
    global ip 
    mac=gma()
    hostname = socket.gethostname()   
    ip = socket.gethostbyname(hostname)   
    global er
    er=''

    global company_name
    global phone_number
    global email
   
    # company_name=input("Enter Your Company Name=")
    # phone_number=input("Enter Your Phone Number=")
    # email=input("Enter Your E-mail=")
    print("=================================")
    print("Your Company Name=",company_name)
    print("Your Phone Number=",phone_number)
    print("Your E-mail=",email)

    mac=gma()




    URL="https://3duser.infiniteai.co.in/api/login" 

    data= {
        "name": company_name,
        # "username":u,8000705534 test2@infiniteai.com
        "mobile": phone_number,
        "email": email,     
    } 


    global r
    r=requests.post(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' })
   
    # print("error") 

    print("====================== api data ======================")

    # print(r.json()) 
    global datas
# user_name ===========
# address==============
#   company_name
#   phone_number
#   mail
#   license type
#   Qty
# registration date
# expiry date
# system mac
    datas=r.json() 
    global customer_name
    global address1
    global state
    global city
    global pincode
    
    if('details' in datas):
        print("yes")
        customer_name=datas['details']['customer_name']
        address1=datas['details']['address1']
        state=datas['details']['state']
        city=datas['details']['city']
        pincode=datas['details']['pincode']
        global id
        id=datas['details']['id']
        print("===================== Message =======================")
        print("===================== show data =======================")
        print('customer_name => ',customer_name)    
        print('address1 => ',address1)
        print('state => ',state)
        print('city => ',city)
        print('pincode => ',pincode)
    else:
        er=datas['Message']
        # print(er)
    
   

    print("===================== show all data =======================")
    # print('customer_name => ',customer_name)    
    # print('address1 => ',address1)
    # print('company name => ',company_name)
    # print('phone number => ',phone_number)
    # print('mail => ',email)


# add_data()


def show(): 

    URL="https://3duser.infiniteai.co.in/api/key-generate"

    data= {

        "id":id,
        "ip_address":ip,
        "mac_address":mac,   
    } 

    
    rs=requests.post(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' }) 

    print("===================== mac =======================")
    print(rs.json()) 
    global data_key 
    data_key=rs.json() 

    print("===================== key =======================")


    global key
    key=data_key['Key']
    print(key)







# show()




def v_key(): 
    URL="https://3duser.infiniteai.co.in/api/key-verify" 

    data= {
        "id": id,
        # "username":u,8000705534 test2@infiniteai.com
        "key": key,
        # "email": email,     
    } 

    
    
    ro=requests.post(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' }) 

    print("====================== key data ======================")

    print(ro.json()) 
# user_name ===========
# address==============
#   company_name
#   phone_number
#   mail
#   license type
#   Qty
# registration date
# expiry date
# system mac
    global data1
    data1=ro.json() 


    startdate=data1['Startdate']
    enddate=data1['Enddate']
    # state=datas['details']['state']
    # city=datas['details']['city']
    # pincode=datas['details']['pincode']
    # global id
    # id=datas['details']['id']

    
    print("===================== show data =======================")
    print('customer_name => ',startdate)    
    print('address1 => ',enddate)
    # print('state => ',state)
    # print('city => ',city)
    # print('pincode => ',pincode)



# v_key()


