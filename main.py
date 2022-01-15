import json
from collections import Counter

# Checking how many times I've listened to Gloryhammer the past year, and how many days
with open('StreamingHistory0.json', 'r', encoding='utf8') as file:
    data = json.load(file)

print(data[:10])

counter_gh = 0
# counter_date = {}
gh_list = []
date_list = []
for item in data:
    if item['artistName'] != 'Gloryhammer':
        continue
    else:
        gh_list.append(item.get('artistName'))
        date = item['endTime'][:11]
        date_list.append(date)
        counter_gh += 1

# TODO can't print number of times listened each day this way - need to implement Counter
occurences = []
for item in date_list:
    if item not in occurences:
        occurences.append(item)

print(occurences)
print(len(occurences))

    # print(item)

# for item in gh_list:
#     print(item)


        # print(date)
        # print(type(date))
        # print(Counter(date))
        # counter_date += 1
        # counter_gh +=1

# print(counter_gh)

    # gloryhammer = item.get('artistName' == 'Gloryhammer')
    # print(gloryhammer)
    # gh_list.append(gloryhammer)
# print(gh_list)

# gloryhammer = data.get('artistname' == 'Gloryhammer')
# print(gloryhammer)