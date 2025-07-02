from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict, List, Literal
from model.MedicalImage import MedicalImage
import utils.validator as validator

DevicesDict = Dict[str, MedicalImage]
app = FastAPI()

listDevices: List[MedicalImage] = []

@app.get("/")
def root():
    return 'API working...'

@app.get("/api/elements/")
def get_elements():
    global listDevices

    indexed = { str(i+1): device for i, device in enumerate(listDevices)  }
    return indexed

@app.get("/api/elements/{id}")
def get_element_by_id(id: str):
    for i, device in enumerate(listDevices):
        if device.get("id") == id:
            return device
    
    return 'Not Found'

@app.post("/api/elements/")
def create_element(devices: DevicesDict) :
    global listDevices

    devices_body = devices.values()

    for device in devices_body:
        if not validator.isNumber(device["data"]):
            return JSONResponse(status_code=415 , content={"error": "Some devices have data doesn't supported"})

    listDevices.extend(devices_body)

    return JSONResponse(status_code=201, content='success')

@app.put("/api/elements/{id}")
def update_element(id: str, new_device: MedicalImage):
    global listDevices

    for i, device in enumerate(listDevices):
        if device.get("id") == id:
            if not validator.isNumber(device["data"]):
                return JSONResponse(status_code=415 , content={"error": "Some devices have data doesn't supported"})
            
            device = new_device
            listDevices[i] = device

            return 'Updated'
        
    return 'Not Found'

@app.delete("/api/elements/{id}")
def delete_element(id: str):
    global listDevices

    for i, device in enumerate(listDevices):
        if device.get("id") == id:
            listDevices.pop(i)
            return 'Deleted'
        
    return 'Not Found'