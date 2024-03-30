import streamlit as st

def model(x):
    if x == 0:
        # Create a select box with some options
        options = ["Collaborative Filtering", "Content - based Filtering"]
        selected_option = st.selectbox("Select an option",options )
        if selected_option == options[0]:

            url_surprise = "https://surpriselib.com/"
            url_surprise_models = "https://github.com/NicolasHug/Surprise/blob/46b9914995e6c8c7d227b46f2eaeef2d4600580f/doc/source/refs.bib"
            url_als = "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALS.html"
            url_fastai = "https://www.fast.ai/"

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
            st.markdown(
                f"""
                As the growth in the volume of data available to power recommender systems accelerates rapidly, data scientists are increasingly turning from more traditional machine learning methods to highly expressive deep learning models to improve the quality of their recommendations. 
    
                Broadly, the life-cycle of deep learning for recommendation can be split into two phases: training and inference. In the training phase, the model is trained to predict user-item interaction probabilities (calculate a preference score) by presenting it with examples of interactions (or non-interactions) between users and items from the past.
                """
            )
            st.image("./pictures/dl_training.png", caption = "Deep learning for recommendation training. ")
            st.markdown(
                f"""
                Once it has learned to make predictions with a sufficient level of accuracy, the model is deployed as a service to infer the likelihood of new interactions. 
                
                """
            )
            st.image("./pictures/dl_inference.png", caption="Deep learning for recommendation inference. ")
            st.markdown(
                f"""
                This inference stage utilizes a different pattern of data consumption than during training:
    
                - Candidate generation: pair a user with hundreds or thousands of candidate items based on learned user-item similarity.
                - Candidate ranking: rank the likelihood that the user enjoys each item.
                - Filter: show the user the item they are rated most likely to enjoy.
                """
            )
            st.image("./pictures/dl_inference.png", caption="Deep learning for recommendation inference: candidate generation, ranking and filtering.")
            st.markdown(
                f"""
                PyTorch works best as a low-level foundation library, providing the basic operations for higher-level functionality. The <a style='color: black;' href='{url_fastai}'><b>fastai library </b></a>  one of the most popular libraries for adding this higher-level functionality on top of PyTorch.
                
                In this project, we are going to work on Men's Fashion recommendation problem using Fastai. 
                """
            , unsafe_allow_html=True)
        else:
            url_gensim = "https://pypi.org/project/gensim/"
            url_cosinsim = "https://naomy-gomes.medium.com/the-cosine-similarity-and-its-use-in-recommendation-systems-cb2ebd811ce1"
            st.markdown("### Gensim library and its applications")
            st.image("./pictures/gensim.png")
            st.markdown(
                f"""
                Textual data is abundant in today’s digital world, and extracting meaningful insights from it is a challenging task. <a style='color: black;' href='{url_gensim}'><b>Gensim</b></a> , a popular Python library, provides a powerful toolkit for topic modeling, natural language processing (NLP), and semantic analysis. 
                
                Word embeddings are dense vector representations of words that capture semantic and syntactic information. Gensim provides an easy way to train and use word embeddings using algorithms like **Word2Vec** and **FastText**.
                
                Gensim provides functionality for computing similarities between texts and documents using techniques like cosine similarity. This can be useful for tasks like document retrieval, recommendation systems, and clustering.
                
                Gensim’s similarity calculations can be extended to other metrics and algorithms, enabling you to explore various approaches for measuring text and document similarity based on your specific requirements.

                Gensim is a powerful library that offers a wide range of capabilities for topic modeling, word embeddings, and text similarity analysis. In this blog post, we explored the practical applications of Gensim, focusing on topic modeling, word embeddings, and text/document similarity. By incorporating Gensim into your NLP projects, you can uncover hidden patterns, extract meaningful insights from textual data, and enhance the performance of various natural language processing tasks. Embrace the power of Gensim and leverage its tools to gain valuable knowledge from textual information.
                """
            , unsafe_allow_html=True)

            st.markdown("### How about cosines similarity? ")
            st.markdown(
                f"""
                A recommendation system can be as complicated as we want, such as the ones that use deep learning [1,2], but they can also be simple and based on the similarity between items. And one way to calculate the similarity between items is with the use of <a style='color: black;' href='{url_cosinsim}'><b>cosine similarity</b></a>.
                
                To understand this metric of similarity, we first need to understand some concepts. Suppose we have a table of books 1 and 2 containing their genre. To each word in the genre table, we create another column in a second table, where if the word is in the genre, we give it 1, if it's not, then is 0. Since we have the genres Science Fiction and Fiction, we create another table with these two words. If we draw a graph where the x-axis is the Science axis and the Y-axis is the Fiction axis, we can associate a point to each book. For example, book 1 will be the blue point with a Sience-axis of 1 and a Fiction-axis of 1 (Science Fiction). Book 2 will be the yellow point with a Sience-axis of 0 and a Fiction-axis of 1 (Fiction). We draw a vector from the origin to the points, which we call the book-vector.
                """
            , unsafe_allow_html=True)
            st.image("./pictures/cosinsim.jpg", caption = "Book table containing genres and a graph showing the book-vectors.")
            st.markdown("Now, we can see that the book-vectors form an angle θ with each other. The cosine of this angle is our measure of similarity, and it is given by:")
            st.image("./pictures/formula.jpg")
            st.markdown("where **A** and **B** are the vectors we are considering, ||A|| and ||B|| are their norm (length). The **A**i and **B**i in the formula are the components of each vector. Book-vector 1 is (1,1), and book-vector 2 is (0,1). Let’s calculate the cosine similarity:")
            st.image("./pictures/formula_2.jpg")
            st.markdown(
                f"""
                which says two things: first, these vectors have some similarity, and second, θ is 45º, something that we already expected and could calculate by using the Pythagorean theorem and calculating the cosine using the sides of the triangle.

                If both books were Science Fiction, we would have the same book-vectors (1,1) and the cosine would be 1, meaning they are the same. But if book 1 were Science Fiction (1,1) and book 2 Terror (0,0), in this case, they would have nothing in common, and the cosine would be 0. Therefore, _high similarity means a cosine close to 1, and low similarity, a cosine close to 0_.
                """
            )
    elif x == 1:
        options = ["Surprise package", "ALS Spark Apache", "Deep Learning with Fastai"]
        selected_option = st.selectbox("Select an option",options )
        if selected_option == options[0]:
            st.markdown(
                f"""
                We compared the preformance each of the algorithms from surprise package and we got the result as shown below:
                
                """
            )
            st.image("./pictures/rmse.jpg")
            st.markdown(
                f"""
                Based on the comparison, it’s evident that **SVD (Singular Value Decomposition)** and **SBOnly** have shown the best performance. SBOnly achieves an RMSE of approximately **0.88**, while the MAE is impressively low at **0.58**.
    
                However, before we finalize our decision on the best algorithm from the Surprise package for collaborative filtering tasks, we need to consider the **computational time** required by each of these algorithms. It’s essential to strike a balance between accuracy and efficiency. Once we evaluate the time complexity, we can make a more informed choice. 🕰️🤔
                """
            )
            st.image("./pictures/time_taken.jpg")
            st.markdown(
                f"""
                Considering both accuracy and computational efficiency, it’s great to hear that SBOnly performs well in terms of both metrics. With an RMSE of approximately **0.88** and a remarkably low MAE of **0.58**, coupled with a shorter execution time of **55.8** seconds, it’s a sensible choice for collaborative filtering tasks. 
                
                Prioritizing user experience is essential, and SBOnly seems to strike the right balance. 🚀🌟                
                """
            )
        elif selected_option == options[1]:
            st.markdown("We kicked off the ALS (Alternating Least Squares) model by initializing several parameters, including maxIter, regParam, and coldStartStrategy. Afterward, we assessed its performance using the Root Mean Square Error (RMSE). This evaluation helps us understand how well the model is performing. 📊🔍")
            # Define a Python code block
            python_code = """
            als = ALS(
                maxIter=5,            
                regParam=0.01,        
                userCol="user_id",      
                itemCol="product_id",     
                ratingCol="rating",   
                coldStartStrategy="drop",  
                nonnegative=True      
            )
            """
            st.code(python_code, language='python')
            st.markdown("The Root Mean Square Error (RMSE) value of **1.9247** appears to be higher than any of the RMSE values we obtained from the algorithms in the Surprise package that we evaluated. This discrepancy prompts us to fine-tune the ALS (Alternating Least Squares) model further. Let’s explore whether we can improve its performance. 📊🔍")

            python_code_1 = """
            als_t = ALS(
                maxIter=10,             
                regParam=0.1,         
                userCol="user_id",      
                itemCol="product_id",     
                ratingCol="rating",    
                coldStartStrategy="drop",  
                nonnegative=True       
            )
            """
            st.code(python_code_1, language='python')
            st.markdown(
                f"""
                We adjusted the maxIter and regParam parameters while keeping the others unchanged. As a result, the Root Mean Square Error (RMSE) improved significantly, dropping to **1.237**. However, even with this improvement, it remains higher compared to the SBOnly algorithm. Additionally, the training time for this ALS model was more than 5 minutes.

                Given these observations, it’s worth reconsidering whether we should continue using this model. Further fine-tuning and evaluation are necessary to make an informed decision. 🤔📊
                """
            )
        else:
            st.markdown("Nothing to show. We are doing on this")
    else:
        options = ["Gensim", "Cosines Similarity"]
        selected_option = st.selectbox("Select an option",options )
        if selected_option == options[0]:
            st.image("./pictures/process_gensim.jpg")
            st.markdown(
                f"""
                1. **Creating a Dictionary**:
                    - We start by converting your list of product names (_products_gem_re_) into a dictionary.
                    - This dictionary maps words (product names) to unique integer IDs. Think of it as creating a vocabulary.
                2. **Building the Corpus**:
                    - Next, we create a corpus based on this dictionary.
                    - The corpus represents each document (product name) as a bag of words (word IDs and their frequencies).
                2. **TF-IDF Model**:
                    - We use the TF-IDF (Term Frequency-Inverse Document Frequency) model to process the corpus.
                    - TF-IDF assigns weights to words based on their importance in a document relative to the entire corpus.
                3. **Sparse Matrix Similarity**:
                    - Now, we calculate the similarity between documents using a sparse matrix approach.
                    - The index represents the similarity index based on the TF-IDF-transformed corpus.
                4. **Data Result**:
                    Finally, we create a DataFrame (_data_result_) containing the similarity scores for each document.
                """
            )
            st.image("./pictures/gensim_df.jpg")
        else:
            st.markdown(
                f"""
                
                1. **Creating a TF-IDF Vectorizer**:      
                    - First, we create a TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer using the TfidfVectorizer class.
                    - This vectorizer processes the list of product names (_product_name.products_gem_re_).
                    
                2. **TF-IDF Matrix**:              
                    - Next, we apply the vectorizer to the product names.
                    - The result is a TF-IDF matrix (_tfidf_matrix_), where each row corresponds to a product name, and each column represents a unique word (feature).
 
                3. **Calculating Cosine Similarities**:               
                    - We compute the cosine similarities between all pairs of product names.
                    - Cosine similarity measures the cosine of the angle between two vectors (in this case, the TF-IDF vectors).
                    - Higher cosine similarity indicates greater similarity between the product names.

                4. **Creating a DataFrame**:               
                    - Finally, we organize the cosine similarity scores into a DataFrame (_data_result_cosine_similarities_).
                    - Each cell in the DataFrame represents the similarity score between two product names.
                    """
            , unsafe_allow_html=True)
            st.image("./pictures/gensim_df.jpg")
            st.markdown(
                f"""
                After comparing the performance of Gensim and cosine similarity, we can make an informed decision about which method to use. We have generated 10 random 10 product IDs from the given list of products to run a recommendation system using both the Gensim and cosine similarity models. 
                """
            )
            st.image("./pictures/gensim_vs_cssim.jpg")
            st.markdown(
                f"""
                From the bar chart, it’s evident that when executing both Gensim and cosine similarity models simultaneously for 10 random products, Gensim outperforms in terms of execution time. This results in a **better user experience compared to cosine similarity**. 🚀🕰️               
                """
            )
            st.image("./pictures/gensim_vs_cssim_1.jpg")
            st.markdown(
                f"""
                We also compared the similarity scores produced by both the Gensim and cosine similarity models when recommending each product from the given list. Surprisingly, the results from these two models were **quite similar**.

                ===> Therefore, based on the outcomes and processing time of both models, we opt for Gensim for our content-based recommendation system. 🚀🌟
                """
            )





