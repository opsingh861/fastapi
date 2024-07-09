from fastapi import FastAPI, Query, Path, Cookie, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://example.com",
    "https://www.example.com",
]

# adding cors
app.add_middleware(
    CORSMiddleware,
    allow_origins="localhost:8000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get('/')  # base route

async def root():
    return {"message":"Hello world"}



@app.get("/items/{item_id}") # using this we access parameters given in path
async def read_item(item_id :int |None):
    return {"item_id":item_id}

# order matters, so if you will try to define something same but with different response or logic, only the first will run
# in case of path like /users/me then firstly define this one then the dynamic one

@app.get("/users/me")
async def meRead():
    return {"name:":"My name is Aditya Dhanraj"}

@app.get("/users/{id}")
async def userFun(id:int):
    return {"user_id":id}


# Query parameters, 

# @app.get('/query/{id}')
# async def query(id:int, name:str, roll :int | None = None ):  # whatever extra will be there in function parameter will be treated as query. By giving default value none, we can make any query parameter as optional
#     return {"id":id,"name":name, "roll":roll}


# more complex one

@app.get('/users/{id}/items/{itemsId}')
async def getData(id:int, itemsId:int, q:str):
    return {"userId": id, "itemId":itemsId, "query": q}


@app.get('/bool')
async def booleanCheck(flag:bool):  # here fastapi will convert the value of boolean by itself. eg-> 1 as True and 0 as False
    return {"flag":flag}



# access body

class Item(BaseModel):
    title : str
    desc : str | None = None
    price: int

@app.post('/item/{id}')
async def itemList(id:int, item:Item):
    print(item)
    return {"id": id, "item":item}


# some more validation on body

class Smartphone(BaseModel):
    title : str
    desc : Annotated[ str | None, Query(min_length = 3, max_length = 20)] = None
    price : int
    
    
@app.post('/smartphone')
async def setSmartphone(smartphone: Smartphone):
    return {"smartphone": smartphone}
    
    


@app.get("/parameter/{param}")
async def read_items(
    q: str, param: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"param": param}
    if q:
        results.update({"q": q})
    return results


# multiple parameter as body

class Anime(BaseModel):
    title: str 
    no_season : int
    

class Movies(BaseModel):
    title: str
    duration: int
    

@app.post('/watch')
async def watch(anime:Anime, movie:Movies):
    return {"anime":anime, "movies":movie}


# cookie
@app.get('/set-cookie/')
async def set_cookie(response: Response):
    response.set_cookie(key='ads_id', value='helloworld', httponly=True)
    return {"message" : "cookie set"}


@app.get("/get-cookie/") # get cookie
async def read_items(ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}


# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

