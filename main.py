import json

with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

following = []
for f in following_json['relationships_following']:
    following.append(f['string_list_data'][0]['value'])

for f in followers_json:
    if f['string_list_data'][0]['value'] in following:
        following.remove(f['string_list_data'][0]['value'])

for account in following:
    print(account)
    print()
