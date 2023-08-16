import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_jsonp.js'
response= requests.get(url)
data = response.text[response.text.index("{"):response.text.rindex("}")+1] 
parsed_data = json.loads(data)
usd_value= parsed_data['Valute']['USD']['Value']
mdl_value= parsed_data['Valute']['MDL']['Value']
aud_value= parsed_data['Valute']['AUD']['Value']



print(f'Курс доллара США: {usd_value} рублей')
print(f'Курс Молдавскоко лея: {usd_value} рублей')
print(f'Курс Австралийского доллара: {usd_value} рублей')
