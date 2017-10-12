
#Importing the Necessary Libraries and Initializing Graph/Plot Dimensions

import seaborn as sea
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.figure(figsize=(22, 14))
sea.mpl.rc("figure", figsize=(30,25))



#Importing Data Set
oct_stats = pd.read_csv('October.csv')

#Viewing Column Headers
oct_stats.head()

#Storing Data Set in Data Frame
df1 = pd.DataFrame(oct_stats)


#Getting albums
albums = df1.groupby("Release_Title")



#Getting Net Revenue
revenue = df1.groupby("Net_Revenue_in_USD")


#Plotting Albums with the Gross Revenue
sea.barplot(x="Release_Title", y="Gross_Revenue_in_USD", data=oct_stats)



#Plotting Tracks with the Net Revenue
sea.barplot(x="Track_Title", y="Net_Revenue_in_USD", data=oct_stats)



# Count plotting to find out which region has most number of plays
sea.mpl.rc("figure", figsize=(50,40))
sea.countplot(x='Country', data=oct_stats)


# Count plotting to find out which artist has most number of plays
sea.mpl.rc("figure", figsize=(10,6))
sea.countplot(x='Artist', data=oct_stats)


# Distribution Plot (a.k.a. Histogram)
sea.distplot(oct_stats.Net_Revenue_in_USD)



# Calculate correlations
corr = oct_stats.corr()
 
sea.heatmap(corr)


# Density Plot
sea.kdeplot(oct_stats.Net_Revenue_in_USD, oct_stats.Gross_Revenue_in_USD)


# Count plotting to find out which service has most number of plays
sea.mpl.rc("figure", figsize=(10,6))
sea.countplot(x='Service', data=oct_stats)


