import streamlit as st

def conclusion():
    st.markdown(
        f"""
        For each of the recommendation systems, we have reached the following conclusions:
        
        **Content-Based Filtering**: We opt for the Gensim library due to its superior performance and efficient processing time.
        
        **Collaborative Filtering**: We select the SBOnly algorithm from the Python Surprise package. It stands out with the lowest RMSE, MAE, and efficient processing time.
        
        These choices ensure a balance between accuracy and user experience. 🚀🌟
      
        """)
