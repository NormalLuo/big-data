import pandas as pd
import numpy as np
import matplotlib.pylab as plt 

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('u.user', sep='|', names=u_cols,encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols,encoding='latin-1')

m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] 
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(5),encoding='latin-1') 


movie_ratings = pd.merge(movies, ratings) 
lens = pd.merge(movie_ratings, users)

users.age.plot.hist(bins=30,edgecolor='black')

plt.title("用户年龄分布图")
plt.ylabel('用户数量')
plt.xlabel('用户年龄')
plt.show()