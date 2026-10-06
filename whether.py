import requests

city = input("Enter city: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)

data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

print("Latitude:", latitude)
print("Longitude:", longitude)

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

temperature = weather_data["current"]["temperature_2m"]

print("Temperature:", temperature, "°C")