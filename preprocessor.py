
import re
import pandas as pd


def preprocess(data):

    pattern = r'\d{2}\/\d{2}\/\d{2},\s(?:\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)|(?:[01]?\d|2[0-3]):\d{2})\s-\s'
   
    dates = re.findall(pattern, data)
    messages = re.split(pattern, data)[1:]

    # Making pandas data frame of two columns -
    df = pd.DataFrame({'user_messages': messages, 'message_dates': dates})

    # Step 1: clean
    df['message_dates'] = df['message_dates'].str.strip().str.replace(r'\s*-\s*$', '', regex=True)

    # Step 2: convert
    df['message_dates'] = pd.to_datetime(
        df['message_dates'], 
        # format="%d/%m/%y, %I:%M %p", 
        errors='coerce'
    )

    df.rename(columns={'message_dates':'date'}, inplace=True)

    # separate users and messages
    users = []
    messages = []
    for message in df['user_messages']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:# user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification' )
            messages.append(entry[0])

    df['user'] = users
    df['message' ] = messages
    df.drop(columns=['user_messages'], inplace=True)

    # Exactring data and time -
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['daily_date'] = df['date'].dt.date
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df





