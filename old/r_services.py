import rpy2.robjects as robjects
import pandas as pd
import matplotlib.pyplot as plt
from rpy2.robjects import pandas2ri
import warnings
warnings.filterwarnings("ignore")

from r_package_installer import importr_tryhard

def r_service(file: str) -> None:
    # print("R...")
    pandas2ri.activate()

    syuzhet = importr_tryhard("syuzhet")

    text_df1 = pd.read_csv(file, encoding='utf-8')
    text_df1['Content'] = text_df1['Content'].astype(str).str.replace('[^\w\s]', '').str.replace(
        '\d+', '').str.replace('\n', '').str.replace('\t', '').str.replace('\r', '').str.replace(' +', ' ').str.lower()
    # print("Text: ", text_df1)

    review = text_df1['Content'].tolist()
    review = robjects.vectors.StrVector(review)
    review = [i for i in review]
    review = robjects.vectors.StrVector(review)

    # print(review2)  # raises UnicodeEncodeError, don't print :)
    s1 = syuzhet.get_nrc_sentiment(review)
    # Transpose the dataframe s1
    s1 = pd.DataFrame(s1).T
    # print(s1)
    
    review_sentiment = pd.concat([text_df1['Content'], pd.DataFrame(s1)], axis=1)
    sentiments = "anger anticipation disgust fear joy sadness \
        surprise trust negative positive".split()[::-1]
    review_sentiment.columns = ['Content'] + sentiments
    review_sentiment['sentiment'] = review_sentiment[sentiments].idxmax(axis=1)
    
    print("Reviews + Sentiments")
    print(review_sentiment)
    print(review_sentiment['sentiment'].value_counts())

    review_sentiment['sentiment'].value_counts().plot(kind='bar')
    plt.title('Youtube Comments - Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    # add colours

    plt.show()

    # Other types of plots, provided by GitHub Copilot
    # review_sentiment['sentiment'].value_counts().plot(kind='pie')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='line')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='area')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='box')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='hist')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='kde')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(kind='density')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(
    #     kind='pie', x='sentiment', y='count')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(
    #     kind='barh', x='sentiment', y='count')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()

    # review_sentiment['sentiment'].value_counts().plot(
    #     kind='bar', x='sentiment', y='count')
    # plt.title('Sentiment Analysis')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Count')
    # plt.tight_layout()
    # plt.show()
