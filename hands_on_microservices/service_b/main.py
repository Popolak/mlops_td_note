from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch


#SERVEUR -> BDD
app = FastAPI()
es = Elasticsearch(["http://localhost:8000"])

@app.get("/data")
async def get_data():
    return {"message": "Hello from Service B!"}

# Endpoint pour ajouter un document
@app.post("/add/")
def add_document(index: str, document: dict):
    try:
        response = es.index(index=index, document=document)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint pour rechercher des documents
@app.get("/search/")
def search_documents(index: str, query: dict):
    try:
        response = es.search(index=index, query=query)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
