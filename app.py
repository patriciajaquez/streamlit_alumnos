# First we import the library to use
import streamlit as st
import pandas as pd
import plotly.express as px

#-------------------------------------------------------------------------------------------

# App setup
# For layout we can use wide or centered

st.set_page_config(page_title="My First Streamlit App", page_icon=":tada:", layout="wide")

#-------------------------------------------------------------------------------------------

# Texts
st.title("My First Streamlit App") # Principal title

# Headers
st.header("This is a header") # Header
st.subheader("This is a subheader") # Subheader

# Normal text
st.text("Hello, World!") # Normal text

# Markdown
st.markdown("## This is a markdown header") # Markdown header
st.markdown("This is a **markdown** subheader") # Markdown subheader

# Latex
st.latex(r"""a^2 + b^2 = c^2""") # Latex text

# Code
st.code("print('Hello, World!')", language="python") # Code text

# Information, warning, error and success messages
st.info("This is an info message") # Info message
st.warning("This is a warning message") # Warning message
st.error("This is an error message") # Error message
st.success("This is a success message") # Success message
st.exception("This is an exception message") # Exception message

#-------------------------------------------------------------------------------------------

# Media and resources
# Images , local route or URL, we can use width= and height= to resize the image
# st.image("path/to/image.png", caption="Image caption") # Local image
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit logo") # URL image

# Audios
# Local route or URL, we can use format= to set the audio format
# st.audio("path/to/audio.mp3") # Local audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # URL audio

# Videos
# Local route or URL, we can use format= to set the video format
# st.video("path/to/video.mp4") # Local video
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # URL video


#-------------------------------------------------------------------------------------------


df = pd.DataFrame({
    'Column 1': [1, 2, 3, 8],
    'Column 2': [4, 5, 6, 15],
    'Column 3': [7, 8, 9, 22]
})

st.dataframe(df) # Dataframe


#-------------------------------------------------------------------------------------------


# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.header("This is a sidebar header") # Sidebar header
st.sidebar.subheader("This is a sidebar subheader") # Sidebar subheader
st.sidebar.text("Hello, World!") # Sidebar normal text