import argparse

parser = argparse.ArgumentParser()
# hier koenntest du auch nur valide Windrichtungen
parser.add_argument('-w', '--windrichtung', choices=['N','NNO','NO','ONO','O','OSO','SO','SSO','S','SWS','SW','WSW','W','NNW','NW','WNW'], required=True)
parser.add_argument('-we', '--wetter', choices=['b','r','s'],required=True)
parser.add_argument('-temp', '--temperatur', choices=['20','21','22','23','24','25','26','27','28','29','30'],required=True)

args = parser.parse_args()

windrichtung_mapping = {
    'N': -3.5,
    'NNO': -3.2,
    'NO': -2.4,
    'ONO': -1.4,
    'O': 1,
    'OSO': 1.2,
    'SO': 2.1,
    'SSO': 2.7,
    'S': 3,
    'SWS': 2.7,
    'SW': 2.1,
    'WSW': 1.2,
    'W': 1,
    'NNW': -3.2,
    'NW': -2.4,
    'WNW': -1.4
}

wetter_mapping = {
    'r': -0.07,
    'b': -0.13,
    's': 0
}

temperatur_mapping = {
    '20' : -0.01,
    '21' : -0.01,
    '22' : -0.01,
    '23' : -0.01,
    '24' : 0,
    '25' : 0,
    '26' : 0,
    '27' : 0.01,
    '28' : 0.01,
    '29' : 0.01,
    '30' : 0.01
}

def get_wetter_effekt (wetter):
    return wetter_mapping [wetter]
def get_temperatur_effekt (temperatur):
    return temperatur_mapping [temperatur]
def get_windrichtung_effekt(windrichtung):
    return windrichtung_mapping[windrichtung]


print(get_windrichtung_effekt(args.windrichtung))
print(get_temperatur_effekt(args.temperatur))
print(get_wetter_effekt(args.wetter))
