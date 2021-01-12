import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).

    while True:
        city_raw = input('\nPlease enter a number to choose a city.\n 1. Chicago\n 2. New York\n 3. Washington\n')
        try:
            if int(city_raw) == 1:
                city = 'chicago'
            elif int(city_raw) == 2:
                city = 'new york city'
            elif int(city_raw) == 3:
                city = 'washington'
            else :
                raise ValueError
        except ValueError:
            print("\n" + city_raw + " is not a valid number, try again.")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month_raw = input('\nPlease enter a number to choose a month.\n 1. january\n 2. february\n 3. march\n 4. april\n 5. may\n 6. june\n 7. all\n')
        try:
            if int(month_raw) == 1:
                 month = 'january'
            elif int(month_raw) == 2:
                 month = 'february'
            elif int(month_raw) == 3:
                 month = 'march'
            elif int(month_raw) == 4:
                 month = 'april'
            elif int(month_raw) == 5:
                 month = 'may'
            elif int(month_raw) == 6:
                 month = 'june'
            elif int(month_raw) == 7:
                 month = 'all'
            else :
                raise ValueError

        except ValueError:
            print("\n" + month_raw + " is not a valid number, try again.")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_raw = input('\nPlease enter a number to choose a day of week.\n 1. monday\n 2. tuesday\n 3. wednesday \n 4. thursday \n 5. friday \n 6. saturday \n 7. sunday \n 8. all \n')
        try:
            if int(day_raw) == 1:
                day = 'monday'
            elif int(day_raw) == 2:
                day = 'tuesday'
            elif int(day_raw) == 3:
                day = 'wednesday'
            elif int(day_raw) == 4:
                day = 'thursday'
            elif int(day_raw) == 5:
                day = 'friday'
            elif int(day_raw) == 6:
                day = 'saturday'
            elif int(day_raw) == 7:
                day = 'sunday'
            elif int(day_raw) == 8:
                day = 'all'
            else :
                raise ValueError

        except ValueError:
            print("\n" + day_raw + " is not a valid number, try again.")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most common month is: {}".format(popular_month))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print("The most common day is: {}".format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(most_used_start_station))

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(most_used_end_station))

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df[['Start Station', 'End Station']].apply(lambda x: ' together with '.join(x), axis=1)
    print("the most popular start and end station are: {}".format(df['start_end_station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    print("The total travel time is: {}".format(trip_duration.sum()))
    
    # display mean travel time
    print("The mean travel time is: {}".format(trip_duration.mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(gender_types)

    # Display earliest, most recent, and most common year of birth
    earliest_year_birth = df['Birth Year'].min()
    print("The earlist birth year is: {}".format(earliest_year_birth))

    most_recent_year_birth = df['Birth Year'].max()
    print("The most recent birth year is: {}".format(most_recent_year_birth))

    most_common_year_birth = df['Birth Year'].mode()[0]
    print("The most common birth year is: {}".format(most_common_year_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
