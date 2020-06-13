import requests
import json
from datetime import datetime


now = datetime.now() # current date and time
today = now.strftime("%Y-%m-%d")

def getDatasFromAPI (parameters):
    params = ""
    url = "https://api.orhanaydogdu.com.tr/deprem/index.php?"
    if not "date" in parameters: 
        params = "date="+today+"&"
    
    for param,value in parameters.items():
        params = params+param+"="+value
        params = params+"&"
        
    url = url+params
    response = requests.get(url)
    #returns "status" and "results". Results includes earthquakes 
    jsonResult = json.loads(response.text)
    return jsonResult["result"]

