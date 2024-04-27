from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('speeches.csv')

df.dropna(inplace=True)
df = df[df['year'].str.isdigit()]
df['year'] = df['year'].astype(int)

speeches_before_1945 = df[df['year'] < 1945]['text']

all_speeches = ' '.join(speeches_before_1945)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_speeches)

plt.style.use('ggplot')
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('plot3.png')
