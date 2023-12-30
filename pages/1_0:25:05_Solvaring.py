import streamlit as st
import pandas as pd

st.title("Solvaring", anchor=None, help=None)
with st.container(border=True):
    st.write('''Goals: 63 HP, 17 MP, 16 Water. Have Ice Knife.''')

st.divider()

st.header("Melrode (0:00:00)", anchor="Melrode")
melrode_df = pd.DataFrame(
    {
        "Event": [
            "🍞 Item", 
            "🍞 Item", 
            "❔ Spirit 1",
            "🪽 Item", 
            "🍞 Item", 
            "❔ Spirit 2", 
            "- Action -", 
            ],
        "Notes": [
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

st.divider()

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

st.divider()

st.header("Donoran/Connor Forest (0:07:34)")
donoran_df = pd.DataFrame(
    {
        "Event": [
            "🫙 Item", 
            "🍞 Item", 
            "🪽 Item",
            "❔ Spirit 6",
            "- Action -",
            ],
        "Notes": [
            "Dew Drop: In Donoran shop", 
            "Honey Bread: In Donoran shop talk to dude", 
            "Wings: Get Donoran Wings",
            "In the light brown open space at the bottom of the city",
            "Use wings and leave Donoran",
            ]
    }
)
st.table(donoran_df)

with st.container(border=True):
    st.subheader("Connor Forest Tips")
    st.write("For Exp: you want group of 5-6 Bat’s. It’s a spirit lvl up after you kill them. Round them up and water pillar them.")
    st.write("For Defense Farm: you want a solo Marionasty or the Frog Knights. you want to get hit by a bunch of wind cutters.")

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



st.divider()

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

with st.container(border=True):
    st.subheader("Solvaring Tips")
    st.write("200 HP")
    st.write('''Don’t get close to him on pull from the chest.  
             Use Ice Knife to get him sub-50 and dodge his hand beam.  
             Then go in to get him with water pillar lvl 2  
             Stay decently far back with water pillar so that he wont do his ground pound move.  
             ''')
    st.write()

solvaring_2_df = pd.DataFrame(
    {
        "Event": [
            "- Action -",
            "🫙 Item", 
            ],
        "Notes": [
            "Use Exit to get to start of Forest. Head towards Dondoran Flats.", 
            "Dew Drop: In chest by Dondoran Flats entrance", 
            ]
    }
)
st.table(solvaring_2_df)

st.write("End at 0:25:05")