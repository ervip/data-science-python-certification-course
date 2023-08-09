"""
Write a program to find the distance between two locations when their latitude and longitudes are given.
"""

from math import radians, sin, cos, asin, sqrt


def distance(location1, location2):
    lat1, lon1 = tuple(map(radians, location1))
    lat2, lon2 = tuple(map(radians, location2))
    a = sin((lat2 - lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1)/2)**2
    c = 2 * asin(sqrt(a))
    return c * 6371 # Kilometers, use 3956 for miles


def get_lat_lon(message):
    lat, lon = input(message).split()
    return float(lat), float(lon)


if __name__ == '__main__':
    lat1, lon1 = get_lat_lon("Enter latitude and longitude for first location (separated by space): ")
    lat2, lon2 = get_lat_lon("Enter latitude and longitude for second location (separated by space): ")
    print(f"Distance between two locations: {distance((lat1, lon1), (lat2, lon2)):.2f} KM")