import requests
import time

location_id = "8720"
city = "Braga"

# change date_from and date_to to get different time periods
# query for 2015-2018 and 2018-2020 and 2020-2023, separated because of the large amount of data
# in case of 'connection timeout' error, try again with a smaller time period or query for a single period istead of 3

url = f"https://api.openaq.org/v2/measurements?format=csv&date_from=2015-01-01&date_to=2018-01-01&limit=100000&page=1&offset=0&sort=desc&radius=1000&country_id=PT&country=PT&city={city}&location_id={location_id}&order_by=datetime"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

with open(f"{city}_{location_id}_2015_2018.csv", "w") as f:
    f.write(response.text)

time.sleep(2)

url = f"https://api.openaq.org/v2/measurements?format=csv&date_from=2018-01-01&date_to=2020-01-01&limit=100000&page=1&offset=0&sort=desc&radius=1000&country_id=PT&country=PT&city={city}&location_id={location_id}&order_by=datetime"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

with open(f"{city}_{location_id}_2018_2020.csv", "w") as f:
    f.write(response.text)

time.sleep(2)

url = f"https://api.openaq.org/v2/measurements?format=csv&date_from=2020-01-01&date_to=2023-01-01&limit=100000&page=1&offset=0&sort=desc&radius=1000&country_id=PT&country=PT&city={city}&location_id={location_id}&order_by=datetime"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

with open(f"{city}_{location_id}_2020_2023.csv", "w") as f:
    f.write(response.text)
