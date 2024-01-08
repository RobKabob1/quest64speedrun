import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Solvaring",
    page_icon="🪨",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Solvaring", anchor=None, help=None)
st.warning('''##### Goals: 63 HP, 16 MP, 16 Water.''')

st.header("Melrode (0:00:00)", anchor="Melrode")
melrode_df = pd.DataFrame(
    {
        "Event": [
            "🫙 Item", 
            "🫙 Item", 
            "🫙 Item", 
            "🍞 Item", 
            "🍞 Item", 
            "❔ Spirit 1",
            "🪽 Item", 
            "🍞 Item", 
            "❔ Spirit 2", 
            "- Action -", 
            ],
        "Notes": [
            "Dew Drop: In castle's large opened room",
            "Dew Drop: In room after previous chest",
            "Dew Drop: Second chest in room with previous Dew Drop",
            "Fresh Bread: Talk to lady", 
            "Honey Bread: In chest next to lady", 
            "Take left as you come out of the Monestary. It's in the hay.",
            "Wings: Get wings in Melrode",
            "Fresh Bread: In the house on hill",
            "At the top of the hill in the far corner past the sheep",
            "Use wings and leave Melrode",
            ]
    }
)
st.table(melrode_df)

st.header("Holy Plain (0:08:22)")
st.image('images/HolyPlain.jpg')
holy_plain_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 3", 
            "❔ Spirit 4", 
            "❔ Spirit 5",
            ],
        "Notes": [
            "On the left side in large space coming from Melrode", 
            "Fortune Teller's Hut", 
            "In the yard around a house you'll go by further down the path",
            ]
    }
)
st.table(holy_plain_df)

st.header("Donoran/Connor Forest (0:07:34)")
donoran_df = pd.DataFrame(
    {
        "Event": [
            "🫙 Item", 
            "🪽 Item",
            "❔ Spirit 6",
            "- Action -",
            ],
        "Notes": [
            "Dew Drop: In Donoran shop", 
            "Wings: Get Donoran Wings",
            "In the light brown open space at the bottom of the city",
            "Use wings and leave Donoran",
            ]
    }
)
st.table(donoran_df)
st.success('''
           ### Connor Forest Tips
            * For Experience: Kill groups with 5-6 Bat’s. It’s a spirit level up after you kill them. Round them up and water pillar them.
            * For Defense Farm: Kill a solo Marionasty or the Frog Knights. You want to get hit by a bunch of Wind Cutters that do low damage.
            * Tip: Run counterclockwise on Marionasty/Frog Knights to get hit with more Wind Cutters, meaning an overall faster Defense Farm.
            ''')

connor_forest_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 7",
            "❔ Spirit 8",
            "❔ Spirit 9",
            "🥾 Item", 
            "❔ Spirit 10",
            "❔ Spirit 11",
            ],
        "Notes": [
            "At entrance to the right when you enter Connor Forest", 
            "Take the right path and check behind trees on the right side", 
            "Take the left path it's inside the hut",
            "Giant's Shoes: In the hut", 
            "Take the left path near the tree that makes an arch", 
            "Take the left path, it's just before the boss door", 
            ]
    }
)
st.table(connor_forest_df)
st.write('''Make sure to have 63 HP, 17 MP, 16 Water, and Ice Knife before going to Solvaring.  
         Reasoning for 63 HP: 4 hits from boss per item we use.''')

st.header("Solvaring (0:19:00)")
solvaring_1_df = pd.DataFrame(
    {
        "Event": [
            "🍞 Item", 
            ],
        "Notes": [
            "Honey Bread: Chest on left. Hug wall so you do not engage Solvaring!", 

            ]
    }
)
st.table(solvaring_1_df)
st.error('''
         ### Solvaring Tips
         ###### 200 HP 
        * Engage from Honey Bread chest area
        * Use Giant's Shoes first turn to get closer, then dodge his hand beam.  
        * Then go in to get him with Water Pillar lvl 1.
        * It will take 9 Water Pillar hits.
        * Remember, you can survive 4 hits of his ground pound. Then use bread!
        ''')
st.write("End at 0:24:03")