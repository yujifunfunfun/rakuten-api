import requests
import csv

url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
payload = {
  'applicationId':1071977349781880110,
  'genreId':'100283',
}

r = requests.get(url,params=payload)
resp = r.json()

number = 0

for i in resp['Items']:
  item = i['Item']
  name = item['itemName']
  number += 1

  with open('./ranking.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow([f"{number}位",name])
