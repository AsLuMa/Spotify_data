import json
import pandas as pd

# TODO When do I listen? When do I listen to Gloryhammer? How do aggregate this? (Month, time of day?)
# TODO How many times have I listened to all? What are the top 10 artists I listen to the most?

with open('StreamingHistory0.json', 'r', encoding='utf8') as file:
    data = json.load(file)

df = pd.DataFrame(data)

# --- # All songs I've listened to for over two minutes, with milliseconds-played column dropped
df_over_two_mins = df.loc[df['msPlayed'] > 120000]
df_over_two_mins = df_over_two_mins.set_index('artistName').drop('msPlayed', axis=1).sort_values(by='trackName')

top_ten_artists = df_over_two_mins.index.value_counts().head(10)
print(top_ten_artists)

# list_all_bands = df.loc[:, 'artistName'].unique()
# print(list_all_bands)


exit()

# --- # Various functions
def songs_by_one_band(group, band_name):
    df_song_by_band = group.get_group(band_name)
    return df_song_by_band

def print_songs_by_one_band(group, band_name):
    df_song_by_band = group.get_group(band_name)
    for i in df_song_by_band['trackName'].unique():
        print(i)

def print_played_more_than_ten_times(df_artist):
    nr_times_track_played = df_artist['trackName'].value_counts()
    track_over_ten = nr_times_track_played.loc[lambda x: x > 10]
    print(track_over_ten)

def print_top_ten_by_artist(df_artist):
    top_ten_tracks = df_artist['trackName'].value_counts().head(10)
    print(top_ten_tracks)

# --- # Fetch some data
# Need: Groupby-object, band-name, datafram (from Groupby-object)

# Groupby
group_an = df_over_two_mins.groupby(by='artistName')

# Dataframes from groupby
df_gh = songs_by_one_band(group_an, 'Gloryhammer')
df_sb = songs_by_one_band(group_an, 'Sabaton')
df_ghost = songs_by_one_band(group_an, 'Ghost')

# Function calls
print_played_more_than_ten_times(df_sb)
print_played_more_than_ten_times(df_gh)
print_played_more_than_ten_times(df_ghost)

print_songs_by_one_band(group_an, 'Sabaton')
print_songs_by_one_band(group_an, 'Gloryhammer')

# print_top_ten_by_artist(df_gh)
# print_top_ten_by_artist(df_sb)



exit()


# Finding most frequent songs played without Groupby
df = df.set_index('artistName')
df_gh = df.loc['Gloryhammer'].sort_values(by='trackName')
tracks = df_gh.value_counts(subset='trackName')
top_5 = tracks.head(5)






