library(syuzhet)
# text_df1 <- read.csv("text.csv", stringsAsFactors = FALSE)
text_df1 <- read.csv("comments.csv", stringsAsFactors = FALSE) # Extraction 2
# stringsAsFactors (logical) : should character vectors be converted to factors? Note that this is overridden by as.is and colClasses, both of which allow finer control.

review <- as.character(text_df1$Content)
# Get review content only
# Clean the data received

get_nrc_sentiment('happy') # +ve statements
get_nrc_sentiment('abuse') # -ve statements

s1 <- get_nrc_sentiment(review)
review_sentiment <- cbind(text_df1$Content, s1)

barplot(colSums(s1), col=rainbow(10), ylab='count', main='Az 60 Feedback')

