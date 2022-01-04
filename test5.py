import pandas as pd
import numpy as np
import matplotlib.pylab as plt 

def gender_difference():
    plt.figure(figsize=(6, 6.5))
    u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv('u.user', sep='|', names=u_cols,encoding='latin-1')

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv('u.data', sep='\t', names=r_cols,encoding='latin-1')

    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] 
    movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(5),encoding='latin-1') 


    # 数据集整合

    movie_ratings = pd.merge(movies, ratings) 
    lens = pd.merge(movie_ratings, users)


    labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
    lens['age_group'] = pd.cut(lens.age, range(0, 81, 10), right=False, labels=labels)
    lens[['age', 'age_group']].drop_duplicates()[:10]


    lens.groupby('age_group').agg({'rating': [np.size, np.mean]})

    most_50 = lens.groupby('movie_id').size().sort_values(ascending=False)[:50]
    lens.set_index('movie_id', inplace=True)
    by_age = lens.loc[most_50.index].groupby(['title', 'age_group'])
    # by_age.rating.mean().head(15)
    # by_age.rating.mean().unstack(1).fillna(0)[10:20]

    # 若将上面的一句改为如下，则将电影标题置为列将年龄组置为行：

    # by_age.rating.mean().unstack(0).fillna(0)

    #获取不同性别争议最大的电影
    lens.reset_index('movie_id', inplace=True)  
    pivoted = lens.pivot_table(index=['movie_id', 'title'],
                            columns=['sex'],
                            values='rating',
                            fill_value=0)
    pivoted['diff'] = pivoted.M - pivoted.F
    # pivoted.head()
    plt.subplot(1,3,1)
    pivoted.reset_index('movie_id', inplace=True)
    disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
    disagreements.sort_values().plot(kind='barh', figsize=[9, 15],color = 'blue')
    plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
    plt.ylabel('Title')
    plt.xlabel('Average Rating Difference')

    plt.show()


if __name__ == "__main__":
    gender_difference()