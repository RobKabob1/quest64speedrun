import streamlit as st
import pandas as pd

st.title("Zelse", anchor=None, help=None)
with st.container(border=True):
    st.write('''Goals: 81 HP, 20 MP, 24 Earth, 23 Water. Have Avalanche and Escape.''')

st.divider()


st.header("Dondoran Flats/Glencoe Forest (0:25:05)")
st.image('images/Dondoran1.jpg')
dondoran_one_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 12", 
            "❔ Spirit 13", 
            ],
        "Notes": [
            "To the left off the path", 
            "To the right down the log and to the right again (to the left would be Glencoe Forest)",
            ]
    }
)
st.table(dondoran_one_df)

with st.container(border=True):
    st.write('''In Glenco Forest you want to hit the 23 Water goal, then go straight Earth.  
             Make sure to Escape encounters!''')
   
glenco_forest_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 14", 
            "❔ Spirit 15", 
            "❔ Spirit 16", 
            "❔ Spirit 17", 
            "🪈 Item", 
            "❔ Spirit 18", 
            "❔ Spirit 19", 
            "- Action -"
            ],
        "Notes": [
            "Follow the lake right it should be near the edge",
            "Follow the lake left and it's near where the lake nears the wall",
            "Near previous spirit, at the top of the hill",
            "Hug the right wall from previous spirit and you will reach an opening which leads to another half of the forest.  Continue to a cottage, the spirit is outside.",
            "Silent Flute: In cottage",
            "Near the blue cave rocks visible from the cabin",
            "Very close to previous, father from the water",
            "Use Exit to get to start of forest and head back to Dondoran",
            ]
    }
)
st.table(glenco_forest_df)
st.write("Follow the path south towards the boat")
st.image('images/Dondoran2.jpg')

dondoran_two_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 20", 
            ],
        "Notes": [
            "On the right side right before you can see the ship you'll see a short uphill opening",
            ]
    }
)
st.table(dondoran_two_df)
st.write("Get on boat to West Carmagh")

st.divider()

st.header("West Carmagh/Larapool (0:31:33)")
st.image('images/WestCarmagh.jpg')
west_carmagh_larapool_df = pd.DataFrame(
    {
        "Event": [
            "- Action -",
            "❔ Spirit 21",
            "❔ Spirit 22", 
            "🌿 Item", 
            "🪽 Item",
            "❔ Spirit 23",
            ],
        "Notes": [
            "Save at Efna for spawn point / death warp later", 
            "Coming off the ship, cross two bridges and go up the hill on your right", 
            "Continue on the path and you'll see another hill on your right",
            "Mint Leaves: Get from person at save spot in Larapool",
            "Wings: Get Larapool wings for use after Zelse",
            "Behind the save house before you enter Cull Hazard cave",
            ]
    }
)
st.table(west_carmagh_larapool_df)

with st.container(border=True):
    st.subheader("Cull Hazard Tips")
    st.write("For EXP farm: Get 4 blood jell group. Use Celene's bell or Silent Flute and then and Water Pillar away. 3. You get 2 elements from that.")
    st.write("Make sure to Escape run out of encounters as you run through the cave!")

cull_hazard_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 24",
            "🔺 Item",
            "🍾 Item",
            "❔ Spirit 25", 
            "🍞 Item", 
            "🔺 Item",
            "🪈 Item",
            ],
        "Notes": [
            "Around a rock formation and a single chest", 
            "Healing Potion: Near the previous spirit", 
            "Heroes Drink: Well into the cave by a wall",
            "Once you see the river go to the fork and take the left, near two chests",
            "Honey Bread",
            "Healing Potion",
            "Silent Flute: Once you're in the green area, head left"
            ]
    }
)
st.table(cull_hazard_df)
st.write('''Make sure to have 18 Earth before leaving Cull Hazard (important!)''')

st.divider()

st.header("Normoon/Windward Forest (0:52:37)")
normoon_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 26",
            "❔ Spirit 27",
            "🍞🍞 Item",
            "🍞🌿 Item",
            "❔ Spirit 28", 
            ],
        "Notes": [
            "In the large wheat field", 
            "Also in the large wheat field", 
            "Fresh Bread x2: chests in the left windmill",
            "Fresh Bread & MP Item: chests in the right windmill",
            "In the smaller wheat field",
            ]
    }
)
st.table(normoon_df)
with st.container(border=True):
    st.subheader("Windward Forest Tips")
    st.write('''Run from blaze female enemys and giant pig enemies.''')
windward_forest_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 29",
            "❔ Spirit 30",
            "❔ Spirit 31",
            "🍞 Item",
            ],
        "Notes": [
            "Around the first bend on your left", 
            "Near the cabin behind a tree", 
            "Inside the cabin",
            "Honey Bread: chest in cabin",
            ]
    }
)
st.table(windward_forest_df)

st.write('''Make sure to have 81 HP, 20 MP, 24 Earth, and 23 Water before going to Zelse.  
         Reasoning for this is that we need Avalanche.''')

st.divider()

st.header("Zelse (0:55:55)")
with st.container(border=True):
    st.subheader("Zelse Tips")
    st.write("680 HP")
    st.write('''We don't want him to walk up to us.  
             Fight him mid range so he does Ice Wall. You can dodge this.  
             His Large Cutter up close is the most dangerous move.  
             Engage with Spirit Armor as your first move, move close to him, then Avalanche away.
             ''')
st.write("After Zelse is dead put 25 in Water for Heal 2 and put the rest in Earth for 27")

zelse_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 30",
            "- Action -",
            "🌿 Item",
            ],
        "Notes": [
            "Behind a tree in the clearing where you fight Zelse", 
            "Use Larapool wings", 
            "Mint Leaves: Get from person at save spot in Larapool",
            ]
    }
)
st.table(zelse_df)

st.write("End at 0:59:43")