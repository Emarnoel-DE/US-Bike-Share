#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np
#!pip install tabulate
from tabulate import tabulate
pd.set_option("display.max_columns",None)
pd.set_option("max_colwidth", None)
 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

def input_peruse(display_msg, valid_input):
    """Checks users input to ensure only entries that are determined to be valid_input are accepted. 
        
        Args:
            display_msg : prompt message to inform user what to input
            valid_input: list of valid entries
        
        Returns:
            users_entry - the users valid entry
    """
    
    try:
        
        users_entry = str(input(display_msg)).lower()
        
        while users_entry not in valid_input:
            print ("Oops!!! It seems you typed an incorrect entry")
            print ("Let's try again")
            users_entry = str(input(display_msg)).lower()
        
        print("Super!!! The chosen entry is :{}".format(users_entry))
        return users_entry
    
    except Exceptions as e:
        print ("Seems to be an issue with your input: {}".format(e))
        
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #fixed entry variables to handle exceptions
    validCity = CITY_DATA.keys()
    validMonth = months[:6]
    validMonth.append("all")
    validDay = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    display_msg_city = "Would you like to see data for Chicago, New York City, or Washington?\n"
    city = input_peruse(display_msg_city, validCity)
            
    # get user input for month (all, january, february, ... , june)
    display_msg_month = "Would you like to filter the data by month 'eg January, february,... June', or 'all' to apply no month filter?\n"
    month = input_peruse(display_msg_month, validMonth)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    display_msg_day = "Would you like to filter the data by name of the day of week 'eg Monday, Tuesday,...', or 'all' to apply no day filter?\n"
    day = input_peruse(display_msg_day, validDay)

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
# load specified city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to a more suitable format (datetime)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create month and day column from the transformed Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding integer value
        
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
    
    try: 
        # display the most common month
        print ("The most common month: ", months[df['month'].mode()[0] - 1].title() )
    
        # display the most common day of week
        print ("The most common day of week: ", df['day_of_week'].mode()[0] )

        # display the most common start hour
        print ("The most common start hour: ", df['Start Time'].dt.hour.mode()[0] )
        
    except:
        print ("The month you selected is not captured in the data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    try:

        # display most commonly used start station
        print ("The most common used start station: ", df['Start Station'].mode()[0] )

        # display most commonly used end station
        print ("The most common used end station: ", df['End Station'].mode()[0] )

        # display most frequent combination of start station and end station trip
        print ("The most common used start & end station: ", (df['Start Station'] + df['End Station']).mode()[0] )

    except:
        print("The month you selected isn't captured by the data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    try:

        # display total travel time in days dividing by 60*60*24
        print ("The total travel time in days: ", (df['Trip Duration'].sum())/86400)

        # display mean travel time in hours dividing by 60*60
        print ("The mean travel time in Hours: ", (df['Trip Duration'].mean())/3600 )
    
    except ValueError as v:
        print("The month you selected isn't captured: {}".format(v))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print ("User count: \n", df['User Type'].value_counts())

    try:
    
        # Display counts of gender
        print ("Gender count: \n", df['Gender'].value_counts())
    
    except ValueError as v:
        print ("The selected month isn't captured by the data: {}".format(v))
    except KeyError as k:    
        print ("Your selected City has no data on: {}".format(k))
    

    # Display earliest, most recent, and most common year of birth
    try:
    
        print ("The earliest year of birth: %d" % df['Birth Year'].min(skipna = True))
    
        print ("The most recent year of birth: %d" % df['Birth Year'].max(skipna = True))
    
        print ("The most common year of birth: %d" % df['Birth Year'].mode(dropna = True))
        
    except ValueError as v:
        print ("Your selected month isn't captured by data: {}".format(v))
    except KeyError as k:    
        print ("Your selected City has no data on : {}".format(k))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def display_rawData (df):
    """Displays raw data on bikeshare users based on users input."""
    
    
                 
   
    # Creating variable to handle exceptions
    valid_line_num = len(df.index)
    
    # get user input for number of rows to display at a time
    while True:
        try:
            line_num = int(float(input("How many lines of raw data do you wish to display?")))
            break
        except Exception as e:
            print ("Please enter a number to display: {}".format(e))
    
    
    while line_num > valid_line_num or line_num <= 0 or line_num < 1:
        
        try:
            
            line_num = int(float(input("Please enter a number to display")))
            
        except Exception as e:
            print ("Please enter a number to display: {}".format(e))
            

    # index variable for start(x) and end (y)
    x = 0
    y = line_num
    
    # Display raw data once for the first time
    raw_data = df.iloc[np.arange(x,y)]
    print ("\nThe %d row(s) of data are: \n" %line_num)
    print(tabulate(raw_data, headers ="keys"))
    
    # Ask user whether to continue or not
    display_more = input("\nDo you want to display more rows of raw data? Enter Y or N.\n ")
    
    if display_more.lower() != "no" or display_more.lower() != "n":
          while y < len(df.index):
                try:
                    x = y
                    y+=line_num
                    print("\nThe next %d rows of data are: \n" %line_num)
                    print(tabulate(df.iloc[np.arange(x,y)], headers ="keys"))
               
                    display_more = input("\nDo you want to display more data? Enter Y or N.\n ")
                    
                    if y >= valid_line_num:
                        print (tabulate("\nThe last row of data: \n", df.tail(line_num), headers ="keys"))
                    
                    if display_more.lower() == "no" or display_more.lower() == "n":
                        break
                except KeyboardInterrupt:
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rawData (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' or restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()

