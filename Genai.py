# import streamlit as st
# st.title("chau taset poll")

# col1,col2 = st.columns(2)

# with col1:
#     st.header("masala chai")
#     st.image("https://plus.unsplash.com/premium_photo-1669700572184-edbb6d28b452?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxfHx8ZW58MHx8fHx8",width=200)
#     vote1= st.button("vote masala chai")
# with col2:
#     st.header("adrak chai")
#     vote2= st.button("vote adrak chai")

# if vote1:
#     st.success("thanks for voting malsa chai")
# elif vote2:
#     st.success("thanks for voting adrak chai")


# name = st.sidebar.text_input("Entr the name ")
# tea = st.sidebar.selectbox("Choose chai ",["malsa","adrak","honey"])

# st.write(f"wlecome {name} and your loved chaiis {tea}.")


# with st.expander("show making cahi "):
#     st.write("""
#              1. chai
#              2.milk
#              3.honey 
#     """)

# st.markdown



import streamlit as st


# st.title("live currency converterr !")

# inr = st.number_input("ENter the currency in INR",min_value=1)

# con = st.selectbox("Choose the currency to convert",["USD","EURO","JAP/YEN","Pound"])


# usd= round(inr/87.80,2)
# eur=round(inr/101.35,2)
# yen=round(inr/0.59,2)
# pond =round(inr/116.64,2)


# if con=="USD":
#     st.success(f" ₹ {inr} INR converted to $ {usd}.")
# elif con=="EURO":
#     st.success(f" ₹ {inr} INR converted to {eur}")
# elif con=="JAP/YEN":
#     st.success(f" ₹ {inr} INR converted to {yen}")
# elif con=="Pound":
#     st.success(f" ₹ {inr} INR converted to {pond}")



st.chat_message("user")

prompt = st.chat_input("how was your mood !")

if prompt:
    st.chat_message("assistant")
    st.write(f"say what its said {prompt}")











