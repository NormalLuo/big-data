import matplotlib.pyplot as plt 
import operator
from matplotlib.pyplot import MultipleLocator
import pandas as pd
import numpy as np

user_movie = 'u.data'
movie_information = 'u.item'
user_information = 'u.user'

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def score_analysis(): #电影评分分析
    scores = {"1":0,"2":0,"3":0,"4":0,"5":0}
    for line in open(user_movie):
        user, item, score = line.split('\t')[0:3]
        scores[score] += 1

    x1 = scores.keys() #用字典的键也就是分数作为x轴
    y1 = scores.values() #用字典键对应的值也就是打分人数作为y轴
    # print(scores)

    plt.figure(figsize=(19, 10))
    plt.subplot(2,3,2)
    plt.bar(x1,y1,color = 'slateblue',width = 0.95)
    plt.title("电影评分统计图",fontsize=14)
    # plt.xlabel("影片评分 (0-5)",fontsize=14)
    plt.ylabel("评分人数",fontsize = 14)


def movie_year_analysis(): #电影年份分析
    yearCounts = {} #用来统计电影年份与数量的对应关系
    for year in range(1922,1999):  #按照数据集中电影的年份信息 生成年份字典
        yearCounts[str(year)] = 0


    for line in open(movie_information,encoding='ISO-8859-1'):
        release_date = line.split('|')[2]
        release_year = release_date[-4:]
        if release_year == "": continue
        yearCounts[release_year] += 1

    x2 = list(yearCounts.keys()) #获取x轴坐标并转为列表
    y2 = list(yearCounts.values())#获取y轴坐标并转为列表

    plt.subplot(2,3,5)

    plt.plot(x2,y2,label = '电影数量',color = 'cornflowerblue')
    plt.legend(loc="upper right") #设置标签图在右上角
    x_major_locator=MultipleLocator(5) #设置x轴间隔为5
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.xticks(rotation = -60) #将x轴坐标旋转60度
    x_new = range(1922,1998)
    plt.title("电影年份统计图",fontsize=14)
    plt.xlabel("年份",fontsize=14)
    plt.ylabel("电影数量",fontsize = 14)
    # plt.show()

def occuptin_analysis():   


    occuption_count = {}
    for line in open(user_information): 
        occuption = line.split('|')[3]
        occuption_count[occuption] = occuption_count.get(occuption,0) + 1 #统计职业及其对应人数

    sort_occuption_counts = sorted(occuption_count.items(),key=lambda k: k[1]) #将结果从小到大排序
    # print(sort_occuption_counts)

    sort_occuption = {}
    for i in sort_occuption_counts: #将排序结果存回字典
        sort_occuption[i[0]] = i[1]
    # print(sort_occuption)

    x4 = sort_occuption.keys()
    y4 = sort_occuption.values()
    plt.subplot(2,3,6)
    plt.bar(x4,y4,color = 'blue',width = 0.8)
    plt.xticks(rotation = -60) #将x轴坐标旋转60度
    # plt.title("用户职业统计情况",fontsize=14)
    plt.xlabel("职业",fontsize=14)
    plt.ylabel("人数",fontsize=14)



def gender_analysis():
    unames = ['userid','age','gender','occupation','zip code']
    users = pd.read_table('u.user',sep = '\|',names = unames)
    rnames = ['userid','itemid','rating','timestamp']
    ratings = pd.read_table('u.data',names = rnames,engine = 'python')
    inames = ['itemid','movie title','release date','video release date','IMDB URL','unknown','Action','Adventure'
            ,'Animation','Children\'s','Comedy','Crime','DOcumentrary','Drama','Fatasy','Film-Noir','Horror','Musical'
            ,'Mystery','Romance','Sci-Fi','Thriller','War','Western']
    items = pd.read_table('u.item',sep = '\|',names = inames,engine = 'python')
    
    #计算男女生对电影评分的平均值和标准差
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

def gender_compare():
    u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv(user_information, sep='|', names=u_cols,encoding='latin-1')

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv(user_movie, sep='\t', names=r_cols,encoding='latin-1')

    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] 
    movies = pd.read_csv(movie_information, sep='|', names=m_cols, usecols=range(5),encoding='latin-1') 

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

    lens.reset_index('movie_id', inplace=True)  
    pivoted = lens.pivot_table(index=['movie_id', 'title'],
                            columns=['sex'],
                            values='rating',
                            fill_value=0)
    pivoted['diff'] = pivoted.M - pivoted.F

    plt.subplot(2,3,3)
    users.age.plot.hist(bins=30,edgecolor='black')
    
    plt.title("用户年龄分布图",fontsize=14)
    plt.ylabel('用户数量',fontsize=14)
    plt.xlabel('用户年龄',fontsize=14)


    pivoted.reset_index('movie_id', inplace=True)
    disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
    plt.subplot(1,3,1)
    disagreements.sort_values().plot(kind='barh',color = 'dodgerblue')
    plt.title('男/女性平均评分\n(差异>0=受男性青睐)',fontsize=14)
    plt.ylabel('电影',fontsize=14)
    plt.xlabel('平均评级差',fontsize=14)




if __name__ == "__main__":
    score_analysis()
    movie_year_analysis()
    gender_analysis()
    gender_compare()
    occuptin_analysis()
    plt.show()