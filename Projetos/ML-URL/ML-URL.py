# Gabriel Domingues Silva
# gabriel.domingues.silva@usp.br
# github.com/gds-domingues

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import random

def getTokens(input):
    # Tokenize a URL by splitting on '/', '-', and '.' characters
    tokensBySlash = str(input.encode('utf-8')).split('/')
    allTokens = []

    # Further split tokens by '-'
    for i in tokensBySlash:
        tokens = str(i).split('-')
        tokensByDot = []

        # Further split tokens by '.'
        for j in range(0, len(tokens)):
            tempTokens = str(tokens[j]).split('.')
            tokensByDot = tokensByDot + tempTokens

        allTokens = allTokens + tokens + tokensByDot

    # Remove redundant tokens
    allTokens = list(set(allTokens))

    # Remove 'com' since it occurs frequently and may not provide useful information
    if 'com' in allTokens:
        allTokens.remove('com')

    return allTokens

# Path to the file containing all URLs
allurls = 'C:\\\\Users\\\\Gabriel D\\\\Desktop\\\\Url Classification Project\\\\Data to Use\\\\allurls.txt'

# Read data from the CSV file
allurlscsv = pd.read_csv(allurls, ',', error_bad_lines=False)
allurlsdata = pd.DataFrame(allurlscsv)

# Convert data to a NumPy array and shuffle
allurlsdata = np.array(allurlsdata)
random.shuffle(allurlsdata)

# Extract features (X) and labels (y)
corpus = [d[0] for d in allurlsdata]
y = allurlsdata['label']  # Assuming the column name is 'label'

# Vectorize URLs using TF-IDF
vectorizer = TfidfVectorizer(tokenizer=getTokens)
X = vectorizer.fit_transform(corpus)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Logistic Regression classifier
lgs = LogisticRegression()
lgs.fit(X_train, y_train)

# Print the accuracy score on the test set
print(lgs.score(X_test, y_test))  # Accuracy comes out to be 98%

# Test the classifier on new URLs
X_predict = ['wikipedia.com', 'google.com/search=gdsdomingues', 'twitter.com', 'www.radsport-voggel.de/wp-admin/includes/log.exe', 'ahrenhei.without-transfer.ru/nethost.exe', 'www.itidea.it/centroesteticosothys/img/_notes/gum.exe']
X_predict = vectorizer.transform(X_predict)
y_Predict = lgs.predict(X_predict)

# Print the predicted values
print(y_Predict)
