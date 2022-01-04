import pandas as pd
import numpy as np
def gender_analysis():
    unames = ['userid','age','gender','occupation','zip code']
    users = pd.read_table('u.user',sep = '\|',names = unames)
    rnames = ['userid','itemid','rating','timestamp']
    ratings = pd.read_table('u.data',names = rnames,engine = 'python')
    inames = ['itemid','movie title','release date','video release date','IMDB URL','unknown','Action','Adventure'
            ,'Animation','Children\'s','Comedy','Crime','DOcumentrary','Drama','Fatasy','Film-Noir','Horror','Musical'
            ,'Mystery','Romance','Sci-Fi','Thriller','War','Western']
    items = pd.read_table('u.item',sep = '\|',names = inames,engine = 'python')
    
    #任务一：计算男女生对电影评分的平均值和标准差
    users_df = pd.DataFrame()
    users_df['userid'] = users['userid']
    users_df['gender'] = users['gender']
    ratings_df = pd.DataFrame()
    ratings_df['userid'] = ratings['userid']
    ratings_df['rating'] = ratings['rating']
    rating_df = pd.merge(users_df,ratings_df)
    gender_table = pd.pivot_table(rating_df,index = ['gender','userid'],values = 'rating')
    gender_df = pd.DataFrame(gender_table)
    Female_df = gender_df.query("gender == ['F']")
    Male_df = gender_df.query("gender == ['M']")
    print("男性电影评分平均值："+str(Male_df.rating.sum()/len(Male_df.rating)) +" 标准差："+str(np.std(Male_df.rating)))
    print("女生电影评分平均值："+str(Female_df.rating.sum()/len(Female_df.rating))+"标准差："+str(np.std(Female_df.rating)))
    # print("男生电影评分标准差："+str(np.std(Male_df.rating)))
    # print("女生电影评分标准差："+str(np.std(Female_df.rating)))
    #计算男女生最喜欢的十部电影
    ratings_df_2 = pd.DataFrame()
    ratings_df_2['userid'] = ratings['userid']
    ratings_df_2['rating'] = ratings['rating']
    ratings_df_2['itemid'] = ratings['itemid']
    items_df = pd.DataFrame()
    items_df['itemid'] = items['itemid']
    items_df['movietitle'] = items['movie title']
    
    tmp = pd.merge(users_df,ratings_df_2)
    gender_item_df = pd.merge(tmp,items_df)
    Female_item_df = gender_item_df.query("gender == ['F']")
    Male_item_df = gender_item_df.query("gender == ['M']")
    print("女生最爱看的五部电影")
    print(Female_item_df.groupby(['movietitle']).rating.mean().sort_values(ascending = False)[0:5,])
    print("男生最爱看的五部电影")
    print(Male_item_df.groupby(['movietitle']).rating.mean().sort_values(ascending = False)[0:5,])   



if __name__ == "__main__":
    gender_analysis()