from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from typing import  List
import argparse
import utils.validator as validator
from model.MedicalImage import MedicalImage, DevicesDict
from database.config import Config
from database.query import Query
from utils.normalize import normalize

parser = argparse.ArgumentParser(description="Argumentos de conexion a la BD")

app = FastAPI()

listDevices: List[MedicalImage] = []

#Leer argumentos de conexion enviados en los parametros del script
parser.add_argument("--username", type=str, help="Username DB")
parser.add_argument("--password", type=str, help="Password DB")
parser.add_argument("--database", type=str, help="DB Name")
parser.add_argument("--host", type=str, default='localhost', help="Host DB")
parser.add_argument("--port", type=str, default=5432, help="Port DB")

args = parser.parse_args()

#Usar los argumentos enviados para configurar la BD 
config = Config(username=args.username, password=args.password, database=args.database, host=args.host, port=args.port)

#Crear un objeto query que es el que me va a ayudar con las consultas a la BD
query = Query(config)

@app.get("/")
def root():
    return 'API working...'

@app.get("/api/elements/")
def get_elements():
    listaDevices = query.get_elements()
    indexed = { str(i+1): device for i, device in enumerate(listaDevices)  }
    return indexed

@app.get("/api/elements/{id}")
def get_element_by_id(id: str):
    found = query.get_element_by_id(id)
    if found is None:
         return JSONResponse(status_code=404, content= {"message": "id not found"})
    else:
         return JSONResponse(status_code=200, content=found)


@app.post("/api/elements/")
def create_element(devices: DevicesDict) :
    devices_body = devices.values()

    for device in devices_body:
        if not validator.isNumber(device["data"]):
            return JSONResponse(status_code=415 , content={"error": "Some devices have data doesn't supported"})
        
        normalize(device)

    created = query.create_images(devices_body)
    if created:
        return JSONResponse(status_code=201, content='success')
    else:
        return JSONResponse(status_code=500, content='error')
        

@app.put("/api/elements/{id}")
def update_element(id: str, new_image: MedicalImage):
    if not validator.isNumber(new_image["data"]):
                return JSONResponse(status_code=415 , content={"error": "Some devices have data doesn't supported"})
    
    updated = query.update_image(id, new_image)
    if updated:
         return JSONResponse(status_code=200, content='success')
    else:
         return JSONResponse(status_code=500, content='error')

@app.delete("/api/elements/{id}")
def delete_element(id: str):
     deleted = query.delete_element(id)
     if deleted:
          return JSONResponse(status_code=200, content='success')
     else:
          return JSONResponse(status_code=500, content='error')

@app.get('create_db')
def create_db():
     created: str = query.create_db()
     if created == 'success':
        return JSONResponse(status_code=200, content='success')
     else: 
          return JSONResponse(status_code=500, content=created)
          

#Como necesitamos pasar argumentos directamente desde el commandline, corremos el uvicorn "manualmente"
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )