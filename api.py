import requests

r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ican&tanggal=10-08-1990')

data =r.json()

print(data['data']['nama'])

tgl = []

for x in range(0,31):
    tgl.append((x))

print(tgl)