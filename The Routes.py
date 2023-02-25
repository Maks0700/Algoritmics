import urllib.parse
import requests
main_api="http://www.mapquestapi.com/directions/v2/route?"
key=open("E:\KEY API.txt","r")
while True:
    orig=input("Enter the original: ")
    if orig=="q"or orig=="Q":
        break
    dest=input("Enter the destination: ")
    if dest=="q" or dest=="Q":
        break
    url=main_api+urllib.parse.urlencode({"key":key.read(),"from":orig,"to":dest})
    print("URL: "+url)
    json_data=requests.post(url).json()
    json_status=json_data["info"]["statuscode"]
    if json_status==0:
        print("API status "+str(json_status)+" = a successful.\n")



