from fastapi import FastAPI
from Routes import route
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()

# Conectando Com O MongoDB
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URL"])
    app.database = app.mongodb_client[config["MONGO_DB"]]

# Fechando Concexão
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


# Incluindo As Rotas
app.include_router(route.router)




