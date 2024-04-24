import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("top_100_words_in_politics.xlsx")

plt.barh(df["Word"][:25], df["SUM"][:25])
plt.ylabel("Word")
plt.xlabel("Word Frequency")
plt.show()
