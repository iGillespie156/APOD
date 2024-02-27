import streamlit as st
import os
import requests

key = os.getenv("NASAKEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

response = requests.get(url)

response = response.json()
description = response["explanation"]
date = response["date"]
image = requests.get(response["url"])
image = image.content

print(response)



st.title("APOD - Ian's version")
st.subheader("Trying to have fun while learning to code")
st.write(date)
if response["media_type"] == 'video':
    st.video(response["url"])
else:
    st.image(image)

    


st.write(description)

#if request["media_type"] is not "video":




#with open(image, "wb") as pic:









