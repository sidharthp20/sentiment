### Sentiment Analysis - is a method for identifying expression
### in a piece of text

#Import TextBlob
from textblob import TextBlob

text ="Python is a great tool for ml"
obj = TextBlob(text)


# return the sentiment of text,
# value between -1.0 to 1.0

sentiment = obj.sentiment.polarity

print (sentiment)
