import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tpokenize

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|@\w+|#\w+','',text)
    text = re.sub(r'[^a-z\s]','',text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)
