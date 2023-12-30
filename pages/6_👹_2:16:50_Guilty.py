import streamlit as st
import pandas as pd

st.title("Guilty", anchor=None, help=None)
st.warning('''##### Goals: 156 HP, 24 MP, 50 Earth, 46 Water.''')

st.header("Baragoon Moor/Brannoch Castle (2:02:00)")
st.image('images/BaragoonMoor.jpg')
baragoon_moor_df = pd.DataFrame(
    {
        "Event": [
            "❔ Spirit 63",
            "❔ Spirit 64",
            "🏺🪆🔔 Item",
            "🍸🥾🪈 Item",
            "❔ Spirit 65",
            "- Action -",
            "❔ Spirit 66",
            "- Action -",
            "- Action -",
            ],
        "Notes": [
            "Behind the house you can save in when you exit the Boil Hole. Don't save!",
            "On the second floor of Baragoon Moor Inn",
            "Dragon's Potion, Replica, and Celene's Bell: Go in room to left in inn upstairs",
            "Spirit Light, Giant’s Shoes, and Silent Flute: Go in room to right in inn upstairs",
            "As you approach Brannoch go up and take a right then continue straight",
            "Go through the castle fortification door and come back out (to set Return point)",
            "As you approach Brannoch go up and take a left, follow it left to the end",
            "Use Return",
            "Save at Stewart",
            ]
    }
)
st.table(baragoon_moor_df)
st.info('''
        ### Brannoch Castle Tips
        * You want to Escape/run from every encounter. Ignore everything and focus on getting to Guilty. 
        ''')
st.write('''Make sure to have 156 HP, 24 MP, 50 Earth, and 46 Water before going to Guilty.  
        ''')

st.header("Guilty (2:10:32)")
st.error('''
        ### Guilty Tips
        ###### 1,800 HP
        * Engage by walking close to him. Take 1 step near his left foot. Start Magic Barrier/Avalanche.  
        * If you fail Magic Barrier twice: Run away, wait for him to do the claw move, Magic Barrier and items to heal up, then get close near his left foot with 1 step and then Magic Barrier / Avalanche combo.  
        * This is the hardest boss so use items liberally!
        ''')

st.write("End at 2:16:15")