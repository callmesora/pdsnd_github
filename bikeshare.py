import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

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
        city= input('Please select the city you would like to search from (chicago,new york city,washington)  : ').lower()
        
        if city not in CITY_DATA :
            print("\n \n That's not a valid city :( or we simply don't have it in the database, please choose from (chicago,new york city,washington)")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please select the month you would like to search, (all, january, february, ... , june):  ').lower()
        
        if month not in months:
            print("\n \n That's not a valid month :( or we simply don't have it in the database, please type a month between jarnuary and june):  ")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please select the day you would like to search, (all, monday, tuesday... sunday):  ').lower()
        
        if day not in days:
            print("\n \n That's not a valid day :( , please choose from (monday,tuesday,thursday,wednesday,friday,saturday,sunday)")
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
   #read the data
    df=pd.read_csv(CITY_DATA[city])
    
    #Convert Start time to date time
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #get a month and dayofweek by name column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month!='all':
        #turn string to month int index
        month_num= months.index(month)+1 
        
        #filter by month
        
        df=df[df['month']==month_num]
    
    if day!='all':
        #filter by day
        df=df[df['day_of_week'] == day.title()]
    
    
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #Get most frequent month index and convert it
    
    mc_month_idx= df['month'].value_counts().idxmax() -1
    mc_month=months[mc_month_idx]
    print('The most frequent month is: {}'.format(mc_month))
    
    

    # TO DO: display the most common day of week
    mc_day=df['day_of_week'].value_counts().idxmax()
    print('The most common day is: {}'.format(mc_day))

    # TO DO: display the most common start hour
    mc_hour=df['Start Time'].dt.hour.value_counts().idxmax()
    print('The most common Start hour is: {}'.format(mc_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station=df['Start Station'].value_counts().idxmax()
    print('Most Common Start Staton: {}'.format(mc_start_station))
    # TO DO: display most commonly used end station
    mc_end_station=df['End Station'].value_counts().idxmax()
    print('Most Common End Station: {}'.format(mc_end_station))
    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n User Type Count')
    print(df['User Type'].value_counts())
    
    #Since only washington doesn't have Gender nor Birth collum
    if city != 'washington':
    
        print('\n Gender Count')
        # TO DO: Display counts of gender
        print(df['Gender'].value_counts())
        print('\n')
        # TO DO: Display earliest, most recent, and most common year of birth
        #Earliest value is the min , recent the max and most common the value with most counts
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        mc_year=df['Birth Year'].value_counts().idxmax()
        print('Earliest year of birth: {}'.format(earliest))
        print('Most recent : {} '.format(recent))
        print('Most Common : {}'.format(mc_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # ask the user, " do you want to see raw data?" if user input yes, then it should
#show 5 lines of raw data. and again it should ask the user "do you want to see more 5 lines of raw data?" if yes user yes then it should again show further 5 line of raw data and this should be continuously going until the user gives input "No".
    
    
    while True: 
        y=input('Would you like to see RAW Data? yes or no:  ')
        if y=='yes':
            start=0
            count=5
            print(df.head())
            
            while True: #print 5 by time if he says yes
        
                if input('Would you like to see more data? yes or no:  ') == 'yes':
                    start+=5
                    count+=5
                    print(df.iloc[start:count])
                else:
                    break
            break
        
        elif y =='no':
            break
        else: #check answer
            print('Please Select yes or no')
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
