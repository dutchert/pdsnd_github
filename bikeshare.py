# Developed by Terry Dutcher

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_DATA = ['all','january', 'february', 'march', 'april', 'may', 'june']

DAYS_DATA = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    name = input('May I have your name? \n')
    
    print('Hello!',name.title(), 'Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cityname = ''
    while cityname.lower() not in CITY_DATA:
        cityname = input('Will you please provide me a city name to analyze data? Your options are chicago, new york city or washington)\n')
        if cityname.lower() in CITY_DATA:
            city = CITY_DATA[cityname.lower()]
        else:
            print("So sorry I was not able to process the name of the city to analyze data. Can you please try again?\n")
         
    # TO DO: get user input for month (all, january, february, ... , june)
    
    monthname = ''
    while monthname.lower() not in MONTHS_DATA:
        monthname = input("Can you please provide me a month name to filter on to analyze your data? Your options are 'all','january', 'february', 'march', 'april', 'may', or 'june'.\n")
        if monthname.lower() in MONTHS_DATA:
            month = monthname.lower()
        else:
            print("So sorry I was not able to process the name of the month to analyze data. Can you please try again?\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    dayname = ''
    while dayname.lower() not in DAYS_DATA:
        dayname = input("Can you please provide me a day name to filter on to analyze your data? Your options are 'all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' or 'saturday'.\n")
        if dayname.lower() in DAYS_DATA:
            day = dayname.lower()
        else:
            print("So sorry I was not able to process the name of the day to analyze data. Can you please try again?\n")

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
    #Load datafile into dataframe
    df = pd.read_csv(city)

    #Convert start time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month from start time column to create month column
    df['month'] = df['Start Time'].dt.month
    
    #extract day of week from start time column to create day of week column
    df['day_of_week'] = df['Start Time'].dt.day
    
    #extract hour from start time column to create hour column
    df['hour'] = df['Start Time'].dt.hour
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    
    commonmonth = df['month'].mode()[0]
    print("The most common month is: " + MONTHS_DATA[commonmonth].title())

    # TO DO: display the most common day of week
    commondayofweek = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + str(commondayofweek))


    # TO DO: display the most common start hour
    commonstarthour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(commonstarthour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonstartstation = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is: " + commonstartstation)
    


    # TO DO: display most commonly used end station
    commonendstation = df['End Station'].mode()[0]
    print("The most commonly used End Station is: " + commonendstation)


    # TO DO: display most frequent combination of start station and end station trip
    frequentcombostation = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of Start Station and End Station trip is : " + str(frequentcombostation.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltraveltime = df['Trip Duration'].sum()
    print("The total travel time is: " + str(totaltraveltime))


    # TO DO: display mean travel time
    meantraveltime = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(meantraveltime))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(usertypes))
    
    print('-'*40)
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))
        
        print('-'*40)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliestyear = df['Birth Year'].min()
        print("The earliest year of birth is: {:.0f}\n".format(earliestyear))
    
        recentyear = df['Birth Year'].max()
        print("The most recent year of birth is: {:.0f}\n".format(recentyear))
        
        commonyear = df['Birth Year'].mode()[0]
        print("The most common year of birth is: {:.0f}\n".format(commonyear) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Please enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
