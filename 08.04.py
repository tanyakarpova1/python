import requests

url = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

print(url['Valute']['USD']['Name'], end=' '), print(url['Valute']['EUR']['Value'])

print (url['Valute']['EUR']['Name'], end=' '), print(url['Valute']['EUR']['Value'])

print (url['Valute']['CNY']['Name'], end=' '), print(url['Valute']['CNY']['Value'])

print (url['Valute']['JPY']['Name'], end=' '), print(url['Valute']['JPY']['Value'])

print (url['Valute']['BYN']['Name'], end=' '), print(url['Valute']['BYN']['Value'])

