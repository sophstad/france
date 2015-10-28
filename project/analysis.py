import json, os, requests

with open('data.json') as data_file:
    data = json.load(data_file)

def metro():
    ''' Calculate average metro rides per day '''
    metro_rides = 0
    day_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'How many times did you ride the metro today?':
                    metro_rides += int(response['numericResponse'])
                    day_counter += 1
    metro_average = metro_rides / float(day_counter)
    return metro_average

def working():
    ''' Find percentage of time working to display in pie chart '''
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
    ''' Calculate average temperature '''
    temperature = 0
    day_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            try:
                temperature += snapshot['weather']['feelslikeF']
                day_counter += 1
            except KeyError: pass
    temperature_average = temperature / float(day_counter)
    return temperature_average

def weather():
    ''' Total number of clear days '''
    clear = 0
    day_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            try:
                if snapshot['weather']['weather'] == 'Clear':
                    clear += 1
                if snapshot['weather']['weather'] is not None:
                    day_counter += 1
            except KeyError: pass
    sunny_days = 100 * clear / float(day_counter)
    return sunny_days

def coffee():
    ''' Calculates average coffees per day '''
    coffees = 0
    day_counter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'How many coffees did you have today?':
                    coffees += int(response['numericResponse'])
                    day_counter += 1
    coffee_average = coffees / float(day_counter)
    return coffee_average

def activities():
    ''' Calculates and displays most common activities ''' 
    activity_list = []
    activity_dict = {}
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'What are you doing?':
                    try:
                        activity_list.append(response['tokens'][0]['text'])
                    except KeyError: pass

    # Remove unwanted list items, combine similar responses
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
    ''' Get most common artists from Last.fm ''' 
    music_list = []
    music_dict = {}
    i = 1
    while i <= 5:
        lastfm_url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=sw1m97&api_key=dfc0d3f11ee15ab2f914558029a4896c&format=json&from=1433635200&to=1437814800&limit=200&page={}'.format(i)
        api = requests.get(lastfm_url).json()
        for recent_track in api['recenttracks']['track']:
            music_list.append(recent_track['artist']['#text'])
        i += 1

    for item in music_list:
        if item in music_dict:
            music_dict[item] += 1
        else:
            music_dict[item] = 1

    j = 0 # delete least-listened artists from dictionary
    while j < 110:
        del music_dict[min(music_dict, key=music_dict.get)]
        j += 1

    return music_dict

def locations():
    ''' Get location types from Foursquare '''
    location_keys = []
    location_types = []
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                try:
                    if response['questionPrompt'] == 'Where are you?':
                        location_keys.append(response['locationResponse']['foursquareVenueId'])
                except KeyError: pass

    for place in location_keys:
        location_url = 'https://api.foursquare.com/v2/venues/{}?client_id=FH5CJJBXKZNKBHFXW0ZX35LPNGZJFHZAT1FE3HTNNT5RAWI4&client_secret=XAGPXZL23RJMDSNLSVJW01QFF0LDHAN1IRVGIW3MCQQDPW1P&v=20130815'.format(place)
        api2 = requests.get(location_url).json()
        for location in api2['response']['venue']['categories']:
            location_types.append(str(location['name']))

    return location_types