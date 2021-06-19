import requests

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
  'applicationId':1071977349781880110,
  'shopCode':'frenz2',
  'page':1,
  'hits':2,
}

r = requests.get(url,params=payload)
resp = r.json()

for i in resp['Items']:
  item = i['Item']
  name = item['itemName']
  price = item['itemPrice']

  print(name)
  print(price)
