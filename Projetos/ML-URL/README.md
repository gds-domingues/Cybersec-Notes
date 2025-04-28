# Machine Learning for Malicious URL

This code is for a simple URL classification model using a logistic regression classifier. It involves the following steps:

**Gathering Data Explanation:**

The initial step involved data collection. After exploring various websites that hosted malicious links, I developed a small crawler to systematically gather a substantial number of malicious links from different online sources. Simultaneously, I sought to acquire a set of clean URLs for comparison. Fortunately, I came across an existing dataset, eliminating the need for additional crawling. Although specific sources aren't mentioned here, the dataset will be provided at the end of this post for reference.

In total, I amassed approximately 400,000 URLs, with around 80,000 identified as malicious and the rest deemed clean. This compilation formed the basis of our dataset, paving the way for the subsequent stages.

**Analysis Approach:**

For the analysis, I opted for Logistic Regression due to its efficiency. The first phase involved tokenizing the URLs. Given the unique structure of URLs compared to conventional document text, I crafted a custom tokenizer function tailored to their characteristics. Consequently, some of the extracted tokens included terms like 'virus', 'exe', 'php', 'wp', 'dat', and so forth. This process laid the groundwork for further analysis.

```python
def getTokens(input):
	tokensBySlash = str(input.encode('utf-8')).split('/')	#get tokens after splitting by slash
	allTokens = []
	for i in tokensBySlash:
		tokens = str(i).split('-')	#get tokens after splitting by dash
		tokensByDot = []
		for j in range(0,len(tokens)):
			tempTokens = str(tokens[j]).split('.')	#get tokens after splitting by dot
			tokensByDot = tokensByDot + tempTokens
		allTokens = allTokens + tokens + tokensByDot
	allTokens = list(set(allTokens))	#remove redundant tokens
	if 'com' in allTokens:
		allTokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
return allTokens
```

The subsequent stage involves loading the gathered data and storing it in a list.

```python
allurls = 'C:\\\\Users\\\\Gabriel D\\\\Desktop\\\\Url Classification Project\\\\Data to Use\\\\allurls.txt'	#path to our all urls file
allurlscsv = pd.read_csv(allurls,',',error_bad_lines=False)	#reading file
allurlsdata = pd.DataFrame(allurlscsv)	#converting to a dataframe
 
allurlsdata = np.array(allurlsdata)	#converting it into an array
random.shuffle(allurlsdata)	#shuffling
```

With the data in our list, the next task is to vectorize the URLs. Instead of employing a bag-of-words classification, I opted for tf-idf scores. This decision was motivated by the recognition that certain words in URLs carry more significance than others, such as 'virus', '.exe', '.dat', etc. Now, let's transform the URLs into vector form using tf-idf scores.

```python
corpus = [d[0] for d in allurlsdata]	#all urls corresponding to a label (either good or bad)
vectorizer = TfidfVectorizer(tokenizer=getTokens)	#get a vector for each url but use our customized tokenizer
X = vectorizer.fit_transform(corpus) #get the X vector
```

With the vectors in hand, the next step involves converting them into both test and training data sets. We can then proceed to apply logistic regression for analysis.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)	#split into training and testing set 80/20 ratio

lgs = LogisticRegression()	#using logistic regression
lgs.fit(X_train, y_train)
print(lgs.score(X_test, y_test)) #pring the score. It comes out to be 98%
```

That concludes the process. As demonstrated, it's a straightforward yet highly effective approach. Achieving an accuracy of 98% is noteworthy, particularly in the realm of machine learning for malicious URL detection.

If you'd like to test some links to assess the model's prediction accuracy, we can certainly proceed with that. Let's go ahead and test some links.

```python
X_predict = ['wikipedia.com','google.com/search=gdsdomingues','twitter.com','www.radsport-voggel.de/wp-admin/includes/log.exe','ahrenhei.without-transfer.ru/nethost.exe','www.itidea.it/centroesteticosothys/img/_notes/gum.exe']
X_predict = vectorizer.transform(X_predict)
y_Predict = lgs.predict(X_predict)
print y_Predict #printing predicted values
```
