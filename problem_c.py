import json
from pprint import pprint


def movie_info(movies, genres):
    b = []
    for ids in movies:
        move_name = {
            'id' : ids.get('id'),   
            'title' : ids.get('title'),
            'poster_path' : ids.get('poster_path'),
            'vote_average' : ids.get('vote_average'),
            'overview' : ids.get('overview'),
            'genre_names' : ids.get('genre_ids')
        }
        a= []
        for i in ids.get('genre_ids'):
            for j in genres:
                if j['id'] == i:
                    a.append(j['name'])
        move_name['genre_names'] = a  
        b.append(move_name)

    return b

    
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
