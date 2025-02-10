#%%
import os
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt2
import seaborn as sns
from textblob import TextBlob as tb
from wordcloud import WordCloud,STOPWORDS
import emoji
from collections import Counter
import plotly.graph_objs as go
from plotly.offline import iplot
import warnings
from warnings import filterwarnings
import plotly.express as pex
# %%
df=pd.read_csv("Data/comments.csv")
#%%
# converted csv file to xlsm file
df.to_excel("comments.xlsm", index=False, engine="openpyxl")

# %%
df.head()
# %% checking null values
df.isnull().sum()
# %%
# Removed all the unnecessory  unnamed columns
df=df.drop(df.columns[4:],axis=1)
# %%
# Checking the null values again
df.isnull().sum()
# %%
#Drop the null values
df=df.dropna()
# %%
#Checking the values after droping the null values
df.describe()
# %%
# Checking the null values again
df.isnull().sum()
# All the null values are gone

# %%
# checking the polarity of one comment
tb("Logan Paul it's yo big day ‚ÄºÔ∏è‚ÄºÔ∏è‚ÄºÔ∏è").sentiment.polarity

# %% Sentiment Analysis
#Adding and checking the polarity of each comment
polarity=[]
for comment in df["comment_text"]:
    try:
        polarity.append(tb(comment).sentiment.polarity)
    except:
        polarity.append(0)
        
# %%
polarity
# %%
df[ "polarity"]= polarity
# %%
df.head()
# %% Wordcloud analysis
# passed positive comments in positive_comments 
filter1= df[ "polarity"]==1
positive_comments=df[filter1]
# %%
positive_comments
# %%
#passed negetive comments into negetive_comments
filter2=df["polarity"]==-1
negetive_comments=df[filter2]
# %%
negetive_comments
# %%
# Default words to eliminate
set(STOPWORDS)
# %%
type(df["comment_text"])
# %%
# we create wordcloudfrom the positive comments
#First we convert the series into string
total_positive_comments=" ".join(positive_comments["comment_text"])
# %%
#Wordcloud
wd1=WordCloud().generate(total_positive_comments)
# %%
# wordcloud for positive comments
plt2.imshow(wd1)
plt2.axis('off')
# %%
negetive_comments
# %%
total_negetive_comments=" ".join(negetive_comments["comment_text"])
# %%
wd2=WordCloud().generate(total_negetive_comments)
# %%
# worldcloud for negetive comments
plt2.imshow(wd2)
plt2.axis('off')
# %%
df["comment_text"]
# %%
#Emoji analysis
emoji_list=[]
for char in df["comment_text"].dropna( ):
    for char in char:
        if char in emoji.EMOJI_DATA:
            emoji_list.append(char)

# %%
emoji_list
# %%
# to count the occurance of character

Counter(emoji_list).most_common(10)[0][1]
# %%
# top 10 emojis
emji=[Counter(emoji_list).most_common(10)[i][0] for i in range(10)]
emji
# %%
# No of times top 10 emojies occur
freq=[Counter(emoji_list).most_common(10)[i][1] for i in range(10)]
freq
# %%

# %%
plt2.bar(emji,freq)
plt2.xlabel("Emojis")
plt2.ylabel("Frequency")

# %%
# Reading the files in the folder
files= os.listdir(r'Data/additional_data')
# %%
files
# %%
# extracting csv files only from above list
files_csv=[file for file in files if '.csv' in file]
#%%
files_csv
# %%
filterwarnings('ignore')
# %%
full_df = pd.DataFrame()
path = r'Data/additional_data'


for file in files_csv:
    current_df = pd.read_csv(path+'/'+file , encoding='iso-8859-1' )
    
    full_df = pd.concat([full_df , current_df] , ignore_index=True)
# %%
full_df.shape
 # %%
full_df[full_df.duplicated()].shape
# %%
#Drop all the duplicated values
full_df = full_df.drop_duplicates() 
# %%
full_df.shape
# %%
# Storing data into csv file
full_df[0:1000].to_csv(r'Data/youtube_sample.csv' , index=False)
# %%
#Storing data into json
full_df[0:1000].to_json(r'Data/youtube_sample.json')

# %%
json_df=pd.read_json('Data/youtube_sample.json')
json_df
# %%
json_df['items']
# %%
full_df
# %%
full_df['category_id'].unique()  
# %%
# read json file 
json_df = pd.read_json(r'Data/additional_data/US_category_id.json')
# %%
json_df["items"]
# %%
category_dict={}
for item in json_df['items'].values:
    ## cat_dict[key] = value (Syntax to insert key:value in dictionary)
    category_dict[int(item['id'])] = item['snippet']['title']

# %%
category_dict
# %%
full_df['category_name'] = full_df['category_id'].map(category_dict)
# %%
full_df
# %%
#Analysing the most liked category
plt2.figure(figsize=(12,8))
sns.boxplot(x='category_name',y='likes',data=full_df)
plt2.xticks(rotation='vertical')
  # %%
#Analysing if the people are egaging with the videos
full_df['likes_rate']=full_df['likes']/full_df['views']*100
full_df['dislikes_rate']=full_df['dislikes']/full_df['views']*100
full_df['comment_count_rate']=full_df['comment_count']/full_df['views']*100
# %%
plt2.figure(figsize=(8,6))
sns.boxplot(x='category_name',y='likes_rate',data=full_df)
plt2.xticks(rotation='vertical')
plt2.show
# %%
sns.regplot(x='views', y='likes',data=full_df)
# %%
full_df[['likes','dislikes','views']].corr()
# %%
sns.heatmap(full_df[['likes','dislikes','views']].corr(),annot=True)
# %%
cdf=full_df.groupby("channel_title").size().sort_values(ascending=False).reset_index()
# %%
cdf
# %%
cdf=cdf.rename(columns={0:'total_videos'})
# %%
pex.bar(cdf[:10],x='channel_title',y='total_videos')
# %%
plt2.figure(figsize=(8,6))
sns.boxplot(x='channel_title',y='total_videos',data=cdf[:10])
plt2.xticks(rotation='vertical')
plt2.show
# %%
