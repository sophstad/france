import json

with open('data.json') as data_file:
    data = json.load(data_file)

# counter = 0
# for report in data['reports']:
#     for snapshot in report['snapshots']:
#         try:
#             print str(snapshot['location']['longitude']) + ", " + str(snapshot['location']['latitude'])
#             counter += 1
#         except KeyError: pass
# print counter

for report in data['reports']:
    for snapshot in report['snapshots']:
        for response in snapshot['responses']:
            try:
                print response['locationResponse']['text'] + ": " + str(response['locationResponse']['location']['latitude']) + ", " + str(response['locationResponse']['location']['longitude'])
            except KeyError: pass
            