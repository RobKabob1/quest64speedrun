import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Quest 64 Speedrun",
    page_icon="🪄",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Quest 64 Any % Glitchless Speedrun", anchor=None, help=None)
st.success("##### This Streamlit App serves as a guide for a Quest 64 Any% Glitchless 2 hour 34 minute speedrun. It has timestamps, spirit locations, items, maps, and tips.")
st.image("images/originals/quest64box.png")

st.header("Timings")
df = pd.DataFrame({
  'Boss': ["Solvaring", "Zelse", "Nepty", "Shilf", "Fargo", "Guilty", "Beigis", "Mammon"],
  'Kill Time': [datetime.time(0 ,25, 5), datetime.time(0 ,59, 43), datetime.time(1 ,22, 11), datetime.time(1 ,43, 41), datetime.time(2 , 2, 0), datetime.time(2 ,16, 50), datetime.time(2 ,24, 10), datetime.time(2 ,34, 23)]
})
st.dataframe(df)

st.header("Fuzzy's Speedrun")
st.video("https://www.youtube.com/watch?v=VJxcMVaBfK8")

st.header("Socials")
with st.container(border=True):
  st.markdown('''
              * Quest 64 Discord: https://discord.gg/7qvydbgn
              * Quest 64 Calculations: https://gamefaqs.gamespot.com/n64/198386-quest-64/faqs/66316
              * Spirit Locations: https://gamefaqs.gamespot.com/n64/198386-quest-64/faqs/38586
              * Maps: https://shrines.rpgclassics.com/n64/quest64/map/elimelin.shtml
              ''')

