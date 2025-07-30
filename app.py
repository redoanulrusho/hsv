import streamlit as st
import cv2
import numpy as np

# Streamlit page setup
st.set_page_config(page_title="BGR to HSV Converter", page_icon="🎨")
st.title("🎨 BGR to HSV Converter (Streamlit Version) by RUSHO")

# Switch (like your s1 trackbar)
switch = st.radio("Switch", ["OFF", "ON"])

# BGR sliders
b = st.slider("B", 0, 255, 0)
g = st.slider("G", 0, 255, 0)
r = st.slider("R", 0, 255, 0)

# Display color based on switch
if switch == "OFF":
    bgr_color = (0, 0, 0)  # Black
else:
    bgr_color = (b, g, r)

# Convert BGR to HSV
hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]

# Show current BGR color and HSV value
st.write(f"**BGR:** {bgr_color}")
st.write(f"**HSV:** {tuple(hsv_color)}")

# Convert HSV to HEX (just for visualization)
color_hex = "#{:02x}{:02x}{:02x}".format(*cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2RGB)[0][0])

# Display color box
st.markdown(
    f"<div style='background-color:{color_hex}; width:500px; height:300px; border-radius:10px'></div>",
    unsafe_allow_html=True
)
