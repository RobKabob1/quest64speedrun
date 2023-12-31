import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Shilf",
    page_icon="❤️‍🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Shilf", anchor=None, help=None)
st.warning('''##### Goals: 115 HP, 22 MP, 50 Earth, 30 Water. Have max Earth for more Avalanche damage.''')

st.header("East Limelin (1:22:11)")
st.image('images/EastLimelin.jpg')
east_limelin_1_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 44", 
            "🌿🔺 Item",
            "❔ Spirit 45", 
            "🪽 Item",
            "❔ Spirit 46", 
            "❔ Spirit 47", 
            "❔ Spirit 48", 
            "❔ Spirit 49", 
            "- Action -",
            "❔ Spirit 50", 
            "❔ Spirit 51", 
            "❔ Spirit 52", 
            "❔ Spirit 53", 
            ],
        "Notes": [
            "Look right as you go down the path from the ship", 
            "Mint Leaves & Healing Potion: First House in Limelin upstairs",
            "In a wheat field to the right",
            "Wings: Get wings in Limelin",
            "To the left its a little dock",
            "Behind the statue in the courtyard",
            "Behind the big statue that is just inside the castle",
            "Another one next to previous spirit",
            "Use Limelin wings to get back to entrance and leave Limelin",
            "Take the right when you see circular path going down. By the dirt mound.",
            "Mining Cabin- Inside in plain view",
            "Another one next to previous spirit",
            "Between dirt mounds at the bottom of the circular path."
            ]
    }
)
st.table(east_limelin_1_df)
st.write("You should now have 50 Earth")

st.header("Baragoon Tunnel (1:30:06)")
st.info('''
        ### Baragoon Tunnel Tips
        * In this tunnel, be at full health most of the time because they hit hard.  
        * Watch out for the fire bomb guys. They hit for half health.
        ''')
baragoon_tunnel_df = pd.DataFrame(
    {
        "Event": [
            "🔺🍾 Item", 
            "❔ Spirit 54",
            "🔺 Item",
            "❔ Spirit 55",
            "❔ Spirit 56", 
            ],
        "Notes": [
            "Healing Potion & Hero's Drink: 2 chests at start",
            "In a big room after the third tunnel",
            "Mint Leaves: in chest next to previous spirit",
            "In high walled maze, take the left and it's by a dirt mound.",
            "To the left on the lower level in the room with the two levels",
            ]
    }
)
st.table(baragoon_tunnel_df)
st.write('''Make sure to have 115 HP, 22 MP, 50 Earth, and 30 Water before going to Shilf.  
        ''')

st.header("Shilf (1:40:32)")
st.error('''
        ### Shilf Tips
        ###### 1,000 HP
        * You want her to walk forward so your rocks can hit.  
        * Engage with a Magic barrier, skip turn, then Avalanche in her face.  
        * If she doesn’t walk just keep Magic Barrier + walk.  
        * Use MP items in between Magic Barrier.  
        * Her laser should do around 57 HP. Always be above this!  
        * If you have lots of HP items, then do Confusion to get MP. Then use HP item after Magic Barrier. This saves an MP item.  
        ''')
shilf_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 57",
            "📿🔺 Item", 
            ],
        "Notes": [
            "After fighting Shilf in the treasure room by the chests", 
            "Silver Amulet & Healing Potion: 2 chests with items near previous spirit", 
            ]
    }
)
st.table(shilf_df)

st.write("End at 1:43:41")