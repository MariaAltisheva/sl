import streamlit as st
from PIL import Image
# success
st.success("Привет")

# success
st.info("Как дела")

# success
st.warning("Warning")

# success
st.error("Error")

img = Image.open("rabbit.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=500)


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")