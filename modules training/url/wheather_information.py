import argparse
import json
import pprint
import urllib.request


def wheather_data(city):
    wheather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=c8381001d25d70edbdadb3d6444f44e5'.format(city = city)

    with urllib.request.urlopen(wheather_api_url) as wheather_json_file:
        wheather_information = json.loads(wheather_json_file.read().decode())

    return wheather_information


def main():
    # pprint.pprint(wheather_information)

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", help = "City from which temperature info will be obtain.")

    args = parser.parse_args()

    # city = input("Please enter city: ")

    city = args.city

    wheather_information = wheather_data(city)

    print("Temperature in {city} is {temp}".format(temp = wheather_information['main']['temp'], city = city))

if __name__ == "__main__":
    main()
