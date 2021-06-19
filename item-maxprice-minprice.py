import requests

url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'

payload = {
  'applicationId':1071977349781880110,
  'genreId':100040,
  'page':1,
  'hits':1,
}

r = requests.get(url,params=payload)
resp = r.json()

for i in resp['Products']:
  product = i['Product']
  name = product['productName']
  maxprice = product['maxPrice']
  minprice = product['minPrice']

  print(f"製品名：{name}")
  print(f"最高値：{maxprice}円")
  print(f"最安値：{minprice}円")
