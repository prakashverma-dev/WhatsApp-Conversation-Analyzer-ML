

# this file contains all the function logics -

from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

#Knowing user statistics logic function -
def fetch_stats(selected_user, df):

    #Indivisual Users - 
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]


    # 1. Total no of messages sent -
    total_msgs = df.shape[0]

    # 2. Total no of words -
    words = []
    for message in df['message']:
        words.extend(message.split())

    # 3. Total no of media shared -
    total_media = df[df['message'] == '<Media omitted>\n'].shape[0]

    # 4. Total link shared -
    links =[] 
    extract = URLExtract()

    for message in df['message']:
        # print(message)
        links.extend(extract.find_urls(message))
           

    return total_msgs, len(words), total_media, len(links)



#Knowing Most active user function -
def mostActive_user(df):

    # Knowing Most Active User /Busiest USer -
    x = df['user'].value_counts().head() # Top 5 Users 

    #Knowing percentage of most active user -    
    df = round(df['user'].value_counts() / df.shape[0] * 100, 2).reset_index().rename(columns = {'user':'name', 'count':'percent'})


    return x, df

# Create wordcloud of most frequent word used -
def create_wordCloud(selected_user, df):

    f = open('hinglish_stopwords.txt', 'r')
    stop_words = f.read()

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stopwords(message):
        new_words = []
        for word in message.lower().split():
            if word not in stop_words:
                new_words.append(word)

        return " ".join(new_words)

    wc = WordCloud(width=350, height=300, background_color='white', max_font_size=80,
    min_font_size=10 )
    temp['message'] = temp['message'].apply(remove_stopwords)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc


# Show Most Common word used -
def mostCommon_words(selected_user, df):

    f = open('hinglish_stopwords.txt', 'r')
    stop_words = f.read()

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']


    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

# Emoji ananlysis -
def emoji_analysis(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df 

# Montly timeline Graph Ananlysis of group or a user -
def monthly_timeline(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

# Montly timeline Graph Ananlysis of group or a user -
def daily_timeline(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    daily_timeline = df.groupby('daily_date').count()['message'].reset_index()

    return daily_timeline

# Most Active user or users on which day of week like Monday, Tueday etc. -
def week_activity_map(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

# Most Active user on which day of month like Jan or Aug etc. -
def month_activity_map(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


# Heap Map : To show on which time any user most active and least active -
def activity_heatmap(selected_user, df):

    #Indivisual Users - 
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name',columns='period',values='message' , aggfunc='count').fillna(0)

    return user_heatmap