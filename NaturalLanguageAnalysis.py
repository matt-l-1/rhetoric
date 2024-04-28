import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.probability import FreqDist
from nltk.corpus import wordnet
from gensim import corpora, models
import csv
import os

# Function to read speeches from CSV file
def read_speeches_from_csv(file_path):
    speeches = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            speeches.append(row['text'])
    return speeches

# Tokenize and preprocess speech text
def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())  # Tokenize and convert to lowercase
    tokens = [token for token in tokens if token.isalnum()]  # Remove non-alphanumeric tokens
    tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens
    return tokens

# Topic modeling using LDA
def topic_modeling(speech_texts):
    tokenized_texts = [preprocess_text(text) for text in speech_texts]
    dictionary = corpora.Dictionary(tokenized_texts)
    corpus = [dictionary.doc2bow(text) for text in tokenized_texts]
    lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=20)
    return lda_model.print_topics()

# Sentiment analysis using sentiment intensity analyzer
def sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)
    return sentiment_score['compound']

import pandas as pd

# Read speeches from CSV file
speeches_df = pd.read_csv('speeches.csv')

# Initialize lists to store data
speech_numbers = []
speakers = []
years = []
topics_lists = []
sentiment_scores = []

# Perform topic modeling and sentiment analysis for each speech
for i, row in speeches_df.iterrows():
    speech_number = i + 1
    speech_text = row['text']
    speaker = row['speaker']
    year = row['year']
    
    # Topic modeling
    topics = topic_modeling([speech_text])
    
    # Sentiment analysis
    sentiment_score = sentiment_analysis(str(speech_text))
    
    # Append data to lists
    speech_numbers.append(speech_number)
    speakers.append(speaker)
    years.append(year)
    topics_lists.append(topics)
    sentiment_scores.append(sentiment_score)

# Create DataFrame
speech_analysis_df = pd.DataFrame({
    'Speech Number': speech_numbers,
    'Speaker': speakers,
    'Year': years,
    'Topics': topics_lists,
    'Sentiment Score': sentiment_scores
})

# Define the path for the Excel file
excel_file_path = 'speech_analysis.xlsx'

# Save the DataFrame to an Excel file
speech_analysis_df.to_excel(excel_file_path, index=False)

print("DataFrame successfully saved to Excel file:", excel_file_path)
