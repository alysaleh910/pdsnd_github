import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTHS = {'jan': 1,
          'feb': 2,
          'mar': 3,
          'apr': 4,
          'may': 5,
          'june': 6 }

DAYS =  {'su': 'Sunday',
         'm': 'Monday',
         'tu': 'Tuesday',
         'w': 'Wednesday',
         'th': 'Thursday',
         'f': 'Friday',
         'sa': 'Saturday' }

def get_filters():
#    Asks user to specify a city, month, and day to analyze.

#    Returns:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter


    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    month = None
    day = None

    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington')
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Not a valid input")

    #getuser input for filter type
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        filter = input('Would you like to filter the data by month, day, both, or not at all. Type none for no filter.')
        filter = filter.lower()
        if filter in ['month', 'day', 'both', 'none']:
            break
        else:
            print('Not a valid input')

    if filter in ['month','both']:
        while True:
            month = input('Which month would you like to choose? Jan, Feb, Mar, Apr, May, June or all.')
            month=month.lower()
            if month in ['jan','feb','mar','apr','may','june', 'all']:
                break
            else:
                print('Not a valid input')

    if filter in ['day','both']:
        while True:
            day = input('Which day would you like to choose? Su, M, Tu, W. Th, F, Sa or all')
            day = day.lower()
            if day in ['su','m','tu','w', 'th', 'f', 'sa', 'all']:
                break
            else:
                print('Not a valid input')

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
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month

    if month is not None:
        df = df[df.month==MONTHS[month]]
        pass
    if day is not None:
        df = df[df.weekday ==DAYS[day]]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    pop_month = df['month'].mode()[0]

    print('The most common month is: ', pop_month, '!')

    # display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    pop_weekday = df['weekday'].mode()[0]

    print('The most common day of the week is: ', pop_weekday, '!')

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    pop_hour = df['start_hour'].mode()[0]
    print('The most common start hour is: ', pop_hour, '!')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_st = df['Start Station'].mode()[0]
    print('The most common start station is: ', pop_start_st)

    # display most commonly used end station
    pop_end_st = df['End Station'].mode()[0]
    print('The most common end station is: ', pop_end_st)

    # display most frequent combination of start station and end station trip
    start_end_st = df['Start Station'] + df['End Station']
    pop_comb = start_end_st.mode()[0]
    print('The most frequent combination of start and end station is :', pop_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_s = df['Trip Duration'].sum()
    total_travel_m = df['Trip Duration'].sum()/60
    print('The total trip time in seconds is: {}\n'
    'The total trip time in minutes is: {}'.format(total_travel_s, total_travel_m))

    # display mean travel time
    mean_travel_s = total_travel_s.mean()
    mean_travel_m = total_travel_m.mean()
    print('The mean trip time in seconds is: {}\n'
    'The mean trip time in minutes is: {}'.format(mean_travel_s, mean_travel_m))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    ut_count = df['User Type'].value_counts()
    print('Customer Count: {}\n Subscriber Count: {}'.format(ut_count['Customer'], ut_count['Subscriber']))

    # Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print('Count of genders is:', gender)
    except KeyError:
        print('No data available for gender')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_dob = df['Birth Year'].min()
        recent_dob = df['Birth Year'].max()
        common_dob = df['Birth Year'].mode()[0]
        print('The earliest year of birth is: {}\n'
        'The most recent year of birth is: {}\n'
        'The most common year of birth is: {}'.format(earliest_dob, recent_dob, common_dob))
    except KeyError:
        print("No data available for birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#display raw data when prompted by user
def display_data(df):

    raw_start = 0
    raw_end = 5
    while True:
        raw_data = str(input("Would you like to see the raw data? Enter yes/no"))
        if raw_data.lower() == 'yes':
            print(df.iloc[raw_start : raw_end])
            raw_start += 5
            raw_end += 5
            break
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
