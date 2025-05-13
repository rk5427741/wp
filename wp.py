import streamlit as st 
import pickle

st.title("Weather Prediction App.")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter maximum temperature")
mint=st.number_input("Enter minimum temperature")
wind=st.number_input("Enter wind speed")
button=st.button("Predict!")
# To load model
if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"Today weather situation : {res}")