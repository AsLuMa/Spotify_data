import json
import pandas as pd
import math

with open('StreamingHistory0.json', 'r', encoding='utf8') as file:
    data = json.load(file)

df = pd.DataFrame(data)
# print(df.head(10).to_string())

# Group by artist name, get all Gloryhammer-info, sort by name of song, then set index to artist name
group_an = df.groupby(by='artistName')
df_gh = group_an.get_group('Gloryhammer').sort_values(by='trackName')
# print(df_gh.head(10).to_string())
df_gh = df_gh.set_index('artistName')
# print(df_gh.head(10).to_string())

# Find all songs that have been played more than 2 minutes
df_over_12000 = df_gh.loc[df_gh['msPlayed'] > 120000]
print(df_over_12000)


def ms_to_second(ms):
    return math.floor(ms/1000)


exit()

# Finding most frequent songs played without Groupby
df = df.set_index('artistName')
df_gh = df.loc['Gloryhammer'].sort_values(by='trackName')
tracks = df_gh.value_counts(subset='trackName')
top_5 = tracks.head(5)






