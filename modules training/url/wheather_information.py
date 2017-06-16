import argparse
import json
import pprint
import urllib.request

api = 'c8381001d25d70edbdadb3d6444f44e5'

def wheather_data(city):
    wheather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}'.format(city = city, api = api)

    with urllib.request.urlopen(wheather_api_url) as wheather_json_file:
        wheather_information = json.loads(wheather_json_file.read().decode())

    return wheather_information


def main():
    # pprint.pprint(wheather_information)

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", help = "City from which temperature info will be obtain.")
    parser.add_argument("-i", "--input",action = 'store_true', help = "Input from keyboard during execution.")

    args = parser.parse_args()

    if args.input:
        city = input("Please enter city: ")

    city = args.city

    wheather_information = wheather_data(city)

    print("Temperature in {city} is {temp}".format(temp = wheather_information['main']['temp'], city = city))

if __name__ == "__main__":
    main()
