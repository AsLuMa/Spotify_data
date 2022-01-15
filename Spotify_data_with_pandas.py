import json
import pandas as pd
import matplotlib.pyplot as plt

with open('StreamingHistory0.json', 'r', encoding='utf8') as file:
    data = json.load(file)

df = pd.DataFrame(data)

# --- # All songs I've listened to for over two minutes, with or without milliseconds-played column dropped
df_two_ms = df.loc[df['msPlayed'] > 120000]
# df_over_two_mins = df_two_ms.set_index('artistName').drop('msPlayed', axis=1).sort_values(by='trackName')
df_over_two_mins = df_two_ms.set_index('artistName').sort_values(by='trackName')

# --- # NOT USED
# print(df_over_two_mins.head(10))
# df_time = df_over_two_mins.reset_index()
# df_time = df_time.set_index(['artistName', 'endTime']).sort_values(['artistName', 'endTime'])

gr_for_time = df_over_two_mins.groupby('artistName')
# --- # Gloryhammer
df_gh_time = gr_for_time.get_group('Gloryhammer').sort_values('endTime').drop('msPlayed', axis=1)
df_gh_time["endTime"] = pd.to_datetime(df_gh_time["endTime"])
times_played_pr_month_gh = df_gh_time['endTime'].dt.month.value_counts().sort_index()

new_df = df_gh_time
new_df = new_df.set_index('endTime')
track = new_df['trackName'] == 'Universe on Fire'
times_played_pr_month_uf = track[track].index.month.value_counts().sort_index()
list_0 = [0,0,0,0,0]
ser_0 = pd.Series(list_0)
# ser_0, times_played_pr_month_uf))
times_played_pr_month_uf = pd.concat([ser_0, times_played_pr_month_uf])
print(times_played_pr_month_uf)

# --- # Sabaton
df_sb_time = gr_for_time.get_group('Sabaton').sort_values('endTime').drop(['msPlayed'], axis=1)
df_sb_time["endTime"] = pd.to_datetime(df_sb_time["endTime"])
times_played_pr_month_sb = df_sb_time['endTime'].dt.month.value_counts().sort_index()


# --- # Bar chart - which month do I listen to Gloryhammer the most?
list_months = ['Jan', 'Feb', 'Mars', 'Mai', 'Apr', 'Juni', 'Juli', 'Aug', 'Sept', 'Okt', 'Nov']

# --- # Gloryhammer vs sabaton
plt.bar(list_months, times_played_pr_month_gh, width=-0.25, align='edge')
plt.bar(list_months, times_played_pr_month_sb, width=0.25, align='edge')
plt.ylabel("Antall avspillinger")
plt.title('Gloryhammer vs Sabaton')
colors = {'Gloryhammer':'blue', 'Sabaton':'orange'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# --- # Gloryhammer: Alle sanger vs Universe on Fire
plt.bar(list_months, times_played_pr_month_gh)
plt.bar(list_months, times_played_pr_month_uf)
plt.ylabel("Antall avspillinger")
plt.title('Gloryhammer')
colors = {'Alle sanger':'blue', 'Universe on Fire':'orange'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# TODO time of day


exit()
# --- # All bands and top ten bands
list_all_bands = df.loc[:, 'artistName'].unique()
top_ten_artists = df_over_two_mins.index.value_counts().head(10)

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

# Groupby (only songs I've listened to more than 2 mins)
group_an = df_over_two_mins.groupby('artistName')

# --- # Dataframes from groupby
df_gh = songs_by_one_band(group_an, 'Gloryhammer')
df_sb = songs_by_one_band(group_an, 'Sabaton')
df_ghost = songs_by_one_band(group_an, 'Ghost')

# --- # Function calls
# print_played_more_than_ten_times(df_sb)
# print_played_more_than_ten_times(df_gh)
# print_played_more_than_ten_times(df_ghost)
#
# print_songs_by_one_band(group_an, 'Sabaton')
# print_songs_by_one_band(group_an, 'Gloryhammer')

# print_top_ten_by_artist(df_gh)
# print_top_ten_by_artist(df_sb)

# --- # How many hours listened to Gloryhammer (df_gh)?
# hours_listened = math.ceil((df_gh.loc[:, 'msPlayed'].sum())/3600000)

exit()


# Finding most frequent songs played without Groupby
df = df.set_index('artistName')
df_gh = df.loc['Gloryhammer'].sort_values(by='trackName')
tracks = df_gh.value_counts(subset='trackName')
top_5 = tracks.head(5)






