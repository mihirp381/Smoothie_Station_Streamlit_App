import streamlit
import pandas as pd

streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 and blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list.set_index('Fruit', inplace = True)
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected, :]
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice API display
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
