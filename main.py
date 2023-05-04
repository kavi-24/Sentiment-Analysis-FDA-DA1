# Sentiment Analysis
# Sentiment Analysis is the process of computationally determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.
# Sentiment Analysis is widely applied to voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine.
# Sentiment Analysis is a special case of text classification where users’ opinions or sentiments regarding a product are classified into predefined categories such as positive, negative, neutral etc. Computations involved in Sentiment Analysis rely primarily on Natural Language Processing.
# Sentiment Analysis is a process of extracting opinions or attitudes of the users towards a product from the text documents.

from comment_scraper import scrape_comments
from r_services import r_service
from csvWriter import csv_writer

def main():
    data, conn = scrape_comments()
    file = "comments.csv" if conn else "default.csv"
    if conn:
        csv_writer(data)
    r_service(file)

if __name__ == "__main__":
    main()
