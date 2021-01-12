# rod-s-bike-share-project
In this project we analyzed data from from three cities where the user can select options

References
https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe

From here I got the sentence necessary to display most frequent combination of start station and end station trip
df['start_end_station'] = df[['Start Station', 'End Station']].apply(lambda x: '_'.join(x), axis=1)