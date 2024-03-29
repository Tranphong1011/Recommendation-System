import re
from underthesea import word_tokenize, pos_tag, sent_tokenize
import os
import sys
import ast
import pandas as pd


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'materials', 'vietnamese-stopwords.txt')

with open(csv_path, 'r', encoding='utf-8') as file:
    stop_words = file.read()

stop_words = stop_words.split('\n')
remove_words = ['s','l','xl','xxl','kg', 'k','c']

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

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now import and read the .pkl file
product_rating_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam_rating.csv')
product_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam.csv')

product = pd.read_csv(product_path,index_col=0, converters={'products_gem_re': ast.literal_eval})
product_rating = pd.read_csv(product_rating_path)

product_select = product[["product_id", "products_gem_re"]]
product_rating_select = product_rating[["product_id", "user_id"]]

def product_name_processing(user_id):
    combine_data = pd.merge(product_select,product_rating_select,on='product_id')
    group_data = combine_data.groupby('user_id')['products_gem_re'].apply(list).reset_index()
    product_info_list = group_data.loc[group_data.user_id == user_id, "products_gem_re"].values[0]
    product_info_total = []
    for product_info_each in product_info_list:
        product_info_total.append(' '.join(product_info_each))
    product_info_text = ' '.join(product_info_total)
    return product_info_text

