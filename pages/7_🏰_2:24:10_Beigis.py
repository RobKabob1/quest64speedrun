import streamlit as st
import pandas as pd

st.title("Beigis", anchor=None, help=None)
st.warning('''##### Goals: 182 HP, 24 MP, 50 Earth, 49 Water.''')

st.header("More Brannoch Castle (2:16:50)")
brannoch_df = pd.DataFrame(
    {
        "Event": [
            "🔺🍾 Item", 
            "🌿 Item", 
            "🏺🔺 Item", 
            "❔ Spirit 62",
            "- Action -"
            ],
        "Notes": [
            "Healing Potion & Hero's Drink: 2 chests in checkered floor room after Guilty", 
            "Mint Leaves: chest outside of save room", 
            "Dragon's Potion & Healing Potion: inside save room",
            "Inside save room",
            "Skip chests in room with Shannon and Brian's father",
            ]
    }
)
st.table(brannoch_df)
st.write('''Continue onto Beigis. You should have 182 HP, 24 MP, 50 Earth, and 49 Water at this point. If not, just engage anyway.  
        ''')

st.header("Beigis (2:20:27)")
st.error('''
        ### Beigis Tips
        ###### 1,900 HP
        * All attacks hit extremely hard. Top your HP off always.  
        * Engage with Magic Barrier, use Giant's Boots, Magic Barrier, line up with carpet and ledge, then Avalanche / Magic Barrier away.
        ''')

st.write("End at 2:24:10")
