import yaml
from yaml import Loader
import googlemaps as gm
from googlemaps import directions


def neighbour(points):
    start = points[0]
    results = []
    for j in points:
        for i in points:
            dirRes = directions(origin=j, destination=i, mode='driving')
            results.append(dirRes)
    print(dirRes)
    return dirRes


with open('config.yaml') as f:
    config = yaml.load(f, Loader=Loader)
    print(config)
points = []

client = gm.Client(config)

# input loop
while True:
    x = input('Type first part of coordinates or type "stop" to finish inputting: ')
    if x == 'stop':
        break
    else:
        x2 = input('Type another part of coordinates')
        points.append([x, x2])
        print(points)
        neighbour(points)