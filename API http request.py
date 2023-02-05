import requests
import urllib.parse
main_api="http://www.mapquestapi.com/directions/v2/route?"
orig="Washington"
dest="Baltiamore"
key="BoKo0vhLFsYGEzn10FEU4Ll9gZHjrBo4"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data=requests.get(url).json()
print(json_data)


 

 

 
