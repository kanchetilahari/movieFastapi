from fastapi import FastAPI,Query,Body

app=FastAPI()
movies=[
    {"id":1,"movie_name":"The Dark Knight","genre":"Action","language":"English","rating":6},
    {"id":2,"movie_name":"Inception","genre":"Thriller","language":"English","rating":8},
    {"id":3,"movie_name":"KGF","genre":"Drama","language":"Hindi","rating":9},
    {"id":4,"movie_name":"Thalapathi","genre":"action","language":"Tamil","rating":5},
    {"id":5,"movie_name":"Avathar","genre":"Sci-Fi","language":"English","rating":8}
]

@app.get("/")
def home():
    return {"message":"Movie API is running"}

@app.get('/get_all_movies')
def view_all_movies():
    return{"operation":"GET",
           "result":movies}

@app.get('/get_single_movie_by_id')
def single_movie_id(movie_id:int):
    for movie in movies:
        if movie["id"]==movie_id:
            return {"request":"GET",
                    "result":movie}
    return{"message":"movie not found"}

@app.get('/filter')
def filter_movies(genre:str=Query(None),language:str=Query(None),rating:int=Query(None)):
    filtered=movies
    if genre:
        filtered=[movie for movie in filtered
                  if movie['genre']==genre]
    if language:
        filtered=[movie for movie in filtered 
                  if movie['language']==language]
    if rating:
        filtered=[movie for movie in filtered
                if movie['rating']>=rating]
    return filtered

@app.post('/add_movie')
def add_new_movie(addnewmovie:dict=Body()):
    movies.append(addnewmovie)
    return {"message":"Movie added successfully"}

@app.put('/update_a_movie_by_id/{movie_id}')
def  update_movie(movie_id:int,updated_movie:dict=Body()):
    for movie in movies:
        if movie["id"]==movie_id:
            movie.update(updated_movie)
            return{"message":"Movie updated successfully"}
    return{"message":"Movie not found"}

@app.delete('/delete_movie_by_id/{movie_id}')

def delete_movie(movie_id:int):
    for movie in movies:
        if movie["id"]==movie_id:
            movies.remove(movie)
            return {"message":"Movie deleted successfully"}
    return{"message":"movie not found"}
