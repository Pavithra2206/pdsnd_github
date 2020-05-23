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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Enter correctly")
            continue
        else:
            break
    


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWould you like to see data for any specific month or all?Enter January, February, March, April, May, June or all\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Enter correctly")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nAre you looking for a particular day?Enter Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'\n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Enter correctly")
            continue
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
          months = ['january', 'february', 'march', 'april', 'may', 'june']
          month = months.index(month) + 1
          df = df[df['month'] == month]
    
    if day != 'all':
          df = df.loc[df['day_of_week'] == day.title()]

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mm = df['month'].mode()[0]
    print('The most common month is ',mm)


    # TO DO: display the most common day of week
    md = df['day_of_week'].mode()[0]
    print('The most common day of week is ',md)

    # TO DO: display the most common start hour
    mh = df['hour'].mode()[0]
    print('The most common hour is ',mh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mss = df['Start Station'].mode()[0]
    print('The most common start station is ',mss)

    # TO DO: display most commonly used end station
    mes = df['End Station'].mode()[0]
    print('The most common end station is ',mes)

    # TO DO: display most frequent combination of start station and end station trip
    mess = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most common combination of start and end station is ',mess)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tt = df['Trip Duration'].sum()
    print('The total travel time is ',tt)


    # TO DO: display mean travel time
    tm = df['Trip Duration'].mean()
    print('The mean travel time is ',tm)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The user types and their counts are:')
        print(df['User Type'].value_counts())
    except:
        print('exception')

    # TO DO: Display counts of gender
    try:
        print('The counts of gender are:')
        print(df['Gender'].value_counts())
    except:
        print('exception')
          
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth is ',df['Birth Year'].min())
    except:
        print('The earliest year of birth is exception')
    try:
        print('The most recent year of birth is ',df['Birth Year'].max())
    except:
        print('The recent year of birth is exception')
    try:
        print('The most common year of birth is ',df['Birth Year'].mode()[0])
    except:
        print('The common year of birth is exception')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() == 'yes':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
