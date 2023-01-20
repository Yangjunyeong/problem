import json
from pprint import pprint
# id,1title,1poster_path,1vote_average,1overview,1genre_ids

def movie_info(movie):
    m_info = {
        'id' : movie.get('id'),
        'title' :movie.get('title'),
        'poster_path' :movie.get('poster_path'),
        'vote_average' :movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')

    }

    # m_info['genre_names']= movie.get['genre_ids'][1]
    return m_info
    
        
     
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))