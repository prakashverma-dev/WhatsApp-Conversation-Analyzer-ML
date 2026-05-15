
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob 


# We put the data logic in preprocessor.py file which accept a data and return a clearn struture data frame of having - 

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

    period = []
    for hour in df[['day_name','hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour+1))
        else:
            period.append(str(hour) + "-" + str(hour+1))

    df['period'] = period


    # Sentiment Anlyasis -

    analyzer = SentimentIntensityAnalyzer()

    if 'Sentiment' in df.columns:
        return df  # Already computed

    sentiments = []
    scores = []

    for message in df['message']:
        if not isinstance(message, str) or len(message.strip()) == 0:
            sentiments.append('Neutral')
            scores.append(0.0)
            continue

        # VADER Score
        vader_scores = analyzer.polarity_scores(message)
        compound = vader_scores['compound']

        # TextBlob Score (for ensemble)
        textblob_score = TextBlob(message).sentiment.polarity

        # Ensemble: Average both scores
        final_score = (compound + textblob_score) / 2

        if final_score >= 0.05:
            sentiments.append('Positive')
        elif final_score <= -0.05:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
        
        scores.append(round(final_score, 4))

    df = df.copy()
    df['Sentiment'] = sentiments
    df['Sentiment_Score'] = scores


    return df





