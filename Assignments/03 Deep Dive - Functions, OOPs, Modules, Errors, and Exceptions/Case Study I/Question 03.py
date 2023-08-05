"""
Weather forecasting organization wants to show whether is it day or night. So, 
write a program for such an organization to find whether is it dark outside or not.
"""

from urllib.request import urlopen
from re import search
from json import loads
from datetime import datetime


IP_URL = "http://checkip.dyndns.com/"
GEO_URL = "http://ip-api.com/json/{ip}"
WEATHER_URL = "https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date=today&formatted=0"


def get_ip():
    res = str(urlopen(IP_URL).read())
    return search(r'Address: (\d+\.\d+\.\d+\.\d+)', res).group(1)


def get_location(ip):
    res = urlopen(GEO_URL.format(ip=ip)).read()
    return loads(res.decode())


def get_weather_info(lat, lng):
    res = urlopen(WEATHER_URL.format(lat=lat, lng=lng)).read()
    return loads(res.decode())


if __name__ == '__main__':
    try:
        ip = get_ip()
        location = get_location(ip)

        print("Country:", location['country'])
        print("Region:", location['regionName'])
        print("Timezone:", location['timezone'])

        weather = get_weather_info(location['lat'], location['lon'])

        if weather['status'] == 'OK':
            today = datetime.utcnow()
            sunset = datetime.fromisoformat(weather['results']['sunset'])
            if today.date() == sunset.date() and today.time() < sunset.time():
                print("It's light outside.")
            else:
                print("It's dark outside.")

    except Exception as ex:
        print("Something went wrong !!\nUnable to get required information !!\nError:\n", str(ex))