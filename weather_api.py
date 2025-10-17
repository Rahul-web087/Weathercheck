import requests
city_name = 'Jajpur'
api_key = '2146f3d92970f96826eef505c22d4b36'
url =f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Weather is ",data["weather"][0]["description"])
    print("Temperature is ",data["main"]["temp"])
    print("Humidity is ",data["main"]["humidity"])
    print("Wind Speed is ",data["wind"]["speed"])
    print("Wind Direction is ",data["wind"]["deg"])
    print("Weather Condition is ",data["weather"][0]["main"])
    print("Weather Condition is ",data["weather"][0]["description"])