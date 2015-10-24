import json, operator

with open('data.json') as data_file:
    data = json.load(data_file)

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

print(activity_dict)