import json
from pprint import pprint


def movie_info(movie, genres):
    a= []
    for ids in movie.get('genre_ids'):
        for j in genres:
            if j['id'] == ids:
                a.append(j['name'])
    move_name = {
        'id' : movie.get('id'),   
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : movie.get('genre_ids')
        }
    
    move_name['genre_names'] = a                


    

    return move_name
      
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
