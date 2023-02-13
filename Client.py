import requests
import urllib.parse
import base64
main_api="http://www.mapquestapi.com/directions/v2/route?"
orig="Moscow"
dest="Bali"
key=open("E:\KEY API.txt","r")
encode_key=base64.b64encode(bytes(key.read(),'utf-8'))
key.close()
decode_key=base64.b64decode(encode_key)
url=main_api+urllib.parse.urlencode({"key":decode_key,"from":orig,"to":dest})
json_data=requests.get(url).json()

print(json_data)


