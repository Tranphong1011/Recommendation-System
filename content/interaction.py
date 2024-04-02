import pandas as pd
import numpy as np
import pickle
import os
import sys
import re
import ast
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gensim import corpora, models, similarities
from underthesea import word_tokenize
# import streamlit_nested_layout
import locale

def format_vnd(amount):
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
    return locale.currency(amount, grouping=True)



# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Text processing
csv_path = os.path.join(parent_dir, 'materials', 'vietnamese-stopwords.txt')
with open(csv_path, 'r', encoding='utf-8') as file:
    stop_words = file.read()
stop_words = stop_words.split('\n')
remove_words = ['s','l','xl','xxl','kg', 'k','c']

# Product raw info
product_raw_path = os.path.join(parent_dir, 'materials', 'Products_ThoiTrangNam_raw.csv')
product_raw = pd.read_csv(product_raw_path)
def product_info(product_id):
    sub_category = product_raw.loc[product_raw.product_id==product_id, "sub_category"].values[0]
    link_info = product_raw.loc[product_raw.product_id==product_id, "link"].values[0]
    image_product = product_raw.loc[product_raw.product_id==product_id, "image"].values[0]
    price = product_raw.loc[product_raw.product_id==product_id,"price"].values[0]
    rating = product_raw.loc[product_raw.product_id==product_id,"rating"].values[0]
    description = product_raw.loc[product_raw.product_id==product_id,"description"].values[0]
    if pd.isnull(image_product):
        image_product = "No image available"
    if pd.isnull(description):
        description = "No description Found"
    return [sub_category, link_info, image_product, price, rating, description]


def rating_bar(rating):
    if rating > 0:
        rating_bar = f'''
        <div style="display: flex; align-items: center;">
            <div style="width: {rating * 20}%; background-color: #ffd700; height: 20px; border-radius: 5px; position: relative;">
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: black;">{rating}</div>
            </div>
            <div style="width: {(5 - rating) * 20}%; background-color: #d3d3d3; height: 20px; border-radius: 5px;"></div>
        </div>
        '''
        return rating_bar
    else:
        return "Rating not found"


def text_processing(text):
    cleaned_text = re.sub(r'\(.*?\)|\[.*?\]', '', text)
    cleaned_text = re.sub(r'\b\w*\d\w*\b', '', cleaned_text)
    cleaned_text = word_tokenize(cleaned_text, format="text")
    cleaned_text = [word for word in cleaned_text.split()]
    cleaned_text = [re.sub('[0-9]+','', word) for word in cleaned_text]
    cleaned_text = [word.lower() for word in cleaned_text if not word in ['', ' ', ',', '.', '...', '-',':', ';', '?', '%', '_%' , '(', ')', '+', '/', 'g', 'ml']]
    cleaned_text = [word for word in cleaned_text if not word in stop_words]
    cleaned_text = [word for word in cleaned_text if not word in remove_words]
    cleaned_text = [word for word in cleaned_text if re.match(r'^[\wàáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ_]+$', word)]
    cleaned_text = [re.sub(r'\b_+|_+\b', '', word) for word in cleaned_text ]
    return cleaned_text



