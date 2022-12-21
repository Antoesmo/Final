import streamlit as st
import pandas as pd


st.write("""
# Welcome to the Skyscraper Analysis Application
The map below points out in red dots *WHERE* the 99 *tallest skyscrapers* on Earth are located!
 """)

df=pd.read_csv("Skyscrapers2021.csv", usecols=["RANK","NAME","CITY", "FULL ADDRESS", "latitude", "longitude", "COMPLETION", "HEIGHT", "METERS", "FEET", "FLOORS","MATERIAL", "FUNCTION", "LINK"])
st.map(df)
st.write("""The table below shows the 99 *tallest* Skyscrapers of the world!
Each columnn informs the reader on a specific characteristic of each building!
""")
df=df.drop(df.columns[[0,2,3,4,5,8,9,13]], axis=1)
df=df.sort_values(by=['HEIGHT','FLOORS'], ascending=False)

#df=df.[df.]
st.write("""
Below is a map of Manhattan, New York City, NY, USA. This area has a large amount of skyscrappers *(a total of 7!)* as indicated by the red dots on the map."""
)
st.table(df)
df=pd.read_csv("Skyscrapers2021.csv", usecols=["RANK","NAME","CITY", "FULL ADDRESS", "latitude", "longitude", "COMPLETION", "HEIGHT", "METERS", "FEET", "FLOORS","MATERIAL", "FUNCTION", "LINK"])
df=df[df.CITY=='New York City']
#df=df.drop(df.columns[[0,2,3,4,5,8,9,13]], axis=1)
df=df.sort_values(by=['HEIGHT','FLOORS'], ascending=False)
st.map(df)


st.write("""
Dubai is a city in the United Arab Emirates. The current tallest skyscraper in the world is located there, named Burj Khalifa! (You can see more information on this skyscraper from the table at the top of the page, the skyscraper is placed at #1)
Below is a map of Dubai, UAE. This area has an even *larger* amount of skyscrappers *(a total of 16!)* as indicated by the red dots on the map."""
)
df=pd.read_csv("Skyscrapers2021.csv", usecols=["RANK","NAME","CITY", "FULL ADDRESS", "latitude", "longitude", "COMPLETION", "HEIGHT", "METERS", "FEET", "FLOORS","MATERIAL", "FUNCTION", "LINK"])
df=df[df.CITY=='Dubai']
#df=df.drop(df.columns[[0,2,3,4,5,8,9,13]], axis=1)
df=df.sort_values(by=['HEIGHT','FLOORS'], ascending=False)
st.map(df)

df=pd.read_csv("Skyscrapers2021.csv", usecols=["RANK","NAME","CITY", "FULL ADDRESS", "latitude", "longitude", "COMPLETION", "HEIGHT", "METERS", "FEET", "FLOORS","MATERIAL", "FUNCTION", "LINK"])
df=df.groupby(["COMPLETION"]).count()
st.write("""
The bar chart below shows the number of skyscrapers built per year:
""")
df=df.drop(df.columns[[1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)
st.bar_chart(df)


option=st.selectbox(
    'Skyscrapers are fun! Would you like to see the tallest building in America, Asia or Europe?', ('AMERICA','ASIA','EUROPE'))
if (option=='AMERICA'):
    st.write("One World Trade Center, in NYC, USA")
elif (option=='ASIA'):
    st.write("Burj Khalifa, in Dubai, UAE")
elif (option=='EUROPE'):
    st.write("Lakhta Center, in Saint Petersburg, RUSSIA")

df=pd.read_csv("Skyscrapers2021.csv", usecols=["RANK","NAME","CITY", "FULL ADDRESS", "latitude", "longitude", "COMPLETION", "HEIGHT", "METERS", "FEET", "FLOORS","MATERIAL", "FUNCTION", "LINK"])



option=st.selectbox('Do you want to see the tallest composite?',('YES','NO'))
if (option=='YES'):
    from PIL import Image
    image=Image.open('Image.jpg')
    st.image(image, caption='Shanghai Tower')


    #st.line_chart(df)
#df=df.drop(df.columns[[1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)
#st.bar_chart(df)
