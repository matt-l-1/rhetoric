import pandas as pd
from nltk import ngrams, FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import matplotlib.pyplot as plt

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
    text = re.sub("U.S.A.", "America", text)
    text = re.sub("U.K.", "Britain", text)
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    tokens = [token for token in tokens if token.isalnum()]  # Remove non-alphanumeric tokens
    tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
    tokens = [lemmatizer.lemmatize(token) for token in tokens if len(token) > 2]  # Lemmatize tokens
    return tokens


# Read speeches from CSV file
speeches_df = pd.read_csv('speeches.csv')

# Initialize array to store data
df_main = pd.DataFrame()

for i, row in speeches_df.iterrows():

    speaker = row['speaker']
    try:
        party = str(re.search(r'\((.*?)\)',speaker).group(1))
    except:
        continue

    speech_number = i + 1
    speech_text = row['text']

    tokenized_text = preprocess_text(speech_text)

    frequency = FreqDist(token.lower() for token in tokenized_text)

    df = pd.DataFrame(frequency.items(), columns=['Word','Frequency'])
    df['Year'] = row['year']
    df['Speech Number'] = speech_number
    df['Party'] = party

    df_main = pd.concat([df, df_main], ignore_index=True)

    print(speech_number)

pt = pd.pivot_table(df_main, values=['Frequency'], index=['Word'], columns=['Party'], aggfunc='sum')
pt.to_excel('frequency_by_party.xlsx')



