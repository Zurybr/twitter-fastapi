from fastapi import FastAPI

# Importar los path 
from Paths import user_route,tweet_route
app = FastAPI()

#Includes the paths from paths folder
app.include_router(user_route.router)
app.include_router(tweet_route.router)

@app.get(path='/')
def home():
    return {'work':'it'}