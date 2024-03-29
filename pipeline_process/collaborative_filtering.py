import pandas as pd
import numpy as np
import pickle
import os
import sys
import warnings
warnings.filterwarnings("ignore")

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now import and read the .pkl file
pkl_file_path = os.path.join(parent_dir, 'surprise_results', 'algorithm_BSOnly.pkl')
data_path = os.path.join(parent_dir, 'processed_data', 'Products_ThoiTrangNam_rating.csv')
with open(pkl_file_path, 'rb') as file:
    algorithm_svd = pickle.load(file)

data = pd.read_csv(data_path)
def get_recommend(user_id, rating_prefer):
    user_list = data.user_id.drop_duplicates().values
    if ~np.isin(user_id, user_list):
        return "Không có thông tin user!"
    df_score = data[["product_id"]]
    df_score['EstimateScore'] = df_score['product_id'].apply(lambda x: algorithm_svd["algo"].predict(user_id, x).est) # est: get EstimateScore
    df_score = df_score.sort_values(by=['EstimateScore'], ascending=False)
    df_score_top10 = df_score.drop_duplicates().head(10)
    df_score_top5 = df_score.drop_duplicates().head()
    if rating_prefer == 0:
        get_item_list = data.loc[df_score_top5.index].head().product_name.tolist()
    elif rating_prefer == 1:
        get_item_list = data.loc[df_score_top10.index].sort_values(by=['rating'], ascending=False).head().product_name.tolist()
    else:
        raise ValueError("Invalid model_id. Must be 1 or 2.")
    return get_item_list
