# Password-Strength

This code is an example of a simple password strength classifier using the TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer and logistic regression. It reads a file containing passwords and their corresponding labels, processes the data, and trains a logistic regression classifier to predict the strength of passwords.

Here's a breakdown of the code:

1. Data Collection Explanation:

The passwords utilized in our analysis were sourced from the 000webhost leak, publicly available on the internet. To assess the strength of these passwords, we employed a tool called PARS developed by Georgia Tech University. PARS integrates various commercial password meters. In the data collection process, I provided PARS with all the passwords, and in return, it generated new files for each commercial password strength meter. These files included the passwords along with an additional column indicating their strength based on the respective commercial password strength meters. Essentially, this approach allowed us to categorize passwords into different strength levels using established commercial criteria.

1. **Import Libraries:**
    - **`numpy`**: Numerical operations in Python.
    - **`random`**: Random number generation.
    - **`TfidfVectorizer`**: Used for vectorizing passwords using TF-IDF.
    - **`pandas`**: Data manipulation library.
    - **`train_test_split`**: Splitting data into training and testing sets.
    - **`LogisticRegression`**: Logistic regression classifier from scikit-learn.
2. **Custom Tokenizer Function:**

I'll leverage Tf-idf scores, but rather than considering the entire password as a unit, I'll treat each individual character as a distinct token. Additional metrics that I haven't incorporated could include factors such as password length, the frequency of special characters, the usage of digits, and similar attributes. Below is the custom tokenizer employed for this purpose.

```python
def getTokens(inputString):
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens
```

A custom tokenizer function that tokenizes a string into individual characters.

1. **Read Data:**
    
    ```python
    filepath = 'file_path'
    data = pd.read_csv(filepath, ',', error_bad_lines=False)
    ```
    
    Reads a CSV file containing passwords and labels. The passwords are expected to be in one column and the labels in another.
    
2. **Shuffle Data:**
    
    ```python
    passwords = np.array(data)
    random.shuffle(passwords)
    ```
    
    Converts the data to a NumPy array and shuffles it randomly for robustness.
    
3. **Prepare Data for Training:**
    
    ```python
    y = [d[1] for d in passwords]
    allpasswords = [d[0] for d in passwords]
    ```
    
    Separates labels (**`y`**) and passwords (**`allpasswords`**) from the shuffled data.
    
4. **Vectorize Passwords:**
    
    ```python
    vectorizer = TfidfVectorizer(tokenizer=getTokens)
    X = vectorizer.fit_transform(allpasswords)
    ```
    
    That concludes the process. To establish our machine learning-based password strength checker, we simply need to implement our machine learning algorithm. Let's proceed. I opted for logistic regression with multi-class classification to ensure swift algorithm execution.
    
    Uses TF-IDF vectorization to convert passwords into numerical vectors.
    
5. **Split Data into Training and Testing Sets:**
    
    ```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    ```
    
    Splits the data into training and testing sets.
    
6. **Initialize and Train Logistic Regression Classifier:**
    
    ```python
    lgs = LogisticRegression(penalty='l2', multi_class='ovr')
    lgs.fit(X_train, y_train)
    ```
    
    Initializes a logistic regression classifier and trains it on the training data.
    
    The achieved accuracy stands at 81%, a commendable result, especially considering the relatively modest amount of data used. This implies that 80% of the time, our algorithm categorizes passwords in alignment with the consensus of three prominent commercial password classifiers. Let's examine how this algorithm categorizes our passwords.
    
7. **Evaluate Classifier on Test Data:**
    
    ```python
    print(lgs.score(X_test, y_test))
    ```
    
    Prints the accuracy of the logistic regression classifier on the test set.
    
8. **Make Predictions:**
    

```python
X_predict = ['gdsdomingues', '159357Asd@', '@ardnErtsx2g4', ...]
X_predict = vectorizer.transform(X_predict)
y_Predict = lgs.predict(X_predict)
print(y_Predict)
```

Makes predictions on a set of example passwords and prints the predicted labels.

Several key points are worth highlighting. The algorithm acquired its knowledge from existing algorithms, but I enhanced its robustness by amalgamating the outcomes of multiple algorithms. It doesn't merely mimic a rule-based algorithm; rather, it replicates a combination of various password strength checking algorithms observed in practical use. It's important to note that this project was undertaken during my leisure time and is not an exhaustive endeavor. It represents an idea that I wanted to bring to fruition to observe the outcomes and share them with others. I firmly believe that there's potential for further expansion, leading to a more meaningful and comprehensive strength checker or classifier.
