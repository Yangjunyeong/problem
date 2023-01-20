import json


def dec_movies(movies):
    a = []
    for i in movies:
        revenue_json = open(f'data/movies/{i["id"]}.json', encoding='utf-8')
        revenue_list = json.load(revenue_json)

        if revenue_list['release_date'][5:7] == "12":
            a.append(revenue_list["title"])

    return a
        #revenue_list['realese_date'][:4]
      
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