# # Product name processing
# product_rating_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam_rating.csv')
# product_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam.csv')
# product = pd.read_csv(product_path,index_col=0, converters={'products_gem_re': ast.literal_eval})
# product_rating = pd.read_csv(product_rating_path)
# product_select = product[["product_id", "products_gem_re"]]
# product_rating_select = product_rating[["product_id", "user_id"]]
#
# combine_data = pd.merge(product_select, product_rating_select, on='product_id')
#
# def product_name_processing(user_id):
#
#     group_data = combine_data.groupby('user_id')['products_gem_re'].apply(list).reset_index()
#     product_info_list = group_data.loc[group_data.user_id == user_id, "products_gem_re"].values[0]
#     product_info_text = ' '.join([' '.join(sublist) for sublist in product_info_list if isinstance(sublist, list)])
#     return product_info_text
#
# # Plot wordcloud
# def wordcloud(user_id):
#     product_info  = product_name_processing(user_id)
#     nWords = 100
#     # Generate the word cloud with improved clarity
#     wordcloud = WordCloud(width=800, height=400, background_color='white',max_words=nWords).generate(product_info)
#     fig, ax = plt.subplots(figsize=(10, 5))
#     ax.imshow(wordcloud, interpolation='bilinear')
#     ax.axis('off')  # Remove axis
#     ax.set_title(f'Word Cloud of product of user {user_id}', fontsize=20)
#     st.pyplot(fig)
#
#
# # Collaborative Filtering
# pkl_file_path = os.path.join(parent_dir, 'models', 'algorithm_BSOnly.pkl')
# data_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam_rating.csv')
# with open(pkl_file_path, 'rb') as file:
#     algorithm_svd = pickle.load(file)
#
# data = pd.read_csv(data_path)
# def get_recommend(user_id, rating_prefer):
#     user_list = data.user_id.drop_duplicates().values
#     if ~np.isin(user_id, user_list):
#         inform = "Unsuccessfully!"
#         return ["No users found!", "Can not recommend!", inform]
#     else:
#         inform = "Successfully!"
#         df_score = data[["product_id"]]
#         df_score['EstimateScore'] = df_score['product_id'].apply(lambda x: algorithm_svd["algo"].predict(user_id, x).est) # est: get EstimateScore
#         df_score = df_score.sort_values(by=['EstimateScore'], ascending=False)
#         df_score_top10 = df_score.drop_duplicates().head(10)
#         df_score_top5 = df_score.drop_duplicates().head()
#         if rating_prefer == 0:
#             product_id_list = data.loc[df_score_top5.index].head().product_id.tolist()
#         else:
#             product_id_list = data.loc[df_score_top10.index].sort_values(by=['rating'], ascending=False).head().product_id.tolist()
#         return ["User found!", product_id_list, inform]
#
#
# # Content_based Filtering
# csv_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam.csv')
# product_name = pd.read_csv(csv_path,index_col=0, converters={'products_gem_re': ast.literal_eval})
# products_gem_re = product_name.products_gem_re
# dictionary = corpora.Dictionary(products_gem_re)
# feature_cnt = len(dictionary.token2id)
# corpus = [dictionary.doc2bow(text) for text in products_gem_re]
# tfidf = models.TfidfModel(corpus) # Use TF-IDF Model to process corpus
#
# index = similarities.SparseMatrixSimilarity(tfidf[corpus],
#                                             num_features = feature_cnt)
# data_result = pd.DataFrame(index[tfidf[corpus]])
# product_name["products_gem_re"] = product_name["products_gem_re"].apply(lambda x: ' '.join(x))
#
# def get_top_recommend_from_item(product_id):
#     product_list = product_raw.product_id.values
#     if ~np.isin(product_id, product_list):
#         inform = "Unsuccessfully!"
#         return ["No items found!", "Can not recommend!", inform]
#     else:
#         inform = "Successfully!"
#         query = product_raw[product_raw['product_id'] == product_id]
#         item_searching = query.product_name.values[0]
#         processed_text = text_processing(item_searching)
#         kw_vector = dictionary.doc2bow(processed_text)
#         sim_indices_desc = np.argsort(index[tfidf[kw_vector]])[::-1]
#         get_item_range = product_name.iloc[sim_indices_desc[:5]].product_id.values
#         product_id_list = get_item_range.tolist()
#         return [item_searching, product_id_list, inform]
#
#
# def get_top_recommend_from_text(text):
#     processed_text = text_processing(text)
#     kw_vector = dictionary.doc2bow(processed_text)
#     sim_indices_desc = np.argsort(index[tfidf[kw_vector]])[::-1]
#     get_item_range = product_name.iloc[sim_indices_desc[:5]].product_id.values
#     product_id_list = get_item_range.tolist()
#     inform = "Successfully"
#     return [inform,product_id_list]
#
#
# def display_list(product_id_list):
#     for item_id in product_id_list:
#         item_name = product_raw.loc[product_raw['product_id'] == item_id, "product_name"].values[0]
#         sub_category, link_info, link_image, price, rating, description = product_info(item_id)
#
#         with st.expander(
#                 f"**{item_name}**"
#         ):
#             outer_cols = st.columns([1, 1])
#             with outer_cols[0]:
#                 if link_image == "No image available":
#                     st.image(f'./pictures/no_image_found.jpg')
#                 else:
#                     st.image(f'{link_image}')
#                 st.markdown(f"**Subcategory**: {sub_category}")
#                 st.markdown(f"**Product info**: {link_info}")
#                 st.markdown(f"**Price**: {format_vnd(price)}")
#                 inner_cols = st.columns([1,5])
#                 with inner_cols[0]:
#                     st.markdown(f'**Rating**')
#                 with inner_cols[1]:
#                     st.markdown(rating_bar(rating), unsafe_allow_html=True)
#             with outer_cols[1]:
#                 with st.expander('**Show description**'):
#                     st.markdown(f"{description}", unsafe_allow_html=True)
def interaction(x):
    print(f"This function does something but doesn't return anything")
    # # Collaborative filtering
    # if x == 0:
    #     st.markdown(
    #         f"""
    #         #### Recommendation with User ID
    #         """
    #     )
    #     user_id = st.number_input("Enter User ID: ", 0, value=None, placeholder="Example: 10, 102220, ...")
    #
    #     options_dic = {"Yes" : 1, "No": 0}
    #     # Select box
    #     rating_select = st.selectbox("Do you want recommendation with rating? ", list(options_dic.keys()))
    #     # Button
    #     user, product_id_list, inform_cf = get_recommend(user_id, options_dic[rating_select])
    #     if st.button("Submit"):
    #         if inform_cf == "Successfully!":
    #             st.success(f"{inform_cf}")
    #             st.write(f"**{user}**")
    #             st.write(f"**Here are similar products**: ")
    #             display_list(product_id_list)
    #             wordcloud(user_id)
    #         else:
    #             st.warning(f"{inform_cf}")
    #             st.write(f"{user}")
    #             st.write(f"{product_id_list}")
    #
    # # Content_based filtering
    # else:
    #     options = ["Recommendation with Product ID", "Recommendation with Product Name text input"]
    #     selected_option = st.selectbox("Select an option",options )
    #     if selected_option == options[0]:
    #
    #         st.markdown(
    #             f"""
    #             #### Recommendation with Product ID
    #             """
    #         )
    #         product_id = st.number_input("Enter Product ID: ",0, value=None, placeholder="Example: 175063, 194, ...")
    #
    #         item_searching,  product_id_list, inform_cbf = get_top_recommend_from_item(product_id)
    #         # Button
    #         if st.button("Submit ID"):
    #
    #             if inform_cbf == "Successfully!":
    #                 st.success(f"{inform_cbf}")
    #                 st.write(f"**The product with ID {product_id}** is: {item_searching}")
    #                 st.write(f"**Here are similar products:** ")
    #                 display_list(product_id_list)
    #
    #             else:
    #                 st.warning(f"{inform_cbf}")
    #                 st.write(f"**{item_searching}**")
    #                 st.write(f"**{product_id_list}**")
    #     else:
    #         st.markdown(
    #             f"""
    #             #### Recommendation with Product Name text input
    #             """
    #         )
    #         product_search = st.text_input("Enter Product name: ", value="", placeholder="Áo thun ba lỗ nam, ....")
    #         inform_cbf_2, product_id_list = get_top_recommend_from_text(product_search)
    #         # Button
    #         if st.button("Submit name"):
    #
    #             st.success(f"{inform_cbf_2}")
    #             st.write(f"**Here are similar products:** ")
    #             display_list(product_id_list)



