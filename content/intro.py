import streamlit as st

def intro(x):
    if x ==0:
        st.markdown("### Recommender Systems: Why And How?")

        # Define the URL and text for the hyperlink
        url_recommendation = "https://en.wikipedia.org/wiki/Recommender_system"
        url_youtube = 'https://www.youtube.com/'
        url_sportify = 'https://open.spotify.com/'
        url_amazon = 'https://www.amazon.com/'

        url_youtube_info = 'https://www.oberlo.com/blog/youtube-statistics'
        url_sportify_info = 'https://newsroom.spotify.com/company-info/'
        url_amazon_info = 'https://www.retailtouchpoints.com/resources/how-many-products-does-amazon-carry'

        url_feedback = 'https://medium.com/analytics-vidhya/recommender-systems-explicit-feedback-implicit-feedback-and-hybrid-feedback-ddd1b2cdb3b'

        st.markdown(f"""
                <a style='color: black;' href='{url_recommendation}'><b>Recommender systems</b></a> are algorithms providing personalized suggestions
                for items that are most relevant to each user. With the massive growth
                of available online contents, users have been inundated with choices. It
                is therefore crucial for web platforms to offer recommendations of items
                to each user, in order to increase user satisfaction and engagement.
            """, unsafe_allow_html=True)

        st.image("./pictures/Youtube Recommends.jpg",
                 caption="YouTube recommends videos to users, to help them discover and watch content relevant to them in the middle of a huge number of available contents.")
        st.write("""
                YouTube recommends videos to users, to help them discover and watch
                content relevant to them in the middle of a huge number of available
                contents.
            """)

        st.markdown("""
                The following list shows examples of well-known web platforms with a
                huge number of available contents, which need efficient recommender
                systems to keep users interested:
            """)

        st.markdown(
            f""" 1. <a style='color: black;' href='{url_youtube}'><b>Youtube</b></a>. Every minute people upload <a style='color: black;' href='{url_youtube_info}'>500 hours of videos</a>, i.e. it would take 82 years for a user to watch all videos uploaded just in the last hour.""",
            unsafe_allow_html=True)
        st.markdown(
            f""" 2. <a style='color: black;' href='{url_sportify}'><b>Spotify</b></a>. Users can listen to more than <a style='color: black;' href='{url_sportify_info}'>80 million song tracks and podcasts.</a>""",
            unsafe_allow_html=True)
        st.markdown(
            f""" 3. <a style='color: black;' href='{url_amazon}'><b>Amazon</b></a>. Users can buy more than <a style='color: black;' href='{url_amazon_info}'>350 million different products.</a> """,
            unsafe_allow_html=True)

        st.write(
            "All these platforms use powerful machine learning models in order to generate relevant recommendations for each user.")

        st.markdown("### Explicit Feedback vs. Implicit Feedback")

        st.markdown("""
                In recommender systems, machine learning models are used to predict the
                **rating rᵤᵢ of a user u on an item i**. At inference time, we recommend to
                each user u the items i having highest predicted rating rᵤᵢ.
            """)

        st.markdown(""" 
                We therefore need to collect user feedback or rating, so that we can have a ground truth for 
                training and evaluating our models. An important distinction has to be made here 
                between **explicit feedback** and **implicit feedback**.
            """)
        st.image("./pictures/Feedback.jpg", caption="Explicit vs. implicit feedback for recommender systems.")
        st.markdown("""
                <a style='color: black;' href='{url_feedback}'><b>Explicit feedback</b></a> is a rating explicitly given by the user to express
                their satisfaction with an item. Examples are: number of stars on a
                scale from 1 to 5 given after buying a product, thumb up/down given
                after watching a video, etc. This feedback provides **detailed information**
                on how much a user liked an item, but it is **hard to collect** as most
                users typically don’t write reviews or give explicit ratings for each
                item they purchase.
            """, unsafe_allow_html=True)

        st.markdown("""
                <a style='color: black;' href='{url_feedback}'><b>Implicit feedback</b></a>, on the other hand, assume that user-item interactions
                are an indication of preferences. Examples are: purchases/browsing
                history of a user, list of songs played by a user, etc. This feedback is
                **extremely abundant**, but at the same time it is **less detailed** and **more
                noisy** (e.g. someone may buy a product as a present for someone else).
                However, this noise becomes negligible when compared to the sheer size
                of available data of this kind, and **most modern Recommender Systems tend
                to rely on implicit feedback.**
            """, unsafe_allow_html=True)
    elif x == 1:
        url_products = 'https://www.analyticsvidhya.com/blog/2022/03/a-comprehensive-guide-on-recommendation-engines-and-implementation/'
        st.markdown("### Content-Based Filtering")
        st.image("./pictures/Content_base_filtering.jpg")

        st.markdown(f"""
        In this type of recommendation system, relevant items are shown using the content of the previously searched 
        items by the users. Here content refers to the attribute/tag of the product that the user likes. 
        <a style='color: black;' href='{url_products}'>Products</a> are tagged using certain keywords, then the system 
        tries to understand what the user wants and recommends 
        different products based on that.

        ##### Advantage
        - Model doesn't need data of other users since recommendations are specific to a single user.
        - Easier to scale to a large number of users.
        - Captures specific interests of the user and recommends items that few other users are interested in.

        ##### Disadvantage
        - Requires hand-engineered feature representation of items, which requires domain knowledge.
        - Limited ability to expand on the user’s existing interests.""", unsafe_allow_html=True)

        st.markdown("### Collaborative Based Filtering")
        st.image("./pictures/Collaborative Filtering.jpg")

        st.markdown(f""" 
        Recommending new items to users based on the interest and preference of other similar users is 
        collaborative-based filtering. It leverages user interactions and historical performance to predict 
        future preferences.
        
        This approach not only addresses the limitations of content-based filtering but also leverages user interactions, 
        making it more robust. By focusing on the historical performance of users, this recommendation system can 
        predict future preferences with greater accuracy.
        
        **There are 2 types of collaborative filtering:**""", unsafe_allow_html=True)


        st.image("./pictures/User_Item_based Filtering.jpg")

        st.markdown(f"""
        ##### A. User-Based Collaborative Filtering
           - Ratings of the item are done using the ratings of neighboring users.
           - Based on the notion of users’ similarity.""")
        st.markdown("""Rating of the item is done using the rating of neighbouring users. In simple words, 
        It is based on the notion of users’ similarity.<br><br>
        Let see an example. On the left side, you can see a picture where 3 children named A, B, C, and 4 fruits i.e, 
        grapes, strawberry, watermelon, and orange respectively.<br><br>
        Based on the image let assume A purchased all 4 fruits, B purchased only strawberry and C purchased strawberry 
        as well as watermelon. Here A & C are similar kinds of users because of this C will be recommended Grapes 
        and Orange as shown in dotted line. """, unsafe_allow_html=True)
        st.markdown(f"""
        ##### B. Item-Based Collaborative Filtering
           - Ratings of the item are predicted using the user’s own rating on neighboring items.
           - Based on the notion of item similarity. """)

        st.markdown(f"""The rating of the item is predicted using the user’s own rating on neighbouring items. In simple 
        words, it is based on the notion of item similarity.
        Let us see with an example as told above about users and items. Here the only difference is that we see similar 
        items, not similar users like if you see grapes and watermelon you will realize that watermelon is purchased by 
        all of them but grapes are purchased by Children A & B. Hence Children C is being recommended grapes.<br><br>
        Now after understanding both of them you may be wondering which to use when. Here is the solution if No. of 
        items is greater than No. of users go with user-based collaborative filtering as it will reduce the computation 
        power and If No. of users is greater than No. of items go with item-based collaborative filtering. <br><br>
        For Example, Amazon has lots of items to sell but has billions of customers. Hence Amazon uses item-based 
        collaborative filtering because of less no. of products as compared to its customers. """, unsafe_allow_html=True)

        st.markdown("""
        ##### Advantage
        - Works well even with small data.
        - Helps users discover new interests in items.
        - No need for domain knowledge.

        ##### Disadvantage
        - Cannot handle new items (Cold Start Problem).
        - Side features don’t have much importance. """, unsafe_allow_html=True)
    else :
        url_grv = "https://www.grandviewresearch.com/industry-analysis/mens-wear-market"
        url_mc ="https://www.mckinsey.com/industries/retail/our-insights/state-of-fashion"
        url_pmfro = "https://link.springer.com/chapter/10.1007/978-3-031-27409-1_9"
        url_ct = "https://arxiv.org/abs/2306.03395"
        url_mfrs = "https://arxiv.org/abs/2202.02757"

        st.image("./pictures/Men Fashion Recommendation.jpg")
        st.markdown(
        f"""
        #### Men's Fashion Revolution: AI Tailors the Perfect Wardrobe
        The fashion industry thrives on a constant dance between staying current and expressing individuality. This can 
        be especially challenging for men, who often crave guidance in building a wardrobe that reflects their personality 
        while keeping pace with trends. A recent study by <a style='color: black;' href='{url_grv}'><b>Grand View Research</b></a>  revealed that the 
        global men's fashion market is expected to reach a staggering $97 billion by 2028. This significant growth 
        underscores the increasing interest in men's fashion, but also highlights the need for a more personalized 
        shopping experience.

        Just like their female counterparts, men have a keen eye for style and actively seek inspiration online. But 
        their online searches go beyond just finding desired items. A survey by <a style='color: black;' href='{url_mc}'><b>McKinsey & Company</b></a> 
        found that 72% of male online shoppers actively seek recommendations for complementary products during their 
        shopping journey. This creates a win-win situation: men discover new styles that enhance their look, while 
        businesses leverage recommendation systems to boost sales.
        
        #### AI Steps Up to the Plate
        """, unsafe_allow_html=True)

        st.image("./pictures/Men Fashion Recommendation_2.jpg")
        st.markdown(
        f"""
        Enter the exciting world of Men's Fashion Recommendations, powered by cutting-edge algorithms. This isn't 
        science fiction – it's the future of fashion retail. Frameworks like <a style='color: black;' href='{url_pmfro}'><b>PMFRO</b></a> (Personalized Men’s Fashion 
        Recommendation Using Dynamic Ontological Models)  utilize a combination of user preferences, strategic 
        knowledge, and machine learning to curate personalized recommendations.  This approach has yielded impressive 
        results, with PMFRO achieving a remarkable precision rate of 94.68%.

        But <a style='color: black;' href='{url_pmfro}'><b>PMFRO</b></a> is just one example. A recent survey titled <a style='color: black;' href='{url_ct}'><i>"Computational Technologies for Fashion Recommendation: </i></a>
        A Survey" explores the various cutting-edge approaches driving fashion recommendation systems. From advanced 
        machine learning to data mining and computer vision, these technologies are revolutionizing how men shop for clothes.

        Articles like <a style='color: black;' href='{url_mfrs}'><i>"Building an AI-Powered Outfit Recommendation System With Dataiku"</i></a>  provide practical insights 
        into the technical aspects of these systems. Understanding how AI tailors recommendations allows businesses to refine 
        their approach and deliver an even more seamless shopping experience.""", unsafe_allow_html=True)

        st.markdown("""
        #### Exploring the Algorithm Landscape

        This project delves into the world of recommendation algorithms. We'll compare and analyze different approaches, 
        from the innovative to the established, to determine the most effective solution for building a Men's Fashion 
        Recommendation model that caters to the specific needs of its users.
        """, unsafe_allow_html=True)






