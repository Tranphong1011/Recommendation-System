import streamlit as st
from content.intro import intro
from content.data import data
st.title("Recommender Systems")
st.sidebar.title('Categories')
# """
# # Data Science Project
#
# [![Star](https://img.shields.io/github/stars/jrieke/traingenerator.svg?logo=github&style=social)](https://gitHub.com/jrieke/traingenerator/stargazers)
# &nbsp[![Follow](https://img.shields.io/twitter/follow/jrieke?style=social)](https://www.twitter.com/jrieke)
# &nbsp[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/jrieke)
# """
# Sample movie data

# Define your topics and subtopics
topics = {
    'Home': [],
    'Introduction': ['What is recommendation system?', 'Types of Recommendations', 'Men\'s Fashion Recommendations'],
    'Data Process and Explore': ['Dataset', 'Data Process', 'Data Exploration'],
    'Model Build Process': ['Top Models for Recommendations', 'Collaborative Filtering', 'Content-based Filtering'],
    'Conclusions': [],
    'User Interaction': ['Recommendation Based on User', 'Recommendations Based on Content'],
    'References': [],
}


# Sidebar with categories and subcategories
selected_category = st.sidebar.radio('Select Category', list(topics.keys()), index=0)

# Display subcategories for the selected category
if topics[selected_category]:
    st.sidebar.markdown("<h2 style='margin-bottom:0'>Subcategories:</h2>", unsafe_allow_html=True)
    selected_subcategory = st.sidebar.radio('Select Subcategory', topics[selected_category])
    if selected_subcategory in topics['Introduction']:
        intro((topics['Introduction'].index(selected_subcategory)))
    elif selected_subcategory in topics['Data Process and Explore']:
        data((topics['Data Process and Explore'].index(selected_subcategory)))



    # elif selected_subcategory in topics['Introduction']:

else:
    st.sidebar.write("No subtopics available for this category.")





