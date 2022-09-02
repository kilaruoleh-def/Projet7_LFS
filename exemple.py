import requests
import json

url = "http://127.0.0.1:8000/predict"

payload = json.dumps({
    "AMT_CREDIT" : -0.075097,
    "AMT_ANNUITY" : -0.451790,
    "AMT_GOODS_PRICE" : -0.239153,
    "REGION_POPULATION_RELATIVE" : -0.145910,
    "DAYS_BIRTH" : 0.734193,
    "DAYS_ID_PUBLISH" : 1.445696,
    "OCCUPATION_TYPE" : 0.028118,
    "WEEKDAY_APPR_PROCESS_START" : 0.888235,
    "HOUR_APPR_PROCESS_START" : 1.817788,
    "EXT_SOURCE_1" : 1.781131,
    "EXT_SOURCE_2" : 1.441565,
    "EXT_SOURCE_3" : -2.038369,
    "AMT_REQ_CREDIT_BUREAU_YEAR" : -1.007331
})
headers = {
    'Content-Type' : 'application/json'
}
response = requests.post(url, headers = headers, data = payload)
print(response.json())
