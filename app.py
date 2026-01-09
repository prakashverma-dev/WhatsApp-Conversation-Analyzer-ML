import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")

# st.title("Hello Streamlit!")
# st.write("This is a simple web application built with Python.")
 
uploaded_file = st.sidebar.file_uploader("Choose Whatsapp Export File :")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # st.text(data)
    df = preprocessor.preprocess(data)
    # st.dataframe(df)

    # fetch unique users i.e all users -
    userlist = df['user'].unique().tolist()
    userlist.remove("group_notification")
    userlist.sort()
    userlist.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show Analysis with Selected User", userlist)

    if st.sidebar.button("Show Analysis"):

        # Stats Area -
        st.title("User Statistics ")
        total_msgs, words, total_media, total_links = helper.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.columns(4)

        
        with col1:
            st.subheader("Total Messages")
            st.title(total_msgs)
        with col2:
            st.subheader("Total Words")
            st.title(words)
        with col3:
            st.subheader("Media Shared")
            st.title(total_media)
        with col4:
            st.subheader("Link Shared")
            st.title(total_links) 

        # Monthly Timeline Graph of the Group/a single user -
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)

        # Daily Timeline Graph of the Group/a single user -
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        
        ax.plot(daily_timeline['daily_date'], daily_timeline['message'], color='black')
        # plt.figure(figsize = (18,10)) 
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)

        # Finding the busiest users in the group(Group Level only)-
        if selected_user == "Overall":
            
            st.title("Most Active User In Group")

            x, new_df = helper.mostActive_user(df)
            fig, ax = plt.subplots()
           
            col1, col2 = st.columns(2)

            with col1 :
                ax.bar(x.index, x.values, color = 'red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2 :
                st.dataframe(new_df)


        # Wordcloud -
        st.title("WordCloud of Most Used Words ")
        df_wc = helper.create_wordCloud(selected_user, df )
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most Common words used /Top 20 Words -
        most_common_df = helper.mostCommon_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title("Most Common Words")
        st.pyplot(fig)

        # st.dataframe(most_common_df)

        # Emoji Analysis -
        emoji_df = helper.emoji_analysis(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)
