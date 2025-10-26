# x-sentiment-analysis
A machine learning project to classify X posts as positive, negative, or neutral using NLP.
 
## Rquirements
 - Python 3.8+
 - librqries: see 'requirments.txt'
 - Dataset: [sentiment140](http://www.sentiment140.com/)

## Setup
1. Clone the repo: 'git clone https://github.com/yourusername/x-sentiment-analysis.git'
2. Install dependencies: 'pip install -r requirements.txt'
3. Downland a sentiment dataset and update 'main.py' to load it.
4. Run the model:'python main.py'
5. Launch the demo: 'streamlit run app.py'

## Features
- Text preprocessing (removes URLs, stop words, etc.).
- Logistic regression model with TF-IDF vectorization.
- Interactiveweb app with Streamlit.

## Next Steps
- Use the X API for live data.
- Try deep learning witg HUgging Face Transformers.
- Improve preprocessing with lemmatization.
- 
