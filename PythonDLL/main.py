import json
import requests

url = "http://121.37.153.74:8091/api/user/login?username=17344050960&password=E10ADC3949BA59ABBE56E057F20F883E&baseCode=100000"

payload = ""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)
token=response.headers.get("Authorization")
# print(response.text)
url = "http://121.37.153.74:8091/api/baseStation/getBaseSettings"
payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': token,
  'DateString': '2021-05-19 09:52:16'
}

response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)
# import requests
# import json

url = "http://121.37.153.74:8091/api/sampleCheck/swiping?cardNum=112233"

payload = json.dumps({
  "page": 1,
  "pageSize": 5,
  "timeStart": "2020-12-01 00:00:00",
  "timeEnd": "2021-01-01 00:00:00"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': token
}
response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
categoryId=response.text[416:418]
# import requests

url = "http://121.37.153.74:8091/api/sampleCheck/categorySelect?categoryId=19"

payload={}
headers = {
  'Authorization': token
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
# import requests
import json
Water = str(12)
# url = "http://121.37.153.74:8091/api/sampleCheck/budgetedPrice?a=13.5&l=&categoryId=19"
url = "http://121.37.153.74:8091/api/sampleCheck/budgetedPrice?a=" + Water +"&l=&categoryId=19"
payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
