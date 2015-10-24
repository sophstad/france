import json

with open('project/data.json') as data_file:
    data = json.load(data_file)

def metro():
    metros = 0
    metroCounter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'How many times did you ride the metro today?':
                    metros += int(response['numericResponse'])
                    metroCounter += 1
    metroAverage = metros / metroCounter
    return metroAverage

def working():
    notWorking = 0
    yesWorking = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'Are you working?':
                    if response['answeredOptions'][0] == 'Yes':
                        yesWorking += 1
                    elif response['answeredOptions'][0] == 'No':
                        notWorking += 1
    return yesWorking, notWorking

def temperature():
    temperature = 0
    temperatureCounter = 0
    for report in data['reports']:
        for snapshot in report['snapshots']:
            try:
                temperature += snapshot['weather']['feelslikeF']
                temperatureCounter += 1
            except KeyError: pass
    temperatureAverage = temperature / temperatureCounter
    return temperatureAverage

def activities():   
    activity_list = []
    activity_dict = {}
    for report in data['reports']:
        for snapshot in report['snapshots']:
            for response in snapshot['responses']:
                if response['questionPrompt'] == 'What are you doing?':
                    try:
                        activity_list.append(response['tokens'][0]['text'])
                    except KeyError: pass

    for item in activity_list:
        if item == '\U0001F341':
            activity_list.remove(item)

    for item in activity_list:
        if item in activity_dict:
            activity_dict[item] += 1
        else:
            activity_dict[item] = 1
    return activity_dict