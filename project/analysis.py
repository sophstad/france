import json, os, requests

with open('data.json') as data_file:
    data = json.load(data_file)

def metro():
    '''Calculate average metro rides per day'''
    metros = 0
    metro_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'How many times did you ride the metro today?':
                    metros += int(response['numericResponse'])
                    metro_counter += 1
    metro_average = metros / metro_counter
    return metro_average

def working():
    '''Find percentage of days working'''
    not_working = 0
    yes_working = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'Are you working?':
                    if response['answeredOptions'][0] == 'Yes':
                        yes_working += 1
                    elif response['answeredOptions'][0] == 'No':
                        not_working += 1
    return yes_working, not_working

def temperature():
    '''Calculate average temperature'''
    temperature = 0
    temperature_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            try:
                temperature += snapshot['weather']['feelslikeF']
                temperature_counter += 1
            except KeyError: pass
    temperature_average = temperature / temperature_counter
    return temperature_average

def weather():
    '''Total number of clear days'''
    clear = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            try:
                if snapshot['weather']['weather'] == 'Clear':
                    clear += 1
            except KeyError: pass
    return clear

def activities():
    '''Display common activities''' 
    activity_list = []
    activity_dict = {}
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'What are you doing?':
                    try:
                        activity_list.append(response['tokens'][0]['text'])
                    except KeyError: pass

    # Remove unwanted list items
    i = 0
    for item in activity_list:
        if item == u'\U0001F341':
            activity_list.remove(item)
        if item == 'On the subway' or item == 'On the bus':
            activity_list[i] = 'Commuting'
        i += 1

    for item in activity_list:
        if item in activity_dict:
            activity_dict[item] += 1
        else:
            activity_dict[item] = 1
    return activity_dict

def music():
    '''Display common music''' 
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
    while j < 110:
        del music_dict[min(music_dict, key=music_dict.get)]
        j += 1

    return music_dict