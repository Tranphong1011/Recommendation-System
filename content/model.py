import streamlit as st

def model(x):
    if x == 0:
        url_surprise = "https://surpriselib.com/"
        url_surprise_models = "https://github.com/NicolasHug/Surprise/blob/46b9914995e6c8c7d227b46f2eaeef2d4600580f/doc/source/refs.bib"
        url_als = "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALS.html"


        st.markdown("### What is Surprise?")
        st.markdown(
            f"""
            
            <a style='color: black;' href='{url_surprise}'><b>Surprise</b></a>, whose full name is “Simple Python RecommendatIon System Engine,” is a valuable resource for anyone 
            looking to build recommendation systems. It was created to make the process of creating recommendations more 
            accessible and less complicated. But what makes Surprise so special? 

            1. **Easy to use**: Surprise is designed to make even beginners feel like experts. If you’ve ever tried to assemble furniture with confusing instructions, you know how frustrating it can be. Surprise is the opposite: its instructions are clear, and its pieces fit together perfectly. You don’t need to be a programming wizard to get started. With just a few lines of code, you can have a basic recommendation system up and running.
            2. **Fast and efficient**: In the world of programming, time is precious. Nobody wants to wait hours to see the results of their work. Surprise is like an Olympic runner: fast and agile. Its algorithms are optimized so that you can get quality recommendations in the blink of an eye.
            3. **Supportive community**: Imagine having a problem and a group of expert friends ready to help you. That’s what the Surprise community offers. It’s a network of people who share tips, solve doubts, and constantly improve the library. It’s like having a team of superheroes by your side.
            
            In a nutshell, Surprise is the perfect tool to dive into the exciting world of recommendation systems without having to worry about technical obstacles.
            Note that surprise does not support implicit ratings or content-based information.
            
            """
        , unsafe_allow_html=True)
        st.markdown(
            f"""
            Surprise was also designed with the following purposes in mind:
            
            - Provide various ready-to-use prediction algorithms such as baseline algorithms, neighborhood methods, matrix factorization-based ( SVD, PMF, SVD++, NMF), and many others. Also, various similarity measures (cosine, MSD, pearson…) are built-in. I will not detail the different models but provide some resources if you are interested in knowing more about them (all the papers behind these groups are <a style='color: black;' href='{url_surprise_models}'>here</a>).
            - Make it easy to implement new algorithm ideas.
            - Provide tools to evaluate, analyse and compare the algorithms’ performance. Cross-validation procedures can be run very easily using powerful CV iterators (inspired by scikit-learn excellent tools), as well as exhaustive search over a set of parameters.
            
            """
        , unsafe_allow_html=True)

        st.markdown("### Apache Spark ML with ALS")

        st.markdown(
            f"""
            Apache Spark ML implements alternating least squares (<a style='color: black;' href='{url_als}'>ALS</a>) for collaborative filtering, a very popular algorithm for making recommendations.

            ALS recommender is a matrix factorization algorithm that uses Alternating Least Squares with Weighted-Lamda-Regularization (ALS-WR). It factors the user to item matrix A into the user-to-feature matrix U and the item-to-feature matrix M: It runs the ALS algorithm in a parallel fashion. The ALS algorithm should uncover the latent factors that explain the observed user to item ratings and tries to find optimal factor weights to minimize the least squares between predicted and actual ratings.
            
            """
        , unsafe_allow_html=True)
        st.image("./pictures/low_rank_matrix_factor.png")
        st.markdown(
            f"""
            We also know that not all users rate the products (movies), or we don’t already know all the entries in the matrix. With collaborative filtering, the idea is to approximate the ratings matrix by factorizing it as the product of two matrices: one that describes properties of each user (shown in green), and one that describes properties of each movie (shown in blue).
            """
        )

        st.markdown("### How about Deep Learning?")

