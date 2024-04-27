import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('speeches.csv')  

df = df[['year', 'text']]

df.dropna(inplace=True)
df = df[df['year'].str.isdigit()]
df['year'] = df['year'].astype(int)

df['Word Lengths'] = df['text'].apply(lambda x: [len(word) for word in x.split()])

avg_word_length_by_year = df.groupby('year')['Word Lengths'].apply(lambda x: sum(map(sum, x)) / sum(map(len, x)))

avg_word_length_by_year = avg_word_length_by_year.reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(avg_word_length_by_year['year'], avg_word_length_by_year['Word Lengths'], marker='o', color='orange')
plt.title('Average Word Length by Year')
plt.xlabel('Year')
plt.ylabel('Average Word Length')
plt.grid(True)
plt.savefig("plot5.png")
