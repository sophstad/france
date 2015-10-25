import json, operator
import requests

with open('data.json') as data_file:
    data = json.load(data_file)

# with open('music.json') as music_file:
#     music = json.load(music_file)

# counter = 0
# for report in data['reports']:
#     for snapshot in report['snapshots']:
#         try:
#             print str(snapshot['location']['longitude']) + ", " + str(snapshot['location']['latitude'])
#             counter += 1
#         except KeyError: pass

# for report in data['reports']:
#     for snapshot in report['snapshots']:
#         for response in snapshot['responses']:
#             try:
#                 print(response['locationResponse']['text'] + ": " + str(response['locationResponse']['location']['latitude']) + ", " + str(response['locationResponse']['location']['longitude']))
#             except KeyError: pass
   

# for recenttrack in music['recenttracks']:
#     for track in recenttrack['track']:
#         print(track['artist']['#text'])

music_list = []
music_dict = {}
i = 1
while i <= 5:
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=sw1m97&api_key=dfc0d3f11ee15ab2f914558029a4896c&format=json&from=1433635200&to=1437814800&limit=200&page={}'.format(i)
    api = requests.get(url).json()
    for recenttrack in api['recenttracks']['track']:
        music_list.append(recenttrack['artist']['#text'])
    i += 1

for item in music_list:
    if item in music_dict:
        music_dict[item] += 1
    else:
        music_dict[item] = 1

j = 0
while j < 120:
    del music_dict[min(music_dict, key=music_dict.get)]
    j += 1

print(music_dict)


# music_list = []
#     music_dict = {}
#     i = 1
#     while i <= 5:
#         url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=sw1m97&api_key=dfc0d3f11ee15ab2f914558029a4896c&format=json&from=1433635200&to=1437814800&limit=200&page={}'.format(i)
#         api = requests.get(url).json()
#         for recenttrack in api['recenttracks']['track']:
#             music_list.append(recenttrack['artist']['#text'])
#         i += 1

#     for item in music_list:
#         if item in music_dict:
#             music_dict[item] += 1
#         else:
#             music_dict[item] = 1

#     for artist, plays in music_dict.items():
#         if plays < 10:
#             del music_dict[artist]
#             