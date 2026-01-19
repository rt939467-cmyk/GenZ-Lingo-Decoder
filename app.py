import streamlit as st

# Website ka title aur look
st.set_page_config(page_title="GenZ AI Decoder", page_icon="💅")
st.title("💅 The Ultimate GenZ Decoder")
st.write("BCA Minor Project - Making 'Grown-ups' understand GenZ Lingo!")

# Badi Dictionary - Isme aur words add kar diye hain
genz_dict = {
    "Rizz": "Matlab 'Charisma'. Jab kisi ke paas kisi ko bhi impress karne ka talent ho.",
    "Slay": "Jab koi bahut accha kaam kare ya bahut accha dikhe. 'Slayed it!'",
    "Delulu": "Short for Delusional. Matlab khayali pulao pakana ya unreal umeed rakhna.",
    "Cap": "Matlab jhoot bolna. Agar koi kahe 'No Cap', matlab wo 100% sach bol raha hai.",
    "Sus": "Short for Suspicious. Matlab jab kuch gadbad lage ya shaq ho.",
    "Aura": "Aapki personality ki energy. 'Minus 1000 Aura' matlab aapne kuch embarrassing kiya.",
    "Cooked": "Matlab jab kisi ki buri tarah haar ho jaye ya wo kisi musibat mein phas jaye.",
    "Simp": "Jo kisi ke peeche pagal ho aur uski har baat maane.",
    "Tea": "Matlab 'Gossip'. 'Spill the tea' matlab gossip sunao.",
    "Flex": "Apni cheezon ka dikhawa karna. 'Stop flexing your new iPhone!'",
    "Bet": "Matlab 'Theek hai' ya 'Done'.",
    "Bussin": "Jab khana bahut hi zyada swadisht ho.",
    "G.o.a.t": "Greatest Of All Time. Matlab sabse best!",
    "Situationship": "Aisa rishta jo dosti se zyada ho par commitment na ho."
}

# User input
word = st.text_input("Koi GenZ word likho (e.g. Rizz, Slay, Delulu, Cap):")

if st.button("Decode Karo"):
    if word:
        # Search logic
        search_word = word.strip().capitalize()
        if search_word in genz_dict:
            st.success(f"**{search_word}:** {genz_dict[search_word]}")
        else:
            st.warning("Oops! Ye word abhi list mein nahi hai. Par fikar mat karo, ye GenZ log roz naye words banate hain!")
    else:
        st.error("Bhai, pehle word toh likho!")

# Sidebar mein guide
st.sidebar.header("Try These Words ✨")
for k in sorted(genz_dict.keys()):
    st.sidebar.markdown(f"- {k}")

st.sidebar.info("Tip: Viva mein bolna ki ye 'User-Friendly Interface' hai.")