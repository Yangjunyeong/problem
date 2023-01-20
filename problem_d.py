import json


def max_revenue(movies):
    a = []
    for i in movies:
        revenue_json = open(f'data/movies/{i["id"]}.json', encoding='utf-8')
        revenue_list = json.load(revenue_json)
        a.append(revenue_list['revenue'])

    for i in movies:
        revenue_json = open(f'data/movies/{i["id"]}.json', encoding='utf-8')
        revenue_list = json.load(revenue_json)

        if max(a) == revenue_list['revenue']:
            return revenue_list['title']
    

        
        
    
    
    
      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
