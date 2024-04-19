import requests

state_abbr = input("To look up weather alerts in your state, enter in your states abbreviation: ")
state_abbr = state_abbr.upper()
apiurl = "https://api.weather.gov/alerts/active"

result = requests.get(apiurl, params={"area": f"{state_abbr}"}).json()

for item in result['features']:
	print("...Weather Alert...")
	print("\n")
	print(item['properties']['description'])
	print("\n")
