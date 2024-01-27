import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

    #MEDIAN = a      #median (baseline)
    #MID_MEDIAN = b   #median of a middle section (baseline)
    #RANDOM = c      #uniform random (stochastic baseline)
    #CONVEX = d       #random convex combination
    #ALTERNATING = e  #alternate between 0.4 and 0.6





    



#dataframes from all strategies 5k integers

df_5a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_5k.csv')['xronos katanomis'].mean()
df_5b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_5k.csv')['xronos katanomis'].mean()
df_5c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_5k.csv')['xronos katanomis'].mean()
df_5d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_5k.csv')['xronos katanomis'].mean()
df_5e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_5k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 10k integers

df_10a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_10k.csv')['xronos katanomis'].mean()
df_10b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_10k.csv')['xronos katanomis'].mean()
df_10c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_10k.csv')['xronos katanomis'].mean()
df_10d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_10k.csv')['xronos katanomis'].mean()
df_10e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_10k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 25k integers

df_25a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_25k.csv')['xronos katanomis'].mean()
#df_25b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_25k.csv')['xronos katanomis'].mean()
df_25c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_25k.csv')['xronos katanomis'].mean()
#df_25d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_25k.csv')['xronos katanomis'].mean()
#df_25e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_25k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 50k integers
'''
df_50a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_50k.csv')['xronos katanomis'].mean()
df_50b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_50k.csv')['xronos katanomis'].mean()
df_50c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_50k.csv')['xronos katanomis'].mean()
df_50d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_50k.csv')['xronos katanomis'].mean()
df_50e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_50k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 75k integers

df_75a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_75k.csv')['xronos katanomis'].mean()
df_75b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_75k.csv')['xronos katanomis'].mean()
df_75c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_75k.csv')['xronos katanomis'].mean()
df_75d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_75k.csv')['xronos katanomis'].mean()
df_75e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_75k.csv')['xronos katanomis'].mean()

#dataframes from all strategies 100k integers

df_100a = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_median_100k.csv')['xronos katanomis'].mean()
df_100b = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_mid_median_100k.csv')['xronos katanomis'].mean()
df_100c = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_100k.csv')['xronos katanomis'].mean()
df_100d = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_convex_100k.csv')['xronos katanomis'].mean()
df_100e = pd.read_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_altern_100k.csv')['xronos katanomis'].mean()
'''

'''
sum1 = df1['xronos katanomis'].sum()
max1 = df1['xronos katanomis'].max()
min1 = df1['xronos katanomis'].min()
'''
x1= ['5k','10k']  
x = ['5k','10k','25k']
plt.plot(x,[df_5a,df_10a,df_25a], label = 'Median strategy')
plt.plot(x1,[df_5b,df_10b], label = 'Mid-median strategy')
plt.plot(x,[df_5c,df_10c,df_25c], label = 'Random strategy')
plt.plot(x1,[df_5d,df_10d], label = 'Convex strategy')
plt.plot(x1,[df_5e,df_10e], label = 'Alternating strategy')

plt.legend()
plt.show()

