# rod-s-bike-share-project
In this project we analyzed data from from three cities where the user can select options

Once you choose a city, month and day you can see some stats, raw data, restart and pick another city or just exit

I've learned a lot about how to input data and checking the consitency of the data. I also learned how to use lamba expressions
and I also learn to use loc and iloc to look into a dataframe's details 

References
https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe

From here I got the sentence necessary to display most frequent combination of start station and end station trip
df['start_end_station'] = df[['Start Station', 'End Station']].apply(lambda x: '_'.join(x), axis=1)