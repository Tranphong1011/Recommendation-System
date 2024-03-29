from gensim import corpora, models, similarities
import os
import pandas as pd
import numpy as np
import ast
import text_processing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

csv_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam.csv')


product_name = pd.read_csv(csv_path,index_col=0, converters={'products_gem_re': ast.literal_eval})
products_gem_re = product_name.products_gem_re
dictionary = corpora.Dictionary(products_gem_re)
feature_cnt = len(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in products_gem_re]

# Use TF-IDF Model to process corpus
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus],
                                            num_features = feature_cnt)

data_result = pd.DataFrame(index[tfidf[corpus]])

# Cosine similarity model
product_name["products_gem_re"] = product_name["products_gem_re"].apply(lambda x: ' '.join(x))
tf = TfidfVectorizer(analyzer='word', stop_words=text_processing.stop_words)
tfidf_matrix = tf.fit_transform(product_name.products_gem_re)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
data_result_cosine_similarities = pd.DataFrame(cosine_similarities)


def get_top_recommend_from_item(product_id, model_id):
    product_list = product_name.product_id.values
    if ~np.isin(product_id, product_list):
        return "Không có thông tin product!"
    query = product_name[product_name['product_id'] == product_id]
    item_searching = query.product_name.values[0]
    index = query.index[0]
    if model_id == 1:
        get_index_range = data_result[index].sort_values(ascending=False)[1:6].index
    elif model_id == 2:
        get_index_range = data_result_cosine_similarities[index].sort_values(ascending=False)[1:6].index
    else:
        raise ValueError("Invalid model_id. Must be 1 or 2.")
    get_item_range = product_name.iloc[get_index_range].product_name.values
    item_range_list = get_item_range.tolist()
    return item_searching, item_range_list


def get_top_recommend_from_text(text,  model_id):
    processed_text = text_processing.text_processing(text)

    if model_id == 1:
        kw_vector = dictionary.doc2bow(processed_text)
        sim_indices_desc = np.argsort(index[tfidf[kw_vector]])[::-1]
        get_item_range = product_name.iloc[sim_indices_desc[:5]].product_name.values

    elif model_id == 2:
        processed_text_join = ' '.join(processed_text)
        # Convert the new content to a numerical representation
        new_content_vector = tf.transform([processed_text_join])
        # Compute cosine similarity between the new content and existing documents
        cosine_sim_with_new = cosine_similarity(new_content_vector, tfidf_matrix)
        # Get indices of documents sorted by cosine similarity
        sorted_indices = cosine_sim_with_new.argsort()[0][::-1]
        get_item_range = product_name.iloc[sorted_indices[:5]].product_name.values
    else:
        raise ValueError("Invalid model_id. Must be 1 or 2.")
    item_range_list = get_item_range.tolist()
    return item_range_list
