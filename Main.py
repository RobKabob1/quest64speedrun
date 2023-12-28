import streamlit as st
import pandas as pd
import datetime

st.title("Quest 64 Any % Glitchless Speedrun", anchor=None, help=None)

st.write("This Streamlit App is to detail a Quest 64 Any% Glitchless run. It shows times, spirits, chests, strategies, and everything you need to get a run going.")

st.image("https://assets-prd.ignimgs.com/2023/03/11/quest64-1678500187713.jpg", caption='Quest 64')

st.header("Timings")

df = pd.DataFrame({
  'Boss': ["Solvaring", "Zelse", "Nepty", "Shilf", "Fargo", "Guilty", "Beigis", "Mammon"],
  'Kill Time': [datetime.time(0 ,25, 5), datetime.time(0 ,59, 43), datetime.time(1 ,22, 11), datetime.time(1 ,43, 41), datetime.time(2 , 2, 0), datetime.time(2 ,16, 50), datetime.time(2 ,24, 10), datetime.time(2 ,34, 23)]
})

df
st.header("Socials")

st.markdown("Quest 64 Discord: https://discord.gg/7qvydbgn")
st.markdown("Fuzzy's Speedrun: https://www.youtube.com/watch?v=VJxcMVaBfK8&t=1868s")
st.markdown("Quest 64 Calculations: https://gamefaqs.gamespot.com/n64/198386-quest-64/faqs/66316")
st.markdown("Spirit Locations: https://gamefaqs.gamespot.com/n64/198386-quest-64/faqs/38586")
