import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

#create data frame with csv
happy_df = pd.read_csv("rank.csv")
print(happy_df.head())

#measuring the happiness gap between the old and the young
rank_gap = happy_df['rank_young'] - happy_df['rank_old']
ladder_vector = happy_df['ladder_score']

#scatterplot that maps the overall happiness score to the rank gap
plt.scatter(rank_gap, ladder_vector)

#happiness trajectory line graph
plt.plot(rank_gap, )

#dumbell curve

