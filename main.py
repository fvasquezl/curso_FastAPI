from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
app.title = "My App with FasAPI"
app.version = "0.0.1"


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descriprion de la pelicula",
                "year": 2024,
                "rating": 9.8,
                "category": "Accion",
            }
        }


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 3,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
]


@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Hello World</h1>")


@app.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)


@app.get("/movies/{id}", tags=["movies"], response_model=Movie, status_code=200)
def get_movies(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=200, content=[])


@app.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    data = [item for item in movies if item["category"] == category]
    return JSONResponse(status_code=200, content=data)


@app.post("/movies/", tags=["movies"], response_model=dict, status_code=201)
def create_movies(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(
        status_code=201, content={"message": "Se ha registrado la pelicula"}
    )


@app.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def update_movies(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
        return JSONResponse(
            status_code=200, content={"message": "Se ha modificado la pelicula"}
        )


@app.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def delete_movies(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
        return JSONResponse(
            status_code=200, content={"message": "Se ha eliminado la pelicula"}
        )
    return JSONResponse(
        status_code=404, content={"message": "No se encontro ningun registro"}
    )
