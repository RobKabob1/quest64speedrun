import streamlit as st
import pandas as pd

st.title("Nepty", anchor=None, help=None)
with st.container(border=True):
    st.write('''Goals: 97 HP, 21 MP, 38 Earth, 25 Water. Have Magic Barrier.''')

st.divider()

st.header("Larapool/Blue Cave/Crystal Valley (0:59:43)")
larapool_df = pd.DataFrame(
    {
        "Event": [
            "- Action -",
            "❔ Spirit 33", 
            "❔ Spirit 34", 
            "❔ Spirit 35", 
            ],
        "Notes": [
            "Exit downstairs in the Larapool inn. Drain the water by walking in and out of the secret room.",
            "With the water drained,  take the right path to a side opening to the spirit.", 
            "With the water drained, take the left path and its near the other entrance to the inn.",
            "On the right in the entrance to Blue Cave",
            ]
    }
)
st.table(larapool_df)

with st.container(border=True):
    st.subheader("Blue Cave Tips")
    st.write('''Avoid Coolers and Mimics. They hurt!   
             The goal here is to make it through Blue Cave as fast as you can.  
             There are no exp or defense farms that are efficient here.''')  
   
blue_cave_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 36", 
            "🌿 Item", 
            "❔ Spirit 37", 
            ],
        "Notes": [
            "In the maze (from the start) take a right at the start and then a left",
            "Mint Leaves: in chest next to previous spirit",
            "In the maze (from the start) head straight, then a right, then a right, then a left to the spirit.",
            ]
    }
)
st.table(blue_cave_df)
st.write('''Make sure to have 34 Earth before leaving Blue Cave and head to Crystal Valley.''')
crystal_valley_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 38", 
            ],
        "Notes": [
            "To the left of the house in Crystal Valley",
            ]
    }
)
st.table(crystal_valley_df)
st.write("Head into the house and go upstairs. Go through the teleporter and onto the boat.")

st.divider()

st.header("Isle of Skye (1:14:50)")
larapool_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 39",
            "🏺 Item", 
            "❔ Spirit 40", 
            "❔ Spirit 41",
            "❔ Spirit 42",
            "❔ Spirit 43", 
            ],
        "Notes": [
            "On the lowest deck in the back of the Pirate Ship",
            "Dragon's Potion: chest next to previous spirit",
            "To the right of the dock in Isle of Skye",
            "In front of the fence around Colleen's Cabin", 
            "Behind Colleen's Cabin",
            "Behind a rock near the portal that takes you underwater",
            ]
    }
)
st.table(larapool_df)

st.divider()

st.header("Nepty (1:17:32)")
with st.container(border=True):
    st.subheader("Nepty Tips")
    st.write("680 HP")
    st.write('''We don't want him to walk up to us.  
             Fight him mid range so he does Ice Wall. You can dodge this.  
             His Large Cutter up close is the most dangerous move.  
             Engage with Spirit Armor as your first move, move close to him, then Avalanche away.
             ''')
st.write("After Zelse is dead put 25 in Water for Heal 2 and put the rest in Earth for 27")
