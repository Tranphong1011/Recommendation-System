import pandas as pd
import streamlit as st
import io

products_data  = pd.read_csv("./materials/Products_ThoiTrangNam_raw.csv")
ratings_data  = pd.read_csv("./materials/Products_ThoiTrangNam_rating_raw.csv",sep='\t')


url_menfashion = "https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567"

def data(x):
    if x == 0:
        st.markdown(
            f"""
            The data was extracted from a renowned e-commerce platform in Vietnam, namely Shopee.

            The image below represents the Shopee platform, focusing on the category: <a style='color: black;' href='{url_menfashion}'><b>Thời trang nam</b></a> (Men's Fashion), which will 
            be further analyzed and processed in the subsequent chapter.
            """, unsafe_allow_html=True)
        st.image("./pictures/shopee_fashion.jpg")
        st.markdown(
            """
            The provided data consists of the following files:

            **Products_ThoiTrangNam_raw.csv**: This file contains information about products, such as their product_id, product_name, price, description and so on.
            """
        )
        st.dataframe(products_data.head(3))

        st.markdown(
            """
            **Products_ThoiTrangNam_rating_raw.csv**: This file contains ratings for the products in the Products_ThoiTrangNam_raw.csv file.
            """
        )
        st.dataframe(ratings_data.head(3))
        st.markdown(
            """
            All raw data should be properly **processed and featured** through a pipeline in order to fit into any of the models or
            algorithms from package. 
            """
        )
        st.image("./pictures/data_preparation.jpg")
        st.markdown(
            """
            - The data can be used to build a **recommendation system** for men's fashion products. The recommendation system can 
            be used to recommend products to users based on their product_name, ratings and description.
            
            - The data can also be used to **analyze the trends in men's fashion**. The analysis can be used to identify the most 
            popular products and categories, as well as the most popular brands.

            - The data can also be used to **improve the customer experience**. The analysis can be used to identify the products 
            that are most likely to be returned, and the products that are most likely to be rated highly.
            """
        )


    elif x == 1:

        # Sidebar options
        page_options = ["Products Data", "Ratings Data"]
        selected_page = st.sidebar.selectbox("Select Database", page_options)

        # Page content based on selected option
        if selected_page == "Products Data":
            st.dataframe(products_data.head(5))

            buffer = io.StringIO()
            products_data.info(buf=buffer)
            st.text(buffer.getvalue())

            st.markdown(
                """
                **Select important features to process**: product_id, product_name, sub_category, price, rating and description
                """
            )
            products_data_selected = products_data[
                ["product_id", "product_name", "sub_category", "price", "rating", "description"]]

            st.dataframe(products_data_selected.head(5))

            buffer = io.StringIO()
            products_data_selected.info(buf=buffer)
            st.text(buffer.getvalue())


            st.markdown(""" 
            **Handling missing data**: Only feature "description" has null value, but it's not worth addressing these 
            missing values as it only provides additional insights into the data
            """)
            st.markdown(""" 
            **Handling duplicated data**: None of the features has duplicated values
            """)

            st.markdown(""" 
            **Handling feature "product_name"**: Though the name of each product has already been properly defined by the sellers, it has
            unexpected characters and emoji, also some kinds of mistaken words and teen code. We have to deal with it
            """)
            st.image("./pictures/process_name.jpg")

            st.markdown(
            f"""
                - Remove words within parentheses.
                - Remove words containing numbers.
                - Tokenize the text using word_tokenize.
                - Perform part-of-speech tagging (POS tagging).
                - Split the sentences into words.
                - Remove Vietnamese stopwords.
                - Remove size indicators.
                - Remove non-alphanumeric characters.
                - Remove underscores.
            """
            , unsafe_allow_html=True)

            st.markdown(""" 
            **Handling feature "desciption"**: Although the description field may not contain useful information for 
            model training purposes, its features such as original production can be helpful for data exploration.
            """)
            st.image("./pictures/process_description.jpg")


        else:
            st.dataframe(ratings_data.head(5))

            buffer = io.StringIO()
            ratings_data.info(buf=buffer)
            st.text(buffer.getvalue())

            st.markdown(""" 
            **Handling missing data**: No missing data
            """)
            st.markdown(""" 
            **Handling duplicated data**: 24667 duplicated data => has to be removed
            """)

            st.markdown(""" 
            **Combine data**: We combine data by join 2 databases products and ratings for further analysis
            """)

            st.image("./pictures/combine_data.jpg")

    else:
        # Sidebar options
        page_options = ["Products Data", "Ratings Data"]
        selected_page = st.sidebar.selectbox("Select Database", page_options)

        st.write("""
        <style>
        .center-element {
            text-align: center;
            font-size: 1.5em;
            margin-top: 20px; 
            margin-bottom: 20px; 
            font-weight: bold; 
        }
        </style>
        """, unsafe_allow_html=True)


        # Page content based on selected option
        if selected_page == "Products Data":
            st.markdown('<div class="center-element">Feature: product_name</div>', unsafe_allow_html=True)
            st.image("./pictures/frequent_product.jpg")
            st.image("./pictures/distribution_item_count.jpg")

            st.markdown(
                f"""
                
                Top items with the **highest purchase quantities** from the provided list of items in the dataset, including _"Áo dài cách tân nam"_ (Modernized Traditional Vietnamese Long Shirt for Men), _"Áo Sơ Mi Dài Tay Thời Trang Dành Cho Nam"_ (Long-Sleeved Fashion Shirt for Men), _"HOT MIKASA Áo Thun Tay Ngắn Cosplay Nhân Vật Anime Attack On Titan"_ (HOT MIKASA Short-Sleeved Cosplay T-shirt of Anime Character Attack On Titan), etc.

                The **majority** of items are purchased **only once** (accounting for **approximately 96.64%**). 
                
                => **Conclusion**: The purchasing behavior of customers tends towards **one-time purchases**, especially for clothing items.
                """
            )

            st.markdown('<div class="center-element">Feature: sub_category</div>', unsafe_allow_html=True)
            st.image("./pictures/count_each_subcate.jpg")
            st.markdown(
                f"""
                The bar chart shows that items belonging to the _Trang Phục Truyền Thống, Bồ Độ, Vớ/Tất,_ etc., are purchased in large quantities (nearly **5000 items**). 
                
                On the other hand, items from categories such as  _Áo Khóa, Quần Short, Jeans_, and various types of _Vest, Blazer_ are purchased in smaller quantities (only about **1500 items**).
                """
            )

            st.image("./pictures/price_distribution.jpg")
            st.markdown(
                f"""
                The chart indicates that price distribution is concentrated around the median, with **prices decreasing as they get higher**. 
                
                """
            )
            st.image("./pictures/price_distribution_subcate.jpg")
            st.markdown(
                f"""
                From the boxplot chart, it is evident that the **top items with highest prices** belong to sub-categories such as _Áo Vest_ and _Blazer_, _Trang Phục Truyền Thống_ (Traditional Clothing), _Đồ Hóa Trang_ (Cosmetics), and _Đồ Ngủ_ (Sleepwear). This observation aligns with the actual market trends for clothing.

                On the other hand, sub-categories like _Đồ Lót_ (Underwear) and _Vớ/Tất_ (Socks/Stockings) consistently appear in the list of categories with the lowest-priced items. 📊💰

                Please note that this interpretation is based on the boxplot analysis and may not account for all variations in the data.
                """
            )
            st.image("./pictures/rating_distribution.jpg")
            st.markdown(
                f"""
                The chart reveals an **unusual number of zero ratings**, suggesting that either customers are reluctant to rate products, or a significant proportion of items remain unrated. This observation aligns with reality, as customer ratings and reviews are often optional and may not provide immediate benefits to the reviewers. 
                
                Additionally, when product quality falls short of expectations, some items receive no ratings, resulting in a null value (**rating = 0**).

                However, the relatively high number of **5-star ratings** indicates that a substantial group of customers appreciates the products they purchase, actively engaging in leaving comments and positive ratings. 🌟🛒
                """
            )

            st.markdown('<div class="center-element">Feature: rating</div>', unsafe_allow_html=True)

            st.image("./pictures/Rating Distribution for items buy more than one.jpg")
            st.image("./pictures/Rating Distribution for items buy once.jpg")
            st.markdown(
                f"""
                Although **most items** are purchased in **quantities of one**, customers often leave **high ratings** for these **single-purchase items**. However, even with these positive ratings, there is still a **relatively large number of zero ratings**.

                For items purchased **multiple times**, customers pay more attention to them, resulting in **higher expectations** regarding quality. 
                
                Consequently, a significant proportion of these items receive zero ratings. This outcome may be due to heightened expectations, leading to disappointment if the product does not meet those expectations.
                """
            )
            st.image("./pictures/rating_accross_subcate.jpg")
            st.markdown(
                f"""
                The groups of items such as _Cà Vạt_ (Ties), _Trang Phục Truyền Thống_ (Traditional Clothing), _Đồ Hóa Trang_ (Cosmetics), and _Đồ Ngủ_ (Sleepwear) receive ratings **below 3**. This indicates a genuine level of **dissatisfaction** among customers regarding these specific product categories. Interestingly, these items belong to the top group of high-value products, as evident from the price chart. 
                
                Consequently, customers’ expectations regarding quality are also higher for these items compared to others, leading to consistently low ratings.

                Conversely, **items with lower values** tend to receive higher ratings. This phenomenon suggests that customers may be more forgiving when it comes to lower-priced items. 🌟💔                """
            )
            st.image("./pictures/price_vs_rating.jpg")
            url_pv = "https://priceva.com/blog/high-low-pricing"
            url_i = "https://www.intelligencenode.com/blog/use-price-quality-matrix-optimize-product-pricing/"
            st.markdown(
                f"""
                Items with **high prices** often receive very **low ratings**, whereas items with **moderate and low prices** tend to receive **higher ratings**. 🌟💰

                This phenomenon can be attributed to several factors:
                
                1. High-Low Pricing Strategy:              
                    - High-priced items are initially introduced at a premium price point. Later, they are strategically discounted during clearance sales or promotions.                   
                    - The allure of lower prices following a period of consistently high prices creates excitement among consumers, leading to increased sales.                   
                    - <a style='color: black;' href='{url_pv}'>However, this dynamic pricing strategy can sometimes affect perceived product quality.</a>

                2. Price-Quality Perception:               
                    - Customers often associate higher prices with better quality. When high-priced items receive low ratings, it can lead to doubts about their quality.                   
                    - <a style='color: black;' href='{url_i}'>Conversely, lower-priced items may be perceived as offering good value for the money, leading to more forgiving ratings.</a>
                """
            , unsafe_allow_html=True)

            st.markdown('<div class="center-element">Feature: description - country of origin</div>', unsafe_allow_html=True)
            st.image("./pictures/production_origin.jpg")
            st.markdown('More than **60%** of the listed items are not specified in terms of origin or source. 🌐🔍')
            st.image("./pictures/production_origin_country.jpg")
            st.markdown('Vietnam holds a **significant position** in the list of countries producing men’s fashion products, followed by China and Indonesia 🇻🇳👔🌏')

            st.image("./pictures/wc_prd_name.jpg")
            st.markdown('From the list of product names, it’s evident that items containing phrases like “áo” (shirt), “sơ_mi” (dress shirt), or “áo thun” (T-shirt) dominate. 👕👚')
        else:
            st.image("./pictures/rating_distribution_2.jpg")
            st.markdown('Based on the bar chart, users rate men’s fashion products **quite positively**. 🌟👔👍')

            st.image("./pictures/top_most_frequent_item.jpg")
            st.markdown(
                f"""
                Among the available products, the **most frequently purchased items** include:

                1. "Áo chống nắng thông hơi nam phiên bán cải tiến mới nhất"
                2. "Áo khoác Bomber dù Unisex Ulzzang "  
                3. "Áo khoác gió nam 2 lớp chống nước 2021"
                
                These products belong to the popular category and have garnered significant sales from customers. 🛒👕🧥
                """
            )
            st.image("./pictures/distribution_item_count_2.jpg")
            st.markdown('The majority of items are **purchased only once** (accounting for approximately **88.9%**). This observation suggests that customers tend to buy clothing items with a one-time purchase behavior. 🛒👕')









