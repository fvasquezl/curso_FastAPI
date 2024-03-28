## Instructions to run this API

### Clone the repository
```
$ cd curso_FastAPI
$ pipenv install -r requirements.txt
$ pipenv shell 
$ uvicorn main:app --reload --port 5000 --host 0.0.0.0

```
### Open the browser
```
localhost:5000/docs
```
## Information
### HTTP response status code 
```
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


-Informational responses (100 – 199)
-Successful responses    (200 – 299)
-Redirection messages    (300 – 399)
-Client error responses  (400 – 499)
-Server error responses  (500 – 599)

```