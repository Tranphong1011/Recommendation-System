from wordcloud import WordCloud
import matplotlib.pyplot as plt

import text_processing

def wordcloud(user_id):
    product_info  = text_processing.product_name_processing(user_id)
    nWords = 100

    # Generate the word cloud with improved clarity
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=nWords)
    wordcloud.generate(product_info)

    # Plot the word cloud
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud of product of user {user_id}', fontsize=20)
    plt.axis('off')
    plt.show()