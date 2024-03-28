from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My App with FasAPI"
app.version = "0.0.1"

movies = [
      {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
        {
        "id": 3,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}',tags=['movies'])
def get_movies(id: int):
    for item in movies:
        if item["id"] == id:
          return item
    return []

@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str,year:int):
    items = [item for item in movies if item['category']==category]
    return items

@app.post('/movies/',tags=['movies'])
def create_movies(id:int=Body(), title:str=Body(), overview:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": str(year),
        "rating": rating,
        "category": category
    })
    return movies

@app.put('/movies/{id}',tags=['movies'])
def update_movies(id:int, title:str=Body(), overview:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title']= title
            movie["overview"]= overview
            movie["year"]= year
            movie["rating"] =rating
            movie["category"]= category
    return movies

@app.delete('/movies/{id}',tags=['movies'])
def delete_movies(id:int):
    for movie in movies:
        if movie['id'] == id:
           index = movies.index(movie)
           movies[index]=''
    return movies
