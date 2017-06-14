import urllib.request
import json
import pprint

city = input("Please enter city: ")
wheather_api_url = 'http://samples.openweathermap.org/data/2.5/weather?q={city}&appid=c8381001d25d70edbdadb3d6444f44e5'.format(city = city)

with urllib.request.urlopen(wheather_api_url) as wheather_json_file:
    wheather_information = json.loads(wheather_json_file.read().decode())

pprint.pprint(wheather_information)