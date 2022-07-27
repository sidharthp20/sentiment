### Sentiment Analysis - is a method for identifying expression
### in a piece of text

#Import TextBlob
from textblob import TextBlob

text ="Editing my review after two years of usage .. Got this fridge in 32000 after all discounts.. so no regrets now.. initially there were problems and best part is no one from amazon came to resolve it. Problems went away itself after changing some settings."

text1 ="This is a great Refrigerator with all required features in a budget price. It's frost free and compartments are really spacious. Delivery and installation was seamless and hassel free.Happy with the product so far."

obj = TextBlob(text)
obj1 = TextBlob(text1)

# return the sentiment of text,
# value between -1.0 to 1.0
# also the value between 0.0 to 1.0

sentiment = obj.sentiment.subjectivity
sentiments = obj1.sentiment.polarity
print (sentiment)
print(sentiments)