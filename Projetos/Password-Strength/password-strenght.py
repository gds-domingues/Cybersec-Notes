# Gabriel Domingues Silva
# gabriel.domingues.silva@usp.br
# github.com/gds-domingues

# Import Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import random
import pandas as pd


# Custom Tokenizer Function
def getTokens(inputString):
    # Tokenizes a string into individual characters
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens

# File Path and Data Reading
filepath = 'file_path' # Replace with actual file path
data = pd.read_csv(filepath, ',', error_bad_lines=False)

# Convert Data to NumPy Array and Shuffle
data = pd.DataFrame(data)
passwords = np.array(data)
random.shuffle(passwords) # Shuffling randomly for robustness

# Extract Labels and Passwords
y = [d[1] for d in passwords] # Labels
allpasswords = [d[0] for d in passwords] # Actual passwords

# Vectorize Passwords using TF-IDF
vectorizer = TfidfVectorizer(tokenizer=getTokens) # Vectorizing
X = vectorizer.fit_transform(allpasswords)

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Initialize and Train Logistic Regression Classifier
lgs = LogisticRegression(penalty='l2', multi_class='ovr') # Our logistic regression classifier
lgs.fit(X_train, y_train) # Training

# Evaluate Classifier on Test Data
print(lgs.score(X_test, y_test)) # Testing

# More Testing: Make Predictions on Example Passwords
X_predict = ['gdsdomingues','159357Asd%@','@ardnErtsx2g4','twitteristoxic','gggggggggg','pudim','heuheuheuheuheuheuhe','bolinha','mynameisgabriel','gabriel','123456','abc123']
X_predict = vectorizer.transform(X_predict)
y_Predict = lgs.predict(X_predict)
print(y_Predict)