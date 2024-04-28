import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('speeches.csv')

df.dropna(inplace=True)
df = df[df['year'].str.isdigit()]
df['year'] = df['year'].astype(int)

df['Num Words'] = df['text'].apply(lambda x: len(x.split()))

df = df[df['Num Words'] > 10]

plt.figure(figsize=(10, 6))
plt.scatter(df['year'], df['Num Words'], marker='o', color='orange')
plt.title('Number of Words in Each Speech by Year')
plt.xlabel('Year')
plt.ylabel('Number of Words')
plt.grid(True)
plt.savefig("plot6.png")
