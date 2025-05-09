# =====================================================
# 📦 Import required libraries
# =====================================================

# Streamlit is an open-source Python library that helps you create interactive web apps for data science and machine learning
import streamlit as st # Web app framework
# pandas is a popular library for data manipulation and analysis, especially when working with tables (dataframes)
import pandas as pd # Data manipulation
# seaborn is a statistical data visualization library based on matplotlib, providing a high-level interface for drawing attractive graphics
import seaborn as sns # Dataset source (and optional plotting)
# plotly.express is a high-level interface for Plotly, which is a graphing library that makes interactive, publication-quality graphs online
import plotly.express as px # Interactive plotting

# =====================================================
# ⚙️ Basic Streamlit App Configuration
# =====================================================
# This sets up some properties of the app page like its title, favicon, and layout width
st.set_page_config(page_title="My First Streamlit App", page_icon=":tada:", layout="wide")

# =====================================================
# 🎨 Custom CSS styling using markdown
# =====================================================
# Here we inject some CSS (web styling language) to customize the look and feel of the Streamlit app
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
        }
        .main-title {
            color: #4CAF50;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #2c3e50;
            color: white;
        }
        .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
            color: #ecf0f1;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            margin-right: 5px;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #45a049;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #2e7d32;
        }
        .stDataFrame {
            border: 2px solid #4CAF50;
            border-radius: 5px;
        }
        .column-image {
            text-align: center;
        }
        .column-image img {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================
# 🧱 Sidebar (navigation panel on the left)
# =====================================================
# The sidebar lets you add filters, menus, inputs, or display text/images
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo")
st.sidebar.title("Sidebar Menu")
st.sidebar.header("Sidebar Header")
st.sidebar.subheader("Sidebar Subheader")
st.sidebar.text("Hello, World!")

# =====================================================
# 📂 Tab layout - dividing the main area into multiple tabs
# =====================================================
tab1, tab2, tab3 = st.tabs(["Text", "Multimedia & Resources", "DataFrame"])

# ---------- Tab 1: Text Elements ----------
with tab1:
    st.markdown('<h1 class="main-title">My First Streamlit App</h1>', unsafe_allow_html=True)
    st.header("Main Header")
    st.subheader("Subheader")
    st.text("Simple text: Hello, World!")

    st.markdown("## Markdown Header")
    st.markdown("This is **bold text** using Markdown syntax")

    # LaTeX is a language used to format mathematical formulas
    st.latex(r"""a^2 + b^2 = c^2""")

    # Code block display with syntax highlighting
    st.code("print('Hello World')", language="python")

    # Message boxes with different purposes
    st.info("Info message")
    st.warning("Warning message")
    st.error("Error message")
    st.success("Success message")

    # Simulated error/exception output
    st.exception("Example of an exception message")

# ---------- Tab 2: Multimedia ----------
with tab2:
    # Show an image using a direct URL
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo")

    # Play audio from a URL
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    # Embed a YouTube video
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# ---------- Tab 3: DataFrame ----------
with tab3:
    # Create a small table using pandas DataFrame
    df = pd.DataFrame({
        'Column 1': [1, 2, 3, 8],
        'Column 2': [4, 5, 6, 15],
        'Column 3': [7, 8, 9, 22]
    })

    # Display the table as an interactive widget
    st.dataframe(df)

# =====================================================
# 🖼️ Displaying images in three columns
# =====================================================
# Streamlit allows you to create responsive layouts using columns
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Logo 1", width=200)
with col2:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Logo 2", width=200)
with col3:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Logo 3", width=200)

# =====================================================
# 🧹 Simple data cleaning function
# =====================================================
def clean_df(df):
    """
    Fill missing values (NaNs) in the DataFrame.
    It uses three strategies in order:
    1. Fill with mean of each column
    2. Fill remaining NaNs with the median
    3. Fill final NaNs (if any) with the mode (most frequent value)
    """
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.fillna(df.mode().iloc[0], inplace=True)
    return df

# =====================================================
# 🔁 Using Session State in Streamlit
# =====================================================
# Streamlit's session_state is used to store variables between interactions.
# It's useful for keeping things like counters, user inputs, or login state.

# Create a counter variable in session_state if it doesn't already exist
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Define functions that update the session state
def increment_counter():
    st.session_state.counter += 1

def decrement_counter():
    st.session_state.counter -= 1

def reset_counter():
    st.session_state.counter = 0

# =====================================================
# 📊 Counter interface with buttons
# =====================================================
st.title("Counter")
st.write(f"Current counter value: {st.session_state.counter}")

# Buttons to control the counter (inside 3 columns)
b1, b2, b3 = st.columns(3)
with b1:
    if st.button("Increment"):
        increment_counter()
with b2:
    if st.button("Decrement"):
        decrement_counter()
with b3:
    if st.button("Reset"):
        reset_counter()

# =====================================================
# 🛳 Titanic Dataset Analysis - Streamlit App
# =====================================================

# Load and clean data
@st.cache_data
def load_data():
    df = sns.load_dataset('titanic')
    df.dropna(subset=['sex', 'survived', 'class', 'age'], inplace=True)
    return df[['sex', 'survived', 'class', 'age', 'fare']]

titanic_df = load_data()

# Map survival values to more descriptive text
titanic_df['survival_status'] = titanic_df['survived'].map({0: 'Did not survive', 1: 'Survived'})

# =============================
# 🧭 Dashboard title & intro
# =============================
st.title("🚢 Titanic Dataset Interactive Dashboard")
st.markdown("This dashboard explores passenger survival data from the Titanic dataset using interactive visualizations.")

# ======================================
# 🔎 Filters on the main page (not sidebar)
# ======================================
st.subheader("🔍 Filter the Data")

# Layout: 3 columns for filters
col1, col2, col3 = st.columns(3)

# Class filter
with col1:
    selected_classes = st.multiselect(
        "Select Passenger Class:",
        options=titanic_df['class'].unique().tolist(),
        default=titanic_df['class'].unique().tolist()
    )

# Sex filter
with col2:
    selected_sex = st.multiselect(
        "Select Sex:",
        options=titanic_df['sex'].unique().tolist(),
        default=titanic_df['sex'].unique().tolist()
    )

# Age filter
with col3:
    min_age = int(titanic_df['age'].min())
    max_age = int(titanic_df['age'].max())
    selected_age = st.slider(
        "Select Age Range:",
        min_value=min_age,
        max_value=max_age,
        value=(min_age, max_age)
    )

# =====================================
# 📋 Filter the dataset based on input
# =====================================
filtered_df = titanic_df[
    (titanic_df['class'].isin(selected_classes)) &
    (titanic_df['sex'].isin(selected_sex)) &
    (titanic_df['age'] >= selected_age[0]) &
    (titanic_df['age'] <= selected_age[1])
]

# =====================================
# 🧾 Display filtered dataset
# =====================================
st.subheader("📄 Cleaned Titanic Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Define custom colors
custom_colors = {
    "Did not survive": "#800000",  # Wine red
    "Survived": "#556B2F"          # Olive green
}

# =====================================
# 📊 Survival by Sex (bar chart)
# =====================================
st.subheader("🧍 Survival by Sex")
grouped_sex = filtered_df.groupby(['sex', 'survival_status'], as_index=False).size()

fig_sex = px.bar(
    grouped_sex,
    x='sex',
    y='size',
    color='survival_status',
    barmode='group',
    title="Survival Count by Sex",
    labels={'survival_status': 'Survival Status', 'sex': 'Sex', 'size': 'Count'},
    color_discrete_map=custom_colors,
    category_orders={"survival_status": ["Did not survive", "Survived"]}
)
fig_sex.update_layout(legend_title="Survival Status")
st.plotly_chart(fig_sex, use_container_width=True)

# =====================================
# 📊 Survival by Class (bar chart)
# =====================================
st.subheader("🎫 Survival by Class")
grouped_class = filtered_df.groupby(['class', 'survival_status'], as_index=False).size()

fig_class = px.bar(
    grouped_class,
    x='class',
    y='size',
    color='survival_status',
    barmode='group',
    title="Survival Count by Class",
    labels={'survival_status': 'Survival Status', 'class': 'Passenger Class', 'size': 'Count'},
    color_discrete_map=custom_colors,
    category_orders={"survival_status": ["Did not survive", "Survived"], "class": ["First", "Second", "Third"]}
)
fig_class.update_layout(legend_title="Survival Status")
st.plotly_chart(fig_class, use_container_width=True)

# =====================================
# 📉 Scatter Plot: Age vs Fare (or other)
# =====================================
st.subheader("📈 Explore Numeric Relationships")

numeric_cols = ['age', 'fare']
x_axis = st.selectbox("Select X-axis:", options=numeric_cols, index=0)
y_axis = st.selectbox("Select Y-axis:", options=numeric_cols, index=1)

fig_scatter = px.scatter(
    filtered_df,
    x=x_axis,
    y=y_axis,
    color='survival_status',
    title=f"{x_axis.capitalize()} vs {y_axis.capitalize()} Colored by Survival Status",
    labels={'survival_status': 'Survival Status', x_axis: x_axis.capitalize(), y_axis: y_axis.capitalize()},
    color_discrete_map=custom_colors,
    hover_data=['sex', 'class']
)
fig_scatter.update_layout(legend_title="Survival Status")
st.plotly_chart(fig_scatter, use_container_width=True)