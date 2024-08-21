import streamlit as  st
import google.generativeai as genai

#title for the streamlit
st.title("welcome to chatbot intergrated with gemini ai")

#configure API key for google Generative AI
genai.configure(api_key="AIzaSyCnNtq5lfYpOeTX6w8eWXd7ExA5nO-Q-R0")

#input field for user question
text = st.text_input("Enter your question")

#intialize the generative model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[]) #start a new chat session


if st.button("answer"): #when this clicked to print the output
    response = chat.send_message(text) #send the user's input as a message
    st.write(response.text) #display the response
    
    
    
    
    
