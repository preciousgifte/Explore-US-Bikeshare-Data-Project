import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Cities = ['chicago', 'new york city', 'washington']

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
    
    city = input('Select a city from chicago, new york city, or washington: ').lower()
    while True: 
        if city not in Cities:
         city = input('please choose from the above list of cities :  ').lower()
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
 
    chioce = input("Would you like to enter 'yes' to apply no month filter or enter 'no' to filter by month: ").lower()
    if chioce == "yes":
       month = "all"
    else: 
        month = input("Enter a month from january to june to filter the data: ").lower()
        while month not in months:
            month = input("invalid input. Choose a month from january, febuary, march, april, may, or june:  ").lower() 
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)   
    
    days = ['monday', 'tuesday', 'wenesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("choose a day from monday to sunday to filter by week or choose all to apply no filter: ").lower()
    while True: 
        if day not in days and day != 'all': 
            day = input("please choose a day from monday to sunday or enter all to apply no filter: ").lower()
  
      
        else:
            print("you have successfully filter the data")
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
    # load data from the specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create a new month column by extracting month from Start Time column
    df['month'] = df['Start Time'].dt.month

    #Create a day of week column by extracting day from Start Time column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Create hour column from Start Time column
    df['hour'] = df['Start Time'].dt.hour
    
    
    #filters by month and day if applicable.
    month_dict = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6}
    if month != 'all':
              
     df = df.loc[df['month'] == month_dict[month]]
        
    #filters by month and day if applicable.
    if day !=  'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].value_counts().idxmax()
    print(F"The most frequent month is {frequent_month}")
    
    # TO DO: display the most common day of week
    frequent_day_of_week = df['day_of_week'].value_counts().idxmax()
    print(F"The most frequent day is {frequent_day_of_week}")
    
    # TO DO: display the most common start hour
    frequent_start_hour = df['hour'].value_counts().idxmax()
    print(F"The most frequent start hour is {frequent_start_hour}")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_station = df['Start Station'].value_counts().idxmax()
    print(F"The most frequently used start station is {frequent_start_station}")
    
    # TO DO: display most commonly used end station
    frequent_end_station = df['End Station'].value_counts().idxmax()
    print(F"The most frequently used end station is {frequent_end_station}")
    
    # TO DO: display most frequent combination of start station and end station trip
   
    start_end = df['Start Station'] + ' and ' + df['End Station']
    start_end_station = start_end.mode()[0]
    print(F"The most frequently used start and end station trip is: {start_end_station}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(F"The total travel time is : {df['Trip Duration'].sum()}")
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The average time traveled is : {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
     
        
        
    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print("gender colums not availble")
    else:
        gender_counts = df['Gender'].value_counts()
        print(f"total gender counts :\n {gender_counts}")
        print()
        
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"the most earliest year of birth : {df['Birth Year'].min()}") 
                      
        print(f"the most recent year of birth : {df['Birth Year'].max()}")                    
                                        
        print(f"the most common year of birth : {int(df['Birth Year'].value_counts().idxmax())}")    
    else:
        print('No birth year data')                                   
                                         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
        
def raw_data(df):
    """Display raw data of the first five rows"""
    
    raw_dat = input('\nWould you love to display the fist five rows of the raw data\n').lower()
    count = 0
    while raw_dat == 'yes':
        print(df.iloc[count:count + 5])
        count += 5
        view_again = input('Would you like to see the next 5 rows :').lower()
        if view_again == 'no':
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

