if __name__ == "__main__":
    user_items=[]
    items=[]
    for line in open('u.data'):
            user_items.append(line.split('\t'))
 
    for line in open('u.item', encoding= 'ISO-8859-1'):
            items.append(line.split('|'))
    # print('user_items[0] = '+ user_items[0])
    # print('items[0] = '+ items[0])
 
    items_hash={}
    for i in items:
        items_hash[i[0]]=i[1]
 
    # print'items_hash[1] = ',items_hash['1']
 
    for ui in user_items:
        ui[1]=items_hash[ui[1]]
 
    # print'user_items[0] = ',user_items[0]
    
    f = open('ratings.csv','w',encoding='utf-8')
    for ui in user_items:
        f.write(ui[0]+'|'+ui[1]+'|'+ui[2]+'\n')
    f.close()