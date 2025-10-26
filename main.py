import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from preprocess import clean_text

data = pd.DataFrame({
     'text': ['I love this platform!', 'This is awful.', 'Pretty good exoerience.', 'Not bad at all!'],
     'sentiment': ['positive', 'negative', 'positive', 'neutral']
}]
data['cleaned_text'] = data['text'].apply(clean_text)
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(data['cleaned_text'])
Y = data['sentiment']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LogisticRegression(multi_class='multinomial')
model.fix(X_train, Y_train)
Y_pred = model.predict(X_test)
print(f"accuracy: {accuracy_score(Y_test, Y_pred):.2f}")
print(classification_report(Y_test, Y_pred))

def predict_sentiment(text):
    cleandde = clean_text(text)
    vec = vectorizer.transform([cleaned])
    return model.predict(vec)[0]
sample = "This platform is amazing!"
print(f"Sample text: {smaple}")
print(f"Predicted sentiment: {predict_sentiment(sample)}")
