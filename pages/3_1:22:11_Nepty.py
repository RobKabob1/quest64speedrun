import streamlit as st
import pandas as pd

st.title("Nepty", anchor=None, help=None)
st.warning('''##### Goals: 97 HP, 21 MP, 38 Earth, 25 Water. Have Magic Barrier.''')

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
            "Exit Larapool inn downstairs. Drain water via secret room.",
            "With the water drained, take the right path to a side opening to the spirit.", 
            "With the water drained, take the left path. Near the other entrance to the inn.",
            "On the right in the entrance to Blue Cave",
            ]
    }
)
st.table(larapool_df)
st.info('''
        ### Blue Cave Tips
        * Avoid Coolers and Mimics. They hurt!   
        * The goal here is to make it through Blue Cave as fast as you can.  
        * There are no exp or defense farms that are efficient here.
        ''')  
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
            "In the maze (from the start) head straight, then right, then right, then left to the spirit.",
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
st.write('''Make sure to have 97 HP, 21 MP, 38 Earth, and 25 Water before going to Nepty.  
         Reasoning for this is that we need Avalanche/Magic Barrier combo.
         Only 36 Earth is needed for Magic Barrier, but the spirits we get so far get us to 38.
         ''')

st.header("Nepty (1:17:32)")
st.error('''
        ### Nepty Tips
        ###### 880 HP
        * Magic Barrier and Avalanche back and forth.  
        * Remember to Magic Barrier every 2 turns!  
        * Use MP items in between Magic Barriers. Mint Leaves first.  
        * If you have lots of HP items, then do Confusion to get MP. Then use HP item after Magic Barrier. This saves an MP item.  
        ''')
st.write("Head out of the underwater arena once Nepty is dead, get into an encounter, and die. This death warp's us to Efna. Make sure to save here. Then, get on a boat to East Limelin.")
st.write("End at 1:22:11")