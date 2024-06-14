import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

    #MEDIAN = a      #median (baseline)
    #MID_MEDIAN = b   #median of a middle section (baseline)
    #RANDOM = c      #uniform random (stochastic baseline)
    #CONVEX = d       #random convex combination
    #ALTERNATING = e  #alternate between 0.4 and 0.6




df_1a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_1k.csv')['xronos katanomis'].mean()
df_1b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_1k.csv')['xronos katanomis'].mean()
df_1c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_1k.csv')['xronos katanomis'].mean()
df_1d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_1k.csv')['xronos katanomis'].mean()
df_1e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_1k.csv')['xronos katanomis'].mean()
    



#dataframes from all strategies 5k integers

df_5a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_5k.csv')['xronos katanomis'].mean()
df_5b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_5k.csv')['xronos katanomis'].mean()
df_5c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_5k.csv')['xronos katanomis'].mean()
df_5d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_5k.csv')['xronos katanomis'].mean()
df_5e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_5k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 10k integers

df_10a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_10k.csv')['xronos katanomis'].mean()
df_10b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_10k.csv')['xronos katanomis'].mean()
df_10c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_10k.csv')['xronos katanomis'].mean()
df_10d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_10k.csv')['xronos katanomis'].mean()
df_10e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_10k.csv')['xronos katanomis'].mean()


df_15a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_15k.csv')['xronos katanomis'].mean()
df_15b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_15k.csv')['xronos katanomis'].mean()
df_15c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_15k.csv')['xronos katanomis'].mean()
df_15d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_15k.csv')['xronos katanomis'].mean()
df_15e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_15k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 25k integers

df_25a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_25k.csv')['xronos katanomis'].mean()
df_25b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_25k.csv')['xronos katanomis'].mean()
df_25c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_25k.csv')['xronos katanomis'].mean()
df_25d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_25k.csv')['xronos katanomis'].mean()
df_25e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_25k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 50k integers

df_30a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_30k.csv')['xronos katanomis'].mean()
df_30b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_30k.csv')['xronos katanomis'].mean()
df_30c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_30k.csv')['xronos katanomis'].mean()
df_30d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_30k.csv')['xronos katanomis'].mean()
df_30e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_30k.csv')['xronos katanomis'].mean()

df_50a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_50k.csv')['xronos katanomis'].mean()
df_50b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_50k.csv')['xronos katanomis'].mean()
df_50c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_50k.csv')['xronos katanomis'].mean()
df_50d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_50k.csv')['xronos katanomis'].mean()
df_50e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_50k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 75k integers

df_75a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_75k.csv')['xronos katanomis'].mean()
df_75b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_75k.csv')['xronos katanomis'].mean()
df_75c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_75k.csv')['xronos katanomis'].mean()
df_75d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_75k.csv')['xronos katanomis'].mean()
df_75e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_75k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 100k integers

df_100a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_100k.csv')['xronos katanomis'].mean()
df_100b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_100k.csv')['xronos katanomis'].mean()
df_100c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_100k.csv')['xronos katanomis'].mean()
df_100d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_100k.csv')['xronos katanomis'].mean()
df_100e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_alternating_100k.csv')['xronos katanomis'].mean()



x1= ['1K','5k','10k','15','25k','30k','50k','75k','100k']  

plt.plot(x1,[df_1a,df_5a,df_10a,df_15a,df_25a,df_30a,df_50a,df_75a,df_100a], label = 'Median strategy')
plt.plot(x1,[df_1b,df_5b,df_10b,df_15b,df_25b,df_30b,df_50b,df_75b,df_100b], label = 'Mid-median strategy')
plt.plot(x1,[df_1c,df_5c,df_10c,df_15c,df_25c,df_30c,df_50c,df_75c,df_100c], label = 'Random strategy')
plt.plot(x1,[df_1d,df_5d,df_10d,df_15d,df_25d,df_30d,df_50d,df_75d,df_100d], label = 'Convex strategy')
plt.plot(x1,[df_1e,df_5e,df_10e,df_15e,df_25e,df_30e,df_50e,df_75e,df_100e], label = 'Alternating strategy')



plt.legend()
plt.show()






'''
sum1 = df1['xronos katanomis'].sum()
max1 = df1['xronos katanomis'].max()
min1 = df1['xronos katanomis'].min()
'''