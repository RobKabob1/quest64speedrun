import streamlit as st
import pandas as pd

st.title("Fargo", anchor=None, help=None)
st.warning('''##### Goals: 136 HP, 23 MP, 50 Earth, 39 Water.''')

st.header("Dindom Dries/Boil Hole (1:43:41)")
st.image('images/DindomDries.jpg')
dindom_dries_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 58",
            "❔ Spirit 59",
            "- Action -",
            "❔ Spirit 60",
            ],
        "Notes": [
            "Inside in a pot in the tent",
            "Head southwest from the tent to the house. It's right before the wall.",
            "Save at Edward in the Inn",
            "To the right before you go in the Boil Hole",
            ]
    }
)
st.table(dindom_dries_df)
st.info('''
        ### Boil Hole Tips
        * You want to maximize move distance in the cave by running towards/through enemies in each encounter as long as you don't die.  
        * The goal is to reduce Rocky spawns because they are so horrendously slow and add time to the run.
        ''')
boil_hole_df = pd.DataFrame(
    {
        "Event": [
            "🏺 Item",
            "🔺 Item",
            "❔ Spirit 61",
            "🪆🥾 Item",
            ],
        "Notes": [
            "Dragon's Potion: first chest in Boil Hole",
            "Healing Potion: second chest in Boil Hole",
            "A bit after the second chest",
            "Replica & Giant's Shoes: two chests after spirit",
            ]
    }
)
st.table(boil_hole_df)
st.write('''Make sure to have 136 HP, 23 MP, 50 Earth, and 39 Water before going to Fargo.  
        ''')

st.header("Fargo (1:59:00)")
st.error('''
        ### Fargo Tips
        ###### 1,500 HP
        * Start by running to the right because we want him to approach us.  
        * Use Magic barrier, then he comes close, then you come close and Avalanche. If you do it right its 90%+ chance to hit every time.  
        * Fargo generally isn't worth using items on. You can use Confusion instead. Up close Fargo doesn't hurt as much.
        ''')
fargo_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 62",
            "🏺 Item", 
            ],
        "Notes": [
            "Around the corner to the right after facing Fargo", 
            "Dragon's Potion: chest after Fargo", 
            ]
    }
)
st.table(fargo_df)

st.write("End at 2:02:00")